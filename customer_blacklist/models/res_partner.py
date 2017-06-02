# -*- coding : utf-8 -*-

from odoo import models, fields


class ResPartner(models.Model):
    _name = "res.partner"
    _inherit = ["res.partner"]
    in_blacklist = fields.Boolean("In black list")
