from odoo import fields, models


class website_config_settings(models.TransientModel):
    _inherit = 'website.config.settings'

    recaptcha_site_key = fields.Char(related="website_id.recaptcha_site_key",
                                     string='reCAPTCHA site Key')
    recaptcha_private_key = fields.Char(related="website_id.recaptcha_private_key",
                                        string='reCAPTCHA Private Key')


