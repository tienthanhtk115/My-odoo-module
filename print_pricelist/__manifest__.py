# -*- coding: utf-8 -*-
{
    'name': "Print Pricelist",

    'summary': """
        Printing pricelist from product""",

    'description': """
        Printing pricelist from product
    """,

    'author': "",
    'website': "",

    'category': 'Tools',
    'version': '0.1',

    'depends': ['base','product'],

    # always loaded
    'data': [
        'views/report_item.xml',
        'views/report_template.xml'
    ],
    'application': True,
}
