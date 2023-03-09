from odoo import api, fields, models

class LibraryOther(models.Model):

    _name="library.other"
    l_name = fields.Char('Nom')
    f_name= fields.Char('Prenom')
    bibliography = fields.Char(string='Bibliographie')
    book_ids = fields.Many2many('library.book',string='Livres')
    
    def name_get(self):
        result = []
        for other in self:
            var = '[' + other.l_name + ' ' + other.f_name+']'
            result.append((other.id, var))
        return result