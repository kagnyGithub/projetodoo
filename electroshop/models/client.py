from odoo import api, fields, models

class ElectroshopClient(models.Model):

    _name="electroshop.client"
    nom = fields.Char(string='Nom')
    adresse = fields.Char(string='Adresse')
    telephone = fields.Char(string='Telephone')
    fidelite = fields.Integer(string='Fidelite')
    
