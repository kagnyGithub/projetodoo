from odoo import api, fields, models

class BibliothequeExemplaire(models.Model):

    _name="biblio.exemplaire"
    date_aquition = fields.Date(string='Date Aquisition')
    code_usure = fields.Char(string='Code Usure')
    livre_id = fields.Many2one('biblio.livre', string='Livre')
    editeur_id = fields.Many2one('biblio.editeur', string='Editeur')
    emprunte_ids = fields.One2many('biblio.emprunte', 'exemplaire_id')
