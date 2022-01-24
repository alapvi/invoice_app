# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime
from odoo.exceptions import ValidationError

import logging
_logger = logging.getLogger(__name__)

class InvoiceModel(models.Model):
     _name = 'invoice_app.invoice_model'
     _description = 'Invoice Model'
     _sql_constraints = [ ('invoice_unique_ref','UNIQUE (reference)','Reference must be unique!!'), ]

     reference = fields.Integer(string="Ref",required=True,default=lambda self: self._get_id(),index=True,help="Invoice Reference")
     date = fields.Date(string="Date",required=True,default=datetime.now(),help="Date")
     base = fields.Float(string="Base",compute="_check_base",help="DNI for Client", store=True)
     vat = fields.Selection(string="VAT",selection=[('0','0'),('4','4'),('10','10'),('21','21')], default='21',help="VAT for this invoice")
     total = fields.Float(string="Total",compute="_check_total",help="Total invoice",store=True)
     lines_ids = fields.One2many("invoice_app.line_model","invoice_id",string="Lines")
     client_id = fields.Many2one("invoice_app.client_model", string="Client",required=True)
     state = fields.Selection(string="Status",selection=[('D','Draft'),('C','Confirmed')], default="D")

     def confirmInvoice(self):
          self.ensure_one()
          self._cr.autocommit(False)
          if self.state == "D":
               self.state = "C"
               for rec in self.lines_ids:
                    if rec.quantity <= rec.product_id.stock:
                         rec.product_id.stock -= rec.quantity
                    else:
                         self._cr.rollback()
                         self._cr.autocommit(True)
                         raise ValidationError("There is no Stock of "+rec.product_id.name+"!")          
          self._cr.commit()
          self._cr.autocommit(True)
          return True

     
     def _get_id(self):
          return (self.env['invoice_app.invoice_model'].search([])[-1].id + 1)
          

     @api.depends("lines_ids")
     def _check_base(self):
          sum = 0
          for line in self.lines_ids:
               sum += line.product_id.price*line.quantity
          self.base = sum

     @api.depends("base", "vat")
     def _check_total(self):
          self.total = self.base*int(self.vat)/100.0 + self.base




