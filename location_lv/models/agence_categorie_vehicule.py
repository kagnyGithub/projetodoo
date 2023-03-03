from odoo import models, fields, api
from odoo.exceptions import ValidationError

class AgenceCategVehicule(models.Model):

    _name = 'agence.categorie.vehicule'
    _description = 'Représentation des catégrories des véhicules'
    _parent_store = True
    _parent_name = 'parent_id' # optional if field is 'parent_id'
    parent_path = fields.Char(index=True)
    name = fields.Char('Catégorie')

    parent_id = fields.Many2one(
        'agence.categorie.vehicule',
        ondelete='restrict',
        string='Catégorie Mère',
        Index=True
    )
    child_ids = fields.One2many(
        'agence.categorie.vehicule',
        'parent_id',
        ondelete='restrict',
        string='Sous-Catégorie',
        Index=True
    )
    @api.constrains('parent_id')
    def _check_hierarchy(self):
            if not self._check_recursion():
                raise models.ValidationError('Error! You cannot create recursive categories.')