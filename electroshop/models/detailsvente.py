from odoo import api, fields, models

class ElectroshopDetailsVentes(models.Model):

    _name="electroshop.detailsvente"
    quantite = fields.Integer(string='Quantite')
