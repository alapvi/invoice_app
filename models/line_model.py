# -*- coding: utf-8 -*-

from odoo import models, fields, api


class LineModel(models.Model):
     _name = 'invoice_app.line_model'
     _description = 'Line Model'

     quantity = fields.Integer(string="Quantity",required=True,default=1,help="Quantity for this line")
     invoice_id = fields.Many2one("invoice_app.invoice_model",string="Invoice",help="Invoice reference")
     product_id =fields.Many2one("invoice_app.product_model",string="Product", help="Product name")