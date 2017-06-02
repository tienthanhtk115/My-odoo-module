# -*- coding: utf-8 -*-
{
    'name': "Black List Customer",

    'summary': """
        Setting allow/reject/warring user create sale order while customer in black list """,

    'description': """
        Setting allow/reject/warring user create sale order while customer in black list
    """,

    'author': "Magestore.com",
    'website': "magestore.com",

    'category': 'Tools',
    'version': '0.1',

    'depends': ['base','sale'],

    'data': [
        'views/res_partner_view.xml',
        'views/account_config_setting.xml',
    ],
    'application': True,
}
