# -*- coding:utf-8 -*-
from odoo import fields, models, api


class Setting(models.TransientModel):
    _inherit = 'purchase.config.settings'

    warning_option = fields.Selection([('no_warning', 'No warning'),
                                       ('warning', 'Warning'),
                                       ('eject', 'Eject create purchase')],
                                      required=True,
                                      default='warning',
                                      string="Notify:")


    @api.multi
    def set_warning_option_defaults(self):
        return self.env['ir.values'].sudo().set_default(
            'purchase.config.settings', 'warning_option', self.warning_option)

