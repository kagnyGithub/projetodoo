from odoo import models, fields

class AgenceMarque(models.Model):
    _name='agence.marque'
    _description = 'Les Marques des Véhicules'
    # On met le champ name
    name=fields.Char('Nom de la Marque')
    logo=fields.Binary('Logo')
    vehicules_ids=fields.One2many(
        'agence.vehicule',
        'marque_id',
        string='Véhicules de cette marque'
    )