# -*- coding: utf-8 -*-
{
    'name': "Source document for invoice",
    'summary': """
        Add link source document for invoice """,

    'description': """
       Add link source document for invoice
    """,
    'author': "Magestore.com",
    'website': "magestore.com",
    'category': 'Tools',
    'version': '0.1',
    'depends': ['base','account','sale'],

    'data': [
        'views/account_invoice_view.xml',
    ],
    'application': True ,
}
