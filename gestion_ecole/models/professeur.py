from odoo import api, fields, models

class EcoleProfesseur(models.Model):

    _name="ecole.professeur"
    cni = fields.Char('Numero Carte')
    nom = fields.Char('Nom')
    prenom = fields.Char('Prenom')
    sexe = fields.Selection([('female','Femme'),('male','Homme')])
    adresse = fields.Text('Address')
    email = fields.Char('Email')
    telephone = fields.Char('Telephone')
    status = fields.Char('Status')
    salaire = fields.Integer('Salaire')