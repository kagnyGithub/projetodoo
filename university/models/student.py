from odoo import api, fields, models

class UniversityStudent(models.Model):
    _name="university.student"
    f_name = fields.Char('first Name')
    l_name = fields.Char('last Name')
    sexe = fields.Selection([('female','Female'),('male','Male')])
    identity_card = fields.Char('Identity Card')
    address = fields.Text('Address')
    birthday = fields.Date('Birthday')
    registration_day = fields.Date('Registration Day')
    email = fields.Char('Email')
    phone = fields.Char('Phone')
    classroom_id = fields.Many2one('university.classroom', string='Classroum')
    professors_ids = fields.Many2many(related='classroom_id.professor_ids')
    state = fields.Selection([('l1','licence 1'),('l2','licence 2'),('l3','licence 3'),('finished','Finished')])
    sequence = fields.Char('sequnce')
    student_img = fields.Image(string='Image')

    # def name_get(self):
    #    result=[]
    #    for student in self:
    #        var = '[AA'+student.classroom_id.name+']'+' '+student.f_name+' '+student.l_name
    #        result.append((student.id,var))
    #    return result

    def next_level(self):
        if self.state =='l1':
            return self.write({'state':'l2'})
        elif self.state =='l2':
            return self.write({'state':'l3'})
        elif self.state =='l3':
            return self.write({'state':'finished'})
        elif self.state =='finished':
            return {'warning':{'title':'finished','message':'this student have finished'}}



    def send_mail(self):
        self.ensure_one()
        template_id = self.env.ref('university.email_template_student').id
        ctx ={
            'default_model' : 'university.student',
            'default_res_id':self.id,
            'default_use_template': bool(template_id),
            'default_template_id': template_id,
            'default_composition_mode': 'comment',
            'email_to': self.email
        }
        return {
            'type':'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'mail.compose.message',
            'target': 'new',
            'contex': ctx
        }

