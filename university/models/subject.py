from odoo import api, fields, models

class UniversitySubject(models.Model):
    _name="university.subject"

    name = fields.Char()
    code = fields.Char()
    departement_id = fields.Many2one('university.departement', string='Departement')
    professor_ids = fields.Many2many('university.professor',string='List of Professor')