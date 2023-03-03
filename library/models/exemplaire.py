from odoo import api, fields, models

class LibraryExemplary(models.Model):

    _name="library.exemplary"
    date_acquisition  = fields.Date(string='Date Aquisition')
    code_usure = fields.Char(string='Code Usure')
    book_id = fields.Many2one('library.book', string='Livre')
    editor_id = fields.Many2one('library.editor', string='Editeur')
    borrow_ids = fields.One2many('library.borrow', 'exemplary_id')

    def name_get(self):
        result = []
        for ex in self:
            var = '[' + ex.book_id.title + ':' + ex.code_usure+']'
            result.append((ex.id, var))
        return result