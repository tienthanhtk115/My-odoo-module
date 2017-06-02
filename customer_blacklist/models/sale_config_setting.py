# -*- coding : utf-8 -*-

from odoo import models, fields, api
from odoo.osv import osv


class SaleConfiguration(models.TransientModel):
    _name = 'sale.config.settings'
    _inherit = 'sale.config.settings'
    group_black_list = fields.Selection([
        (0,'Warring customer is in blacklist'),
        (1,'Prevent create sale order while customer is in blacklist'),
        (2,'Allow create sale order while customer is in blacklist')], "BackList setting")

    @api.multi
    def set_blacklist_defaults(self):
        return self.env['ir.values'].sudo().set_default(
            'sale.config.settings', 'group_black_list', self.group_black_list)
