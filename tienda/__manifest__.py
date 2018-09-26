# -*- coding: utf-8 -*-
{
    'name': "tienda",

    'summary': """
       Se puede registrar productos y clientes""",

    'description': """
        Registro de categorias de productos
    """,

    'author': "Das Glogal",
    'website': "http://www.dasglobalcorp.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'ventas',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/views_usuario.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}