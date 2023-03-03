from odoo import models, fields


class Professeur(models.Model):
    _name = 'emploi.professeur'

    cours_ids = fields.One2many('emploi.cours', 'professeur_id')
    lastName = fields.Char(string='Prenom')
    firstName = fields.Char(string='Nom')
    phoneNumber = fields.Char(string='Telephone')
    email = fields.Char(string='Email')
