from odoo import api, fields, models
class WbTransactions(models.Model):
    _name = "wb.bank.transactions"
    descrption="Transaction medel"


    name = fields.Many2one("res.partner", string="Custumer", required=True)
    wb_bank_id = fields.Many2one("wb.bank",string="Bank", required=True)
    balance = fields.Float("Balance")
    remark = fields.Char("Remark")
    state = fields.Selection([('draft','Draft'),('done','Done')],string='State',default='draft')

