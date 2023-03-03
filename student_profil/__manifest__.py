{
    'name': 'Student security',
    'version': '15.0.1',
    'category': 'Project Management',
    'summary': 'University security',
    'description': "",
    'website': 'https://www.odoo.com/page/unversity',
    'depends': ['base', 'website','mail'],
    'data': [
         'views/student_views.xml',
         'security/ir.model.access.xml'

    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'qweb': [],
    'license': 'LGPL-3',
}