# -*- coding: utf-8 -*-

{
    'name': 'Download contact',
    'category': 'Web',
    'author': 'Kriz - Odoo dev , \
            Magestore VN',
    'website': 'http://www.magestore.com',
    'summary': 'Export Contact',
    'description': """This module allow user to export contact & employee to vCard file and download directly""",
    'depends': [
        'web','hr','base',
    ],
    "data": [
        'views/export_vcard_view.xml',
        'views/inherit_employee_treeview.xml',
        'views/inherit_contact_treeview.xml',
        'wizard/export_contact_vcard.xml',
        'wizard/export_employee_vcard.xml',
        'wizard/button_export_in_contact_detail_view.xml',
        'wizard/button_export_in_employee_detail_view.xml',
    ],
    'qweb': [
        "static/src/xml/export_vcard_view_template.xml",
    ],
    'application':True,
}
