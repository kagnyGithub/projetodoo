from odoo import api, fields, models

class LibraryEditor(models.Model):

    _name="library.editor"
    l_name = fields.Char('Nom')
    f_name = fields.Char('Prenom')
    exemplary_ids = fields.One2many('library.exemplary','editor_id')

    def name_get(self):
        result = []
        for editor in self:
            var = '[' + editor.l_name+ ':' + editor.f_name+']'
            result.append((editor.id, var))
        return result