# -*- coding: utf-8 -*-

from odoo import fields, models, api


class StockPicking(models.Model):
    _inherit = "stock.picking"
    origin_reference_in = fields.Many2one('purchase.order', string='Source Document',
                                          compute="origin_compute", readonly=True,
                                          help="Reference of the document")
    origin_reference_out = fields.Many2one('sale.order', string='Source Document',
                                           compute="origin_compute", readonly=True,
                                           help="Reference of the document")

    @api.depends("origin")
    def origin_compute(self):
        for item in self:
            if item.origin:
                order_id = item.origin
                item.origin_reference_in = item.env['purchase.order'].search([('name', '=', order_id)])
                item.origin_reference_out = item.env['sale.order'].search([('name', '=', order_id)])
