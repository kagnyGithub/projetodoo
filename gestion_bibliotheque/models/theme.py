from odoo import api, fields, models

class BibliothequeTheme(models.Model):

    _name="biblio.theme"
    libelle = fields.Char(string='Libelle')
    