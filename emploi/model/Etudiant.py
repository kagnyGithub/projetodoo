from datetime import date
from dateutil.relativedelta import relativedelta
from odoo import models, fields, api

class Etudiant(models.Model):
    _name = 'emploi.etudiant'

    classe_id = fields.Many2one('emploi.classe')
    absence_id = fields.Many2one('emploi.absence')
    presence_id = fields.Many2one('emploi.presence')
    lastName = fields.Char(string='Prenom')
    firstName = fields.Char(string='Nom')
    phoneNumber = fields.Char(string='Telephone')
    email = fields.Char(string='Email')
    age = fields.Char(string='Age', compute="_compute_age")
    birthday = fields.Date(string='Birthday')
    present = fields.Boolean(string='Present')
    absent = fields.Boolean(string='Absent')

    @api.depends("birthday")
    def _compute_age(self):
        for record in self:
            new_date = date.today()
            day_bith = record.birthday
            record.age = relativedelta(new_date, day_bith).years