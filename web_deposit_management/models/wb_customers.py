from odoo import api, fields, models
class WbParner(models.Model):
    _inherit = "res.partner"

    wb_bank_id = fields.Many2one("wb.bank",string="Bank Name")
    balance = fields.Float("Balance")




