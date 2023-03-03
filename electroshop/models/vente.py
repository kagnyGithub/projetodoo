from odoo import api, fields, models

class ElectroshopVente(models.Model):

    _name="electroshop.vente"
    date_v = fields.Date(string='Date Vente')
    montant = fields.Integer(string='Montant')
    client_id = fields.Many2one('electroshop.client', string='Client')
    magasin_id = fields.Many2one('electroshop.magasin', string='Magasin')

