from odoo import api, fields, models

class BibliothequeLivre(models.Model):

    _name="biblio.livre"
    titre = fields.Char(string='Titre')
    type_livre = fields.Char(string='Type Livre')
    auteur_ids = fields.Many2many('biblio.auteur', string='Auteurs')
    reserve_ids = fields.One2many('biblio.reserve','livre_id')
    exemplaire_ids = fields.One2many('biblio.exemplaire','livre_id')
    documents = fields.Binary(string='Documents')
    document_name = fields.Char(string='Document name')
    livre_image= fields.Image(string='Upload  image', max_width=100,max_height=100,verified_resolution=False)
