# -*- coding: utf-8 -*-
from odoo import models
from odoo import api
from odoo import fields
from num2words import num2words


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    amount_total_text = fields.Text(string='Total (In text)', store=False, readonly=True,
                                    compute='_compute_amount_total_text')

    @api.depends('amount_total','currency_id')
    def _compute_amount_total_text(self):
        if self.env.user.lang == 'vi_VN':
            for sale_order in self:
                sale_order.amount_total_text = u'BẰNG CHỮ: ' + self.env['convert.to.vn'].number_to_text(
                    sale_order.amount_total) + \
                                               self._get_currency(sale_order.currency_id.id)
        else:
            for sale_order in self:
                sale_order.amount_total_text = u'IN TEXT: ' + num2words(
                    sale_order.amount_total).upper() + self._get_currency(sale_order.currency_id.id)

    @api.model
    def _get_currency(self, currency_id):
        s = self.env['res.currency'].search([('id', '=', currency_id)]).name
        if isinstance(s, basestring):
            name = u" " + s
            return name
        else:
            return u' '
