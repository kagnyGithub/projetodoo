from datetime import date
from dateutil.relativedelta import relativedelta
from odoo import models, fields, api


class Cours(models.Model):
    _name = 'emploi.cours'

    classe_id = fields.Many2one('emploi.classe')
    professeur_id = fields.Many2one('emploi.professeur')
    matiere_id = fields.Many2one('emploi.matiere')
    absence_ids = fields.One2many('emploi.absence', 'cours_id')
    presence_ids = fields.One2many('emploi.presence', 'cours_id')
    description = fields.Char(string='Description')
    dateDebut = fields.Datetime(string='DateDebut')
    dateFin = fields.Datetime(string='DateFin')
    duree = fields.Char(string='Duree', compute="_compute_duree")

    @api.depends("dateDebut", "dateFin")
    def _compute_duree(self):
        for record in self:
            record.duree = relativedelta(record.dateFin, record.dateDebut).hours

    def action_cours_send(self):
        template = self.env.ref('emploi.email_template_emploi')
        self.env['mail.template'].browse(template.id).sudo().send_mail(self.id ,force_send=True)
        self.env['mail.mail'].sudo().process_email_queue()