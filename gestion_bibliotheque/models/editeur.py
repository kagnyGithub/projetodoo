from odoo import api, fields, models

class BibliothequeEditeur(models.Model):

    _name="biblio.editeur"
    nom = fields.Char('Nom')
    prenom = fields.Char('Prenom')
    exemplaire_ids = fields.One2many('biblio.exemplaire','editeur_id')
