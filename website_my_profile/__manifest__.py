# -*- coding: utf-8 -*-
{
    'name': "My Profiles Website",

    'summary': """
        Create Change Password button and change some properties of My Account page.""",

    'description': """
        This module will adds some property for /my/account page and /web/signup page:
        
        + Add Change Password button to /my/account page: allow user change password directly,
        don't redirect to /web/reset_password
        
        + Add Change Login button to /my/account page: allow user change login name (must input
        current password)
        
        + Add and delete properties of /my/account page:
        
            + Delete Company Name and Zip / Postal Code properties
            + Add Login, Gender, Active and Birthday properties

        + Don't allow access to login, signup and reset_password page if user current loged in""",

    'author': "magestore.com",
    'website': "magestore.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Tools',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base',
                'website',
                'website_portal',
                'auth_signup',
                'mail',
                'fetchmail',
                'hr'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'data/data.xml',
    ],
    'application': True,
}
