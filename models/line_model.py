# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class LineModel(models.Model):
     _name = 'invoice_app.line_model'
     _description = 'Line Model'

     quantity = fields.Integer(string="Quantity",required=True,default=1,help="Quantity for this line")
     invoice_id = fields.Many2one("invoice_app.invoice_model",string="Invoice",help="Invoice reference")
     product_id =fields.Many2one("invoice_app.product_model",string="Product", help="Product name")

     #
     #@api.constrains("quantity")
     #def _check_quantity(self):
     #     for rec in self:
     #          if rec.quantity <= rec.product_id.stock:
     #               rec.product_id.stock -= rec.quantity
     #               return True
     #          raise ValidationError("There is no Stock!")
     