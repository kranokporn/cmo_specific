# -*- coding: utf-8 -*-
from openerp import models, fields, api, tools
from num2words import num2words


class ReportCustomerReceiptVoucher(models.Model):
    _name = 'report.customer.receipt.voucher'
    _auto = False

    voucher_id = fields.Many2one(
        'account.voucher',
        string='Voucher',
    )
    analytic_account_id = fields.Many2one(
        'account.analytic.account',
        string='Project',
    )
    amount_taxed = fields.Float(
        string='Amount Taxed',
    )
    bank_receipt_id = fields.Many2one(
        'account.bank.receipt',
        string='Bank Reciept',
    )
    move_line_id = fields.Many2one(
        'account.move.line',
        string='Move Line',
    )

    def _get_sql_view(self):
        sql_view = """
            SELECT ROW_NUMBER()
                    OVER(ORDER BY av.id, aml2.analytic_account_id) AS id,
                   av.id AS voucher_id,
                   aml2.analytic_account_id,
                   -- SUM(aml2.credit-aml2.debit) AS amount_taxed,
                   av.amount AS amount_taxed,
                   abr.id AS bank_receipt_id,
                   aml.id AS move_line_id
            FROM account_voucher_line avl
            INNER JOIN account_voucher av ON avl.voucher_id = av.id
            LEFT JOIN account_bank_receipt abr ON av.bank_receipt_id = abr.id
            LEFT JOIN account_move_line aml ON avl.move_line_id = aml.id
            LEFT JOIN (
                SELECT aml.move_id, aml.analytic_account_id, aml.debit,
                       aml.credit
                FROM account_move_line aml
                LEFT JOIN account_account aa ON aml.account_id = aa.id
                WHERE aa.type != 'receivable' AND aa.id NOT IN (
                    SELECT account_collected_id
                    FROM account_tax
                    UNION
                    SELECT account_paid_id
                    FROM account_tax
                )
            ) aml2 ON aml.move_id = aml2.move_id
            WHERE av.type = 'receipt' AND av.state = 'posted'
            GROUP BY av.id, aml2.analytic_account_id, abr.id, aml.id
        """
        return sql_view

    def init(self, cr):
        tools.drop_view_if_exists(cr, self._table)
        cr.execute("""CREATE OR REPLACE VIEW %s AS (%s)"""
                   % (self._table, self._get_sql_view()))

    @api.multi
    def get_text_total_amount(self, total_amount):
        return num2words(total_amount, to='currency', lang='th')

    @api.multi
    def _get_wht_all(self):
        wht = []
        for rec in self:
            for wht_line in rec.voucher_id.tax_line_wht:
                wht.append(wht_line.tax_id)
        return list(set(wht))

    @api.multi
    def _filter_wht_line(self, type):
        tax_line_wht = self.mapped('voucher_id').mapped('tax_line_wht')
        wht_type = tax_line_wht.filtered(lambda l: l.tax_id == type)
        return sum(wht_type.mapped('amount'))

    @api.multi
    def _get_amount_all(self, amount_taxed, total_wht=0.0,
                        total_vat=0.0, diff_amount=0.0):
        self.ensure_one()
        amount_untaxed = amount_taxed
        # check tax
        if total_vat:
            amount_untaxed /= 1.07
        taxed = amount_taxed - amount_untaxed
        amount_untaxed_wht = amount_untaxed + total_wht - diff_amount
        return amount_untaxed_wht, taxed

    @api.multi
    def get_vat(self):
        voucher_ids = self.mapped('voucher_id')
        move_line_ids = voucher_ids.mapped('line_ids').mapped('move_line_id') \
            .mapped('move_id').mapped('line_id')
        # Get Account of Tax
        self._cr.execute("""
            select account_collected_id from account_tax
            union
            select account_paid_id from account_tax""")
        vat_account_ids = map(lambda l: l[0], self._cr.fetchall())
        vat_move_line_ids = move_line_ids.filtered(
            lambda l: l.account_id.id in vat_account_ids)
        total_credit_vat = sum(vat_move_line_ids.mapped('credit'))
        total_debit_vat = sum(vat_move_line_ids.mapped('debit'))
        return total_credit_vat - total_debit_vat

    @api.multi
    def get_value_wizard(self):
        Wizard = self.env['customer.receipt.voucher']
        wizard = Wizard.browse(self.env.context.get('active_id'))
        return wizard
