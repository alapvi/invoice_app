# -*- coding: utf-8 -*-

from xml.dom import ValidationErr
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ProductModel(models.Model):
    _name = 'invoice_app.product_model'
    _description = 'Product Model'
    _sql_constraints = [ ('product_unique_name','UNIQUE (name)','Product Name must be unique!!'), ]


    name = fields.Char(string="Name",required=True,index=True,help="Product Name")
    description = fields.Html(string="Description",required=True,help="Description for this product")
    price = fields.Float(string="Price",required=True,default=0,help="Price for this product")
    stock = fields.Integer(string="Stock",required=True,default=1,help="Quantity for this product")

    @api.constrains("price")
    def check_price(self):
        if self.price < 0:
            raise ValidationError("Price must be greater o equal than 0!!")

    @api.constrains("stock")
    def check_stock(self):
        if self.stock < 0:
            raise ValidationError("Stock must be greater o equal than 0!!")