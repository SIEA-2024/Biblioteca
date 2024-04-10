{
    'name': 'Biblioteca',
    'application': True,
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv', 
        'views/biblioteca_libro_menus.xml',
        'views/biblioteca_tipo_menus.xml',
        'views/biblioteca_tags_menus.xml',
        'views/menus.xml'
    ],
    'installable': True,
    'license': 'LGPL-3',
}
