# -*- coding : utf-8 -*-

from odoo import models, fields, api, exceptions
from odoo.osv import osv


class SaleOderBlackList(models.Model):
    _name = 'sale.order'
    _inherit = "sale.order"

    @api.model
    def create(self, vals):
        if vals.has_key('partner_id'):
            result = super(SaleOderBlackList, self).create(vals)
            isblacklist = self.env['res.partner'].search([('id', '=', vals.get('partner_id'))]).in_blacklist

            setting = self.env['sale.config.settings'].search([])
            black_list = 0
            for s in setting:
                black_list = s.group_black_list
            if black_list == 0:         # warring
                return result
            else:
                if black_list == 1:    # reject
                    if isblacklist:
                        raise osv.except_osv(('Black list'), ('The customer in black list , go to setting to allow create sale order'))
                else:                  # allow
                    return result

    @api.onchange('partner_id')
    def change_customer(self):
        in_blacklist = self.partner_id.in_blacklist
        setting = self.env['sale.config.settings'].search([])
        group_black_list =0
        for s in setting:
            group_black_list = s.group_black_list
        if group_black_list == 0 or group_black_list == 1:
                if in_blacklist:
                    return {
                    'warning': {
                        'title': " Warring black list",
                        'message': 'The customer in black list , Let\'s sure you want create sale order' ,
                        }
                    }

