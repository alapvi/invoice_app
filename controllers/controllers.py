# -*- coding: utf-8 -*-
# from odoo import http


# class InvoiceApp(http.Controller):
#     @http.route('/invoice_app/invoice_app/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/invoice_app/invoice_app/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('invoice_app.listing', {
#             'root': '/invoice_app/invoice_app',
#             'objects': http.request.env['invoice_app.invoice_app'].search([]),
#         })

#     @http.route('/invoice_app/invoice_app/objects/<model("invoice_app.invoice_app"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('invoice_app.object', {
#             'object': obj
#         })
