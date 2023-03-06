from odoo import api, fields, models

class WbUser(models.Model):
    _inherit = "res.users"
    #wb_bank_id = fields.Many2one("wb.bank", string="Bank Name")