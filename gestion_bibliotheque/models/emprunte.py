from odoo import api, fields, models

class BibliothequeEmprunte(models.Model):

    _name="biblio.emprunte"
    date_emprute = fields.Date(string='Date Emprunte')
    date_retour = fields.Date(string='Date Retour')
    nbre_renouv = fields.Integer(string='Nombre Renouvellement')
    abonne_id = fields.Many2one('biblio.abonne',string='Abonne')
    exemplaire_id = fields.Many2one('biblio.exemplaire',string='Exemplaire')

