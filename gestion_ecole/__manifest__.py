{
    'name': 'Gestion Ecole',
    'version': '15.0.1',
    'category': 'Gestion Ecole',
    'summary': 'Projet de gestion d"une ecole de formation',
    'description': "",
    'website': 'https://www.odoo.com/page/ecole',
    'depends': ['base', 'website','mail'],
    'data': [
        'views/student_views.xml',
        'security/ir.model.access.csv'
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'qweb': [],
    'license': 'LGPL-3',
}