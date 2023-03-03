from odoo import api, fields, models

class UniversityDepartement(models.Model):
    _name="university.departement"

    name = fields.Char()
    code = fields.Char()
    professor_ids = fields.One2many('university.professor','departement_id')
    subject_ids = fields.One2many('university.subject','departement_id')
    num_prof = fields.Integer(string='Number of professor:', compute='comp_prof')
    num_sub = fields.Integer(string='Number of Subject:', compute='comp_sub')

    def comp_prof(self):
        self.num_prof = len(self.professor_ids)

    def comp_sub(self):
        self.num_sub = len(self.subject_ids)

    @api.onchange('subject_ids')
    def check_number_of_subject(self):
        if len(self.subject_ids)>3:
            return {'warning': {'title': 'warning', 'message': 'The number should than less 3'}}
