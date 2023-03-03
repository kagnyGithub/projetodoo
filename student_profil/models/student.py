from odoo import api, fields, models

class UniversityStudent(models.Model):
    _name="student.security.student"
    f_name = fields.Char('first Name')
    l_name = fields.Char('last Name')
    sexe = fields.Selection([('female','Female'),('male','Male')])
    identity_card = fields.Char('Identity Card')
    address = fields.Text('Address')
    birthday = fields.Date('Birthday')
    registration_day = fields.Date('Registration Day')
    email = fields.Char('Email')
    phone = fields.Char('Phone')
