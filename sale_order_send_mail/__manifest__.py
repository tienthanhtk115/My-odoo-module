# -*- coding: utf-8 -*-
{
    'name': "sale_order_send_mail",

    'author': "evan@trueplus.vn",

    # 'website': "http://www.yourcompany.com",


    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'mail'],

    # always loaded
    'data': [
        'data/email_template_edi_sale_custom.xml'
        # 'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
}