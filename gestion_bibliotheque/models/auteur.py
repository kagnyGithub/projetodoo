from odoo import api, fields, models

class BibliothequeAuteur(models.Model):

    _name="biblio.auteur"
    nom = fields.Char('Nom')
    prenom = fields.Char('Prenom')
    bibliographie = fields.Char(string='Bibliographie')
    livre_ids = fields.Many2many('biblio.livre',string='Livres')
