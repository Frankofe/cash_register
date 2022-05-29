from odoo import models, fields, api
from odoo.exceptions import ValidationError

class movements(models.Model):
    _name = 'cash_register.movements'
    _descripcion='Register in a history the movements in the cash register'    

    type= fields.Selection(string='Movement type', selection=[('i','Entry'),('e','Egress')],required=True)
    amount=fields.Float(string='Amount', required=True)
    balance=fields.Float(string='Balance',help='Current balance', compute='_balance', required=True)
    contact=fields.Many2one('res.partner', required=True)

    @api.depends('balance','amount','type')
    def _balance(self):
        for record in self:
          balance = 0

          movements = self.search([('id', '<=', record.id)])
          for movement in movements:
            if movement.type == 'i':
                record.balance = record.balance+movement.amount
            else:
                record.balance = record.balance-movement.amount
    
    @api.constrains('amount')
    def _constrains_amount(self):
      domain = [('id','!=', self.id)]
      record=self.search(domain, order='id desc', limit=1)
      if record.balance < self.amount and self.type == 'e':
        raise ValidationError("Negative balance is not allowed.")