{
    'name': 'Academy TDSI',
    'version': '15.0.1',
    'category': 'Academie',
    'summary': 'Academie',
    'description': "",
    'website': 'https://www.odoo.com/page/academy',
    'depends': ['base', 'website'],
    'data': [
         'security/ir.model.access.csv',
         'views/templates.xml'
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'qweb': [],
    'license': 'LGPL-3',
}