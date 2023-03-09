from odoo import api, fields, models

class LibraryBook(models.Model):

    _name = "library.book"
    title = fields.Char(string='Titre')
    type_book = fields.Char(string='Type Livre')
    other_ids = fields.Many2many('library.other', string='Auteurs')
    reserve_ids = fields.One2many('library.reserve','book_id')
    exemplary_ids = fields.One2many('library.exemplary','book_id')
    theme_id = fields.Many2one('library.theme',string='Theme')
    documents = fields.Binary(string='Documents')
    document_name = fields.Char(string='Document name')
    book_image= fields.Image(string='Upload  image', max_width=200,max_height=200,verified_resolution=False)
    state = fields.Selection([
        ('disponible', 'Disponible'),
        ('rupture', 'En rupture')], string='Status', default='disponible', track_visibility='onchange')

    
    def button_dispo(self):
        for project in self:
            project.state = 'disponible'

    
    def button_rupture(self):
        for project in self:
            project.state = 'rupture'

    def name_get(self):
        result = []
        for book in self:
            var = book.title
            result.append((book.id, var))
        return result