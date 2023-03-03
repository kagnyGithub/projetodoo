from odoo import api, fields, models

class ElectroshopArticle(models.Model):

    _name="electroshop.article"
    libelle = fields.Char(string='Libelle')
    pu = fields.Integer(string='PU')
    typearticle_id = fields.Many2one('electroshop.typearticle', string='Type Article')