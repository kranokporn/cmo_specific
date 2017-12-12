# -*- coding: utf-8 -*-
{
    "name": "CMO :: Install CMO Addons",
    "summary": "",
    "version": "8.0.1.0.0",
    "category": "Uncategorized",
    "description": """


    """,
    "website": "http://203.146.226.60",
    "author": "Phongyanon Y.,",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        # Standard Module for most SMEs.
        'sale',
        "purchase",
        "stock",
        "sale_stock",
        "project",
        "account",
        # Thai Localization Module
        "sale_split_quote2order",
        "sale_invoice_plan",
        "purchase_invoice_plan",
        "account_billing",
        "account_billing_hook_recompute_vline",
        "l10n_th_account",
        "account_bank_receipt",
        "l10n_th_tax_report",
        "jasper_reports",
        "account_invoice_check_tax_lines_hook",
        "l10n_th_account_pnd_form",
        "l10n_th_account_tax_detail",
        "l10n_th_address",
        "account_pettycash",
        "account_cancel_reversal",
        "web_m2x_options",
        "web_hideleftmenu",
        "web_sheet_full_width",
        "web_invalid_tab",
        "stock_no_negative",
        # "stock_asset",
        "account_financial_report",
        "hr_expense_advance_clearing",
        # "purchase_analytic_plans",
        # "sale_analytic_plans",
        # Additional Module
        "sale_operating_unit",
        "purchase_operating_unit",
        "account_operating_unit",
        "sale_layout",
        "web_translate_dialog",
        "sale_discount_total",
        "account_asset_management",
        "meta_groups",
        # CMO Specific
        "account_asset_depreciation_xls",
        "account_asset_management_enhanced",
        "cmo_account",
        "cmo_account_bank_receipt",
        "cmo_constrain_enhance",
        "cmo_cost_control_sheet",
        "cmo_customer_invoice_report",
        "cmo_doctype_order",
        "cmo_hr",
        "cmo_hr_expense_report",
        "cmo_hr_level_validation",
        "cmo_import_xlsx",
        "cmo_level_validation",
        "cmo_product",
        "cmo_project",
        "cmo_purchase",
        "cmo_purchase_invoice_plan",
        "cmo_purchase_level_validation",
        "cmo_purchase_report",
        "cmo_sale",
        "cmo_sale_discount_total_enhance",
        "cmo_sale_order_revision_enhance",
        "cmo_sale_report",
        "cmo_sale_split_quote2many_order",
        "cmo_stock",
        "cmo_ui",
        "pabi_utils",
    ],
    'pre_init_hook': 'pre_init_hook',
}
