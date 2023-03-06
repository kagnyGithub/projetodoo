{
    'name': 'deposit management System',
    'version': '15.0.1',
    'category': 'system management',
    'summary': 'This is the application for deposit management System',
    'description': "",
    'website': 'https://www.odoo.com/page/deposit.com',
    'depends': ['base', 'contacts','mail'],
    'data': [
        'data/sequence_data.xml',
        'security/ir.model.access.csv',
        'views/wb_bank_view.xml',
        'views/wb_bank_transaction_view.xml'
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'qweb': [],
    'license': 'LGPL-3',
}