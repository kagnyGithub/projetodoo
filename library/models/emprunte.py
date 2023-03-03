from odoo import api, fields, models
from datetime import datetime
from datetime import timedelta
from datetime import date
from dateutil.relativedelta import relativedelta

class LibraryEmprunte(models.Model):

    _name="library.borrow"
    date_borrow = fields.Date(string='Date Emprunt', default=lambda self: date.today())
    date_return = fields.Date(string='Date Retour', compute='_compute_date_return',readonly=True)
    nbre_renew = fields.Integer(string='Nombre Renouvellement')
    nbre_jour = fields.Integer(string='Nbre jour restant',compute='_compute_nbrjour')
    abonne_id = fields.Many2one('library.abonne',string='Abonne')
    exemplary_id = fields.Many2one('library.exemplary',string='Exemplaire')

    def name_get(self):
        result = []
        for borrow in self:
            var = '[' + borrow.abonne_id.cni+ ' ' + borrow.exemplary_id.code_usure+']'
            result.append((borrow.id, var))
        return result

    @api.depends('date_borrow')
    def _compute_date_return(self):
        for record in self:
            if record.date_borrow:
                record.date_return = fields.Date.from_string(record.date_borrow) + timedelta(days=15)

    @api.depends("date_return")
    def _compute_nbrjour(self):
        for record in self:
            new_date = date.today()
            today = record.date_return
            record.nbre_jour = relativedelta(today,new_date).days