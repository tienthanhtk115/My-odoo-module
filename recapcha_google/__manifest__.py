# -*- coding: utf-8 -*-
{
    'name': "Re_captcha google",

    'summary': """
        This modules allows you to integrate Google reCAPTCHA v2.0 to require captcha while login, register, forget password your website """,

    'description': """
       This modules allows you to integrate Google reCAPTCHA v2.0 to require captcha while login, register, forget password your website
    """,

    'author': "Magestore.com",
    'website': "http://www.magestore.com",

    'category': 'Tools',
    'version': '0.1',

    'depends': ['base','website','auth_oauth'],

    'data': [
        'views/website_view.xml',
        'views/config_setting_view.xml',
        'views/website_login_view.xml',
    ],

    'application': True,
}