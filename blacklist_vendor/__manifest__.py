{
    'name': 'Black list vendor',
    'depends': ['base', 'purchase', 'contacts'],
    'summary': """
        Notify while create purchase order in case the vendor in black list""",

    'description': """
        Notify while create purchase order in case the vendor in black list
    """,
    'author': "",
    'website': "",
    'data': [
        'view/vendor_view.xml',
        'view/setting.xml'
    ],
    'application': True,

}
