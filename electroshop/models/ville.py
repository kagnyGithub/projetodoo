from odoo import api, fields, models

class ElectroshopVille(models.Model):

    _name="electroshop.ville"
    nom = fields.Char(string='Nom')
