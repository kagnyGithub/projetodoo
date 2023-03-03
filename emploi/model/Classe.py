from odoo import models, fields

class Classe(models.Model):
    _name = 'emploi.classe'

    etudiant_ids = fields.One2many('emploi.etudiant', 'classe_id')
    cours_ids = fields.One2many('emploi.cours', 'classe_id')
    name = fields.Char(string='NomClasse')