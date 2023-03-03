from odoo import api, fields, models

class EcoleEleve(models.Model):

    _name="ecole.eleve"
    cni = fields.Char('Numero Carte')
    nom = fields.Char('Nom')
    prenom = fields.Char('Prenom')
    sexe = fields.Selection([('female','Femme'),('male','Homme')])
    adresse = fields.Text('Address')
    dateNaissance = fields.Date('Date de Naissance')
    dateInscription = fields.Date('Date Inscription')
    email = fields.Char('Email')
    telephone = fields.Char('Telephone')
    nationalite = fields.Char('Nationalite')
    ville = fields.Char('Ville')