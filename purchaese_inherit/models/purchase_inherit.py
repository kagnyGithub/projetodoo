from odoo import api, fields, models

class PurchaseInherit(models.Model):
    _inherit ="purchase.order"
    nature = fields.Selection([('national','National'),('international','International')])