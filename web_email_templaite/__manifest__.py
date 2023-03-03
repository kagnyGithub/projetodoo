{
    'name': 'Gestion Email',
    'version': '15.0.1',
    'category': 'Gestion Email',
    'summary': 'Email gestion',
    'description': "",
    'website': 'https://www.odoo.com/page/email',
    'depends': ['base', 'website','mail'],
    'data': [
        'report/data/email_templaite.xml'
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'qweb': [],
    'license': 'LGPL-3',
}