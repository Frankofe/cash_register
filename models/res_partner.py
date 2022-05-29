from odoo import models,fields

class res_partner(models.Model):
    _inherit="res.partner"

    record = fields.One2many(comodel_name='cash_register.movements', inverse_name='contact')