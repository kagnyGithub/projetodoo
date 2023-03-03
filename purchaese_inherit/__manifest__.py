# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Purchase_Inherit',
    'version': '14.1',
    'category': 'Achat ',
    'summary': 'Inherit purchase',
    'description': "",
    'website': 'https://www.odoo.com/page/purchase',
    'depends': ['base',
                'mail','purchase'],
    'data': [
      'views/purchase_inherit_view.xml'
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'qweb': [],
    'license': 'LGPL-3',
}
