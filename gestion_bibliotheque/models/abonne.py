from odoo import api, fields, models

class BibliothequeAbonne(models.Model):

    _name="biblio.abonne"
    cni = fields.Char('Numero Carte')
    nom = fields.Char('Nom')
    prenom = fields.Char('Prenom')
    sexe = fields.Selection([('female','Femme'),('male','Homme')])
    adresse = fields.Text('Address')
    dateNaissance = fields.Date('Date de Naissance')
    dateInscription = fields.Date('Date Inscription')
    email = fields.Char('Email')
    telephone = fields.Char('Telephone')
    reserve_ids = fields.One2many('biblio.reserve', 'abonne_id')
    emprunte_ids = fields.One2many('biblio.emprunte', 'abonne_id')
    isabonne = fields.Boolean(string='est abonne')
    image = fields.Image(string="Image")


    def send_email_template(self):
        self.env.ref("web_email_templaite.student_email_template").send_mail(self.id,force_send=True)

    def name_get(self):
        result = []
        for abonne in self:
            var = '[' + abonne.nom + ']' + ' ' + abonne.prenom+']'
            result.append((abonne.id, var))
        return result

    @api.model
    def create(self,values):
        values['isabonne']=True
        rtn = super(BibliothequeAbonne,self).create(values)
        return rtn

    def write(self,values):
        return super(BibliothequeAbonne,self).write(values)

    @api.returns('self',lambda value: value.id)
    def copy(self,default={}):
        rtn = super(BibliothequeAbonne,self).copy(default=default)
        return rtn
    
    def unlink(self):
        return super(BibliothequeAbonne, self).unlink()