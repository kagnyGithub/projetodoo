from odoo import api, fields, models

class BibliothequeEmprunte(models.Model):

    _name="biblio.reserve"
    date_reserve = fields.Date(string='Date Reservation')
    livre_id = fields.Many2one('biblio.livre',string='Livre')
    abonne_id = fields.Many2one('biblio.abonne',string='Abonne')
