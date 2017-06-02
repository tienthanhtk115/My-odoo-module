# -*- coding: utf-8 -*-

{
    'name': 'Partner External Maps',
    'version': '10.0.1.0.0',
    'category': 'Extra Tools',
    'summary': 'Add Map and Map Routing buttons on partner form to '
               'open GMaps, OSM, Bing and others',
    'author': '',
    'website': 'http://www.odoo.com',
    'depends': ['base'],
    'data': [
        'views/res_partner_view.xml',
        'views/map_website_view.xml',
        'data/map_website_data.xml',
        'views/res_users_view.xml',
        'security/ir.model.access.csv',
    ],
    'post_init_hook': 'set_default_map_settings',
    'installable': True,
}
