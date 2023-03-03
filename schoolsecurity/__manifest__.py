{
    'name': 'School',
    'version': '15.0.1',
    'category': 'Project Management',
    'summary': 'University',
    'description': "",
    'website': 'https://www.odoo.com/page/school',
    'depends': ['base', 'website','mail'],
    'data': [
         'views/student_views.xml',
        'security/ir.model.access_data.xml'
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'qweb': [],
    'license': 'LGPL-3',
}