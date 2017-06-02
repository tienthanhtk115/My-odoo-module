from odoo import models
from odoo import api
from odoo import fields


class vendor(models.Model):
    _name = 'res.partner'

    _inherit = ['res.partner']
    in_blacklist = fields.Boolean(string='In black list?',default=False)


