from odoo import api, fields, models
class WbBank(models.Model):
    _name = "wb.bank"
    descrption="Bank medel"
    name = fields.Char("Bank Name",required=True)
    code = fields.Char("Code",default="/",required=True)
    balance = fields.Float("Balance")
    partner_id = fields.Many2one("res.partner",string="Address")

    @api.model
    def create(self,values):
        values['code'] = self.env['ir.sequence'].next_by_code("wb.bank")
        return super(WbBank,self).create(values)

    _sql_constraints = [
        ('unique_bank_name', 'UNIQUE(name)','Please provide unique bank name'),
    ]