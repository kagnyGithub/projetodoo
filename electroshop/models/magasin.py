from odoo import api, fields, models

class ElectroshopMagasin(models.Model):

    _name="electroshop.magasin"
    nom = fields.Char(string='Nom')
    adresse = fields.Char(string='Adresse')
    telephone = fields.Char(string ='Telephone')
    email = fields.Char(string='Email')
    ville_id = fields.Many2one('electroshop.ville', string='Ville')
