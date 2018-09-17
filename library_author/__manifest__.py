# -*- coding: utf-8 -*-
{
    'name': "Library Author",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Add author field from Library Managment
    """,

    'author': "Jorge Fuentes",
    'website': "http://www.dasglobalcorp.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Library',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['library'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/author_view.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
    'application': True
}