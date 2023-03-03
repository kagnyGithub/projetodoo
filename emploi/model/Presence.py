from datetime import date
from dateutil.relativedelta import relativedelta
from odoo import models, fields, api


class Presence(models.Model):
    _name = 'emploi.presence'

    cours_id = fields.Many2one('emploi.cours')
    etudiant_ids = fields.One2many('emploi.etudiant', 'presence_id')
    dateArrive = fields.Datetime(string='DateArrive')
    dateDebut = fields.Datetime(string='DateDebut', compute="_compute_dateD")
    dateFin = fields.Datetime(string='DateFin', compute="_compute_dateF")
    nomMatiere = fields.Char(string='NomMatiere', compute="_compute_nomMatiere")
    motif = fields.Char(string='Motif')
    retard = fields.Char(string='Retard', compute="_compute_retard")

    @api.depends("cours_id")
    def _compute_retard(self):
        for record in self.env['emploi.cours'].search([]):
            dateDebut = record.dateDebut
            for presence in self:
                presence.retard = relativedelta(presence.dateArrive, dateDebut).minutes


    def echo_name(self):
        return "Hello Class"

    def test_list(self):
        return [{"lastName":"Wele",
                 "firstName":"Aliou"},
                {"lastName": "Thiao",
                 "firstName": "Penda"}
                ]

    # @api.depends("etudiant_id")
    # def _compute_prenom(self):
    # for record in self:
    # for eleve in record.env['emploi.etudiant'].sudo().search(['etudiant_id', '=', self.etudiant_id.lastName]):
    # record.prenom = eleve.lastName

    @api.depends("cours_id")
    def _compute_nomMatiere(self):
        for cours in self.env['emploi.cours'].search([]):
            for record in self:
                record.nomMatiere = cours.matiere_id.name

    @api.depends("cours_id")
    def _compute_dateD(self):
        for cours in self.env['emploi.cours'].search([]):
            for record in self:
                record.dateDebut = cours.dateDebut

    @api.depends("cours_id")
    def _compute_dateF(self):
        for cours in self.env['emploi.cours'].search([]):
            for record in self:
                record.dateFin = cours.dateFin
