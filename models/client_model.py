# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ClientModel(models.Model):
    _name = 'invoice_app.client_model'
    _description = 'Client Model'
    _sql_constraints = [ ('client_unique_dni','UNIQUE (dni)','DNI must be unique!!'), ]

    name = fields.Char(string="Name",required=True,index=True,help="Client Name")
    surname = fields.Char(string="Surname",required=True,index=True,help="Surname")
    dni = fields.Char(string="DNI",size=9,required=True,index=True,help="DNI for Client")
    photo = fields.Binary(string="Photo",help="Photo for this client")
    phone = fields.Char(string="Phone",size=9,help="Phone for Client")
    email = fields.Char(string="Email",required=True,help="Email for Client")
    invoices_ids = fields.One2many("invoice_app.invoice_model","client_id", string="Invoices")


    @api.constrains('dni')
    def validate_dni(self):
        if not self.check_DNI(self.dni):
            raise ValidationError("Error DNI!!!!")

    def check_DNI(self, ndni):
        tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
        dig_ext = "XYZ"
        reemp_dig_ext = {'X':'0', 'Y':'1', 'Z':'2'}
        numeros = "1234567890"
        dni = ndni.upper()
        if len(dni) == 9:
            dig_control = dni[8]
            dni = dni[:8]
            if dni[0] in dig_ext:
                dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
            return len(dni) == len([n for n in dni if n in numeros]) \
                and tabla[int(dni)%23] == dig_control
        return False


    @api.constrains('email')
    def validate_dni(self):
        if "@" and "." not in self.email:
            raise ValidationError("Email format error!!!!")
