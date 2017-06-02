# -*- coding : utf-8 -*-

from odoo import fields, models, api


class AccountInvoice(models.Model):
    _inherit = "account.invoice"
    origin_reference = fields.Many2one('sale.order', string='Source Document',
                                       compute="origin_compute", readonly=True)

    @api.depends("origin")
    def origin_compute(self):
        for item in self:
            order_id = item.origin
            item.origin_reference = item.env['sale.order'].search([('name', '=', order_id)])
