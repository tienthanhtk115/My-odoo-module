# -*- coding: utf-8 -*-

from odoo import fields, models, api


class MrpProduction(models.Model):
    _inherit = "mrp.production"

    origin_reference = fields.Many2one('sale.order', string='Source Document',
                                       compute="origin_compute", readonly=True,
                                       help="Reference of the document")

    @api.depends("origin")
    def origin_compute(self):
        for item in self:
            order_id = item.origin
            order_id = order_id.split(":")[0]
            item.origin_reference = item.env['sale.order'].search([('name', '=', order_id)])