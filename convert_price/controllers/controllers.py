# -*- coding: utf-8 -*-
from odoo import http

# class ConvertPrice(http.Controller):
#     @http.route('/convert_price/convert_price/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/convert_price/convert_price/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('convert_price.listing', {
#             'root': '/convert_price/convert_price',
#             'objects': http.request.env['convert_price.convert_price'].search([]),
#         })

#     @http.route('/convert_price/convert_price/objects/<model("convert_price.convert_price"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('convert_price.object', {
#             'object': obj
#         })