from odoo import api, fields, models

class Pateint(models.Model):
    _name="hospital.patient"
    l_name = fields.Char(string='Nom')
    f_name = fields.Char(string='Prenom')
    
    gender = fields.Selection([('male','Male'),('female','Female')],string='Gender')
