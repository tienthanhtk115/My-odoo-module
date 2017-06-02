# -*- coding: utf-8 -*-
{
    'name': "Export calendar events",

    'summary': """
       This module allow user export events in odoo-calendar and inport any drive using google calendar or vcalendar""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Magestore",
    'website': "http://www.magestore.vn",

    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base','calendar'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'wizard/button_export.xml',
        'wizard/export_calendar.xml',
    ],
    # only loaded in demonstration mode
    'qweb': [
        "static/src/xml/web_export_view_template.xml",
    ],
}