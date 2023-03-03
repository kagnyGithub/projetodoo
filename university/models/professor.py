from odoo import api, fields, models

class UniversityProfessor(models.Model):
    _name="university.professor"
    f_name = fields.Char('first Name')
    l_name = fields.Char('last Name')
    sexe = fields.Selection([('female','Female'),('male','Male')])
    identity_card = fields.Char('Identity Card')
    address = fields.Text('Address')
    birthday = fields.Date('Birthday')
    active = fields.Boolean("")
    start_day = fields.Date('Start Day')
    email = fields.Char('Email')
    phone = fields.Char('Phone')
    departement_id = fields.Many2one('university.departement',string='Departement')
    classroom_ids = fields.Many2many('university.classroom', string='List of classroom')
    subject_ids = fields.Many2many('university.subject', string='List of Subject')
    def name_get(self):
       result=[]
       for prof in self:
           var = prof.f_name
           result.append((prof.id,var))
       return result

