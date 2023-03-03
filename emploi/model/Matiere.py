from odoo import models, fields


class Matiere(models.Model):
    _name = 'emploi.matiere'

    cours_ids = fields.One2many('emploi.cours','matiere_id')
    name = fields.Char(string='NomMatiere')
    description = fields.Char(string='Description')
