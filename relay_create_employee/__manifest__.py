# -*- coding: utf-8 -*-
{
    'name': "Create User",

    'summary': """
        Create new employee associated with user when created an user.""",

    'description': """
    This module will provides some new actions when you create an User account:
    
    + create new employee with name is same name of user, work_email is same login of user
    + when you deleted an user, associate employee will be deleted
    + when you edit the user, if login changed --> work_email of employee will be changed""",

    'author': "Magestore.com",
    'website': "Magestore.com",

    'category': 'Tools',
    'version': '1.0',

    'depends': ['base', 'hr'],

    'application':True,
}
