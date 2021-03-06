# -*- coding: utf-8 -*-
{
    'name': 'Asynchronous Actions',
    'version': '8.0.1.0.0',
    'author': 'Kitti U. (Ecosoft)',
    'license': 'AGPL-3',
    'category': 'Generic Modules',
    'depends': [
        'pabi_utils',
        'purchase_invoice_plan',
        'sale_invoice_plan',
        # 'pabi_procurement',
        # 'pabi_th_tax_report',
        # 'account_subscription_enhanced',
        # 'pabi_hr_salary',
        # 'pabi_budget_plan',
        'account_asset_management',
        'cmo_prq',
    ],
    'data': [
        'cmo_action_asset_compute/security/ir.model.access.csv',
        'cmo_action_asset_compute/cmo_process.xml',
        'cmo_action_asset_compute/xlsx_template/templates.xml',
        'cmo_action_asset_compute/xlsx_template/load_template.xml',
        'cmo_action_asset_compute/xlsx_template/xlsx_template_wizard.xml',
        'cmo_action_asset_compute/cmo_action_asset_compute.xml',
        'cmo_action_asset_compute/reports/report_data.xml',
        'action_sale_create_invoice/process.xml',
        'action_sale_create_invoice/sale_view.xml',
        'action_purchase_create_invoice/process.xml',
        'action_purchase_create_invoice/purchase_view.xml',
    ],
    'installable': True,
    'application': False,
}
