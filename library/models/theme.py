from odoo import api, fields, models

class LibraryTheme(models.Model):

    _name="library.theme"
    wording = fields.Char(string='Libelle')
    book_ids = fields.One2many('library.book','theme_id')
    def name_get(self):
        result = []
        for theme in self:
            var = theme.wording
            result.append((theme.id, var))
        return result