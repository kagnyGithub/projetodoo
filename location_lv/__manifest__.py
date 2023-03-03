# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'agence location automobile',
    'version': '1.6',
    'category': 'Agence',
    'sequence': 15,
    'summary': 'agence automobile de kagny',
    'description': "",
    'website': 'https://www.odoo.com/app/',
    'depends': [
        'base_setup',

    ],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/agence_vehicule.xml',
        'views/agence_marque.xml',
        'views/agence_conducteur.xml',
        'views/agence_categorie_vehicule.xml'
    ],
    'demo': [

    ],
    'application': True,
    'installable': True,
    'auto_install': False,
    'sequence': 1,

    'license': 'LGPL-3',
}
