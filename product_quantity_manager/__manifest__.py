# -*- coding: utf-8 -*-
{
    'name': "Products quantity manager",

    'summary': """
        Module for helping quantity of product. If quantity of product = 0, display 0 in red color and warning user cannot sell this product
        """,

    'description': """
        Module for helping quantity of product. If quantity of product = 0, display 0 in red color and warning user cannot sell this product
    """,

    'author': "Magestore",
    'website': "http://www.Magestore.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'point_of_sale'],

    # always loaded
    'data': [
        'views/asset_inherit.xml',
    ],
    'application': True,
    'qweb': ['static/src/xml/pos.xml']

}
