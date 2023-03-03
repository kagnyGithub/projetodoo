# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Emploi',
    'version': '14.1',
    'category': 'TDSI',
    'summary': 'Emploi',
    'description': "",
    'website': 'https://www.odoo.com/page/monemploi',
    'depends': ['base',
                'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/Etudiant_View.xml',
        'views/Absence_View.xml',
        'views/Classe_View.xml',
        'views/Cours_View.xml',
        'views/Matiere_View.xml',
        'views/Presence_View.xml',
        'views/Professeur_View.xml',
        'report/emploi_templates.xml',
        'report/emploi_report.xml',
        'model/data/template_mail.xml'
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'qweb': [],
    'license': 'LGPL-3',
}
