from odoo import api, fields, models
import datetime
class LibraryAbonne(models.Model):

    _name="library.abonne"
    code = fields.Char('Numero Carte',readonly=True)
    l_name = fields.Char('Nom')
    f_name = fields.Char('Prenom')
    sex = fields.Selection([('female','Femme'),('male','Homme')])
    address = fields.Text('Adresse')
    date_birth = fields.Date('Date de Naissance')
    date_registration = fields.Date('Date Inscription')
    email = fields.Char('Email')
    phone = fields.Char('Telephone')
    reserve_ids = fields.One2many('library.reserve', 'abonne_id')
    borrow_ids = fields.One2many('library.borrow', 'abonne_id')
    isabonne = fields.Boolean(string='est abonne')
    image = fields.Image(string="Image",max_width=200,max_height=150,verified_resolution=False)


    def send_email_template(self):
        self.env.ref("library.student_email_template").send_mail(self.id,force_send=True)

    def name_get(self):
        result = []
        for abonne in self:
            var = '[' + abonne.l_name + ' ' + abonne.f_name+']'
            result.append((abonne.id, var))
        return result

    def genid(self,nom):
        x = datetime.datetime.now()
        return  x+''+ nom

    @api.model
    def create(self,values):
        values['isabonne']=True
        # m=str(datetime.datetime.now().month)
        # if len(m)<2:
        #     m='0'+m
        # values['cni'] =str(datetime.datetime.now().year)+values['f_name'][0].upper()+values['l_name'][0].upper()+m
        values['code'] = self.env['ir.sequence'].next_by_code("library.abonne")
        rtn = super(LibraryAbonne,self).create(values)
        return rtn

    def write(self,values):
        return super(LibraryAbonne,self).write(values)

    @api.returns('self',lambda value: value.id)
    def copy(self,default={}):
        rtn = super(LibraryAbonne,self).copy(default=default)
        return rtn
    
    def unlink(self):
        return super(LibraryAbonne, self).unlink()