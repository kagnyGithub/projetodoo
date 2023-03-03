from odoo import models, fields
class ResPartner(models.Model):
    _inherit = 'res.partner'
    vehicules_autorises_ids= fields.Many2many(
        'agence.vehicule',
        string='Véhicules autorisés à être conduits',
        # relation='library_book_res_partner_rel'
    )