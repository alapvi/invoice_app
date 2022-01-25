# -*- coding: utf-8 -*-
{
    'name': "invoice_app",

    'summary': """
        This is an app for invoices""",

    'description': """
        You can manage any product and do the invoice process
    """,

    'author': "Alberto Aparicio",
    'website': "http://www.aaparicio.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/product_view.xml',
        'views/client_view.xml',
        'views/invoice_view.xml',
        'views/line_view.xml',        
        'views/templates.xml',
        'data/data.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'installable': True,
}
