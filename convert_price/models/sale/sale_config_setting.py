# -*- coding: utf-8 -*-

from odoo import models
from odoo import fields
from odoo import api

class SaleConfiguration(models.TransientModel):
    _inherit = 'sale.config.settings'

    language_option = fields.Selection([
        ('eng', 'English'),
        ('viet', 'Vietnamese')], "Language",
        default='eng',
        required=True)

    @api.multi
    def set_language_option_defaults(self):
        return self.env['ir.values'].sudo().set_default(
            'sale.config.settings', 'language_option', self.language_option)

