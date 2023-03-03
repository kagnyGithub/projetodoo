from odoo import api, fields, models

class UniversityClassroom(models.Model):
    _name = "university.classroom"
    _inherit = "mail.thread"
    name = fields.Char()
    code = fields.Char()
    student_ids = fields.One2many('university.student', 'classroom_id')
    professor_ids = fields.Many2many('university.professor', string='List of professor')