# -*- coding: utf-8 -*-
# Esto es un diccionario de datos de nuestro Modulo
{
    'name': "openacademy",

    'summary': """
        Libreria para la gestión de Odoo11
        """,

    'description': """
        Creando un primer modulo para Odoo en el que practicaremos las vistas y la Herencia.
    """,

    'author': "Ogaliz",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}