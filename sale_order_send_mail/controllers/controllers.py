# -*- coding: utf-8 -*-
from odoo import http
import odoo.http as http
from odoo.http import request
import os


# import odoo.addons.web.http as http


class SaleOrderSendMail(http.Controller):
    # _cp_path = '/sale_order_send_mail/sale_order_send_mail/object?id=9&partner_id=45&state=done'

    @http.route('/sale_order_send_mail/done/', auth='public',
                type="http", methods=['GET'])
    def index(self, req, s_action=None, **kw):
        # return request.render("sale_order_send_mail.email_template_edi_sale_custom", {'id': id})
        return "<h3>Thank you for accepting the order!</h3>"
        # print self.httprequest.form["state"]
        # base_url = request.httprequest.base_url
        # bu = unicode(base_url)
        # bu.rsplit("/")
        # # query_string = request.httprequest.query_string
        #
        # rec = request.env['sale.order'].sudo().browse(2)
        # return rec.write({'state': 'done'})

        # self.env['sale.order'].write({'state' : 'done' })
        # return "<h3>Thank you for accepting the order!</h3>"

    @http.route(redirect='/sale_order_send_mail/cancel/', auth='public',
                type="http", methods=['GET'])
    def index(self, req, s_action=None, **kw):
        # self.env['sale.order'].write({'state': 'cancel'})
        return "<h3>You have declined the order!</h3>"


        # @http.route('/sale_order_send_mail/sale_order_send_mail/object?id=9&partner_id=45&state=done', auth='public',
        #             type="http")
        # def index(self, **kw):
        #     return "<h1>Hello, world</h1>"

        # @http.route('/sale_order_send_mail/sale_order_send_mail/object/', auth='public')
        # def list(self, **kw):
        #     return http.request.render('sale_order_send_mail.listing', {
        #         'root': '/sale_order_send_mail/sale_order_send_mail',
        #         'objects': http.request.env['sale_order_send_mail.sale_order_send_mail'].search([]),
        #     })


        # dieu hương den 1 view khac=> sale_order_send_mail.view_id
        #     @http.route('/sale_order_send_mail/sale_order_send_mail/objects/<model("sale_order_send_mail.sale_order_send_mail"):obj>/', auth='public')
        #     def object(self, obj, **kw):
        #         return http.request.render('sale_order_send_mail.object', {
        #             'object': obj
        #         })
