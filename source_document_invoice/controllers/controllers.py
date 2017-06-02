# -*- coding: utf-8 -*-
from odoo import http

# class SourceDocument(http.Controller):
#     @http.route('/source_document_invoice/source_document_invoice/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/source_document_invoice/source_document_invoice/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('source_document_invoice.listing', {
#             'root': '/source_document_invoice/source_document_invoice',
#             'objects': http.request.env['source_document_invoice.source_document_invoice'].search([]),
#         })

#     @http.route('/source_document_invoice/source_document_invoice/objects/<model("source_document_invoice.source_document_invoice"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('source_document_invoice.object', {
#             'object': obj
#         })