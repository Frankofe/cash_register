from email.policy import default
from time import strftime
from odoo import models, fields, api
from datetime import *
# from odoo.exceptions import *
import logging
logger = logging.getLogger(__name__)



class movements(models.Model):
    _name = 'cash_register.movements'
    _descripcion='Register in a history the movements in the cash register'
    _order='create_date desc'
    

    type= fields.Selection(string='Movement type', selection=[('i','Entry'),('e','Egress')],required=True)
    amount=fields.Float(string='Amount', required=True)
    balance=fields.Float(string='Balance',help='Current balance', compute='_balance', required=True)
    contact=fields.Many2one('res.partner', required=True)

    @api.onchange('balance','amount','type', 'id')
    def _balance(self):
        for record in self:
          balance = 0

          movements = self.search([('id', '<=', record.id)])
          for movement in movements:
            if movement.type == 'i':
                record.balance = record.balance+movement.amount
            else:
                record.balance = record.balance-movement.amount