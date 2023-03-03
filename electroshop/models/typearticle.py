from odoo import api, fields, models

class ElectroshopTypeArticle(models.Model):

    _name="electroshop.typearticle"
    libelle = fields.Char(string='Libelle')