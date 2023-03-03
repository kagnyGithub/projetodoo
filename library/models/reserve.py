from odoo import api, fields, models

class LibraryReserve(models.Model):

    _name="library.reserve"
    date_reserve = fields.Date(string='Date Reservation')
    book_id = fields.Many2one('library.book',string='Livre')
    abonne_id = fields.Many2one('library.abonne',string='Abonne')

