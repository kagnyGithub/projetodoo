from odoo import api, fields, models

class ElectroshopStock(models.Model):

    _name="electroshop.stock"
    quantite = fields.Integer(string='Quantite')
    magasin_id = fields.Many2one('electroshop.magasin', string='Magasin')
    article_id = fields.Many2one('electroshop.article', string='Article')