{
    'name': 'University',
    'version': '15.0.1',
    'category': 'Project Management',
    'summary': 'University',
    'description': "",
    'website': 'https://www.odoo.com/page/unversity',
    'depends': ['base', 'website','mail'],
    'data': [
         'views/student_views.xml',
         'views/professor_views.xml',
         'views/departement_views.xml',
         'views/subject_views.xml',
         'views/classroom_views.xml',
         'data/mail_template.xml',
         'security/ir.model.access.csv'

    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'qweb': [],
    'license': 'LGPL-3',
}