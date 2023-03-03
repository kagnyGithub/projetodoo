
from odoo import models, fields

class Absence(models.Model):
    _name = 'emploi.absence'

    cours_id = fields.Many2one('emploi.cours')
    etudiant_ids = fields.One2many('emploi.etudiant', 'absence_id')
    description = fields.Char(string='Description')
    present = fields.Boolean(string='Present')
    absent = fields.Boolean(string='Absent')
    motif = fields.Char(string='Motif')

    # @api.depends('etudiant_id')
    # def _compute_nomEtudiant(self, etudiant=None):
    #     for record in self:
    #        record = self.filtered(lambda record: record.etudiant_id == etudiant.firstName )
    #     return record