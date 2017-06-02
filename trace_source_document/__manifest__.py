# -*- coding: utf-8 -*-
{
    'name': "Trace source document",

    'summary': """
        Add link source document""",

    'description': """
        Add link source document
    """,

    'author': "Magestore.com",
    'website': "magestore.com",


    'category': 'Tools',
    'version': '0.1',

    'depends': ['base', 'account', 'sale', 'stock', 'purchase', 'mrp'],

    'data': [
        'views/account_invoice_view.xml',
        'views/stock_picking_view.xml',
        'views/mrp_production_view.xml',
    ],
    'application': True,
}