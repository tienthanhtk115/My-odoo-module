# -*- coding: utf-8 -*-

from odoo import _
from odoo import api
from odoo import exceptions
from odoo import models


class PurchaseOrder(models.Model):
    _name = "purchase.order"

    _inherit = "purchase.order"

    @api.onchange('partner_id')
    def _on_change_partner_id(self):
        print 'black list:', self.partner_id.in_blacklist
        option = self._get_warning_option()
        if option == 'warning' and self.partner_id.in_blacklist:  # show warning
            return {'warning': {
                'title': _('Warning'),
                'message': _('You are creating purchase order in case the vendor in black list')
            }
            }
        if option == 'eject' and self.partner_id.in_blacklist:
            return {'warning': {
                'title': _('Warning'),
                'message': _('You can not create purchase order in case the vendor in black list')
            }
            }

    # Notify while create purchase order in case the vendor in black list

    @api.model
    def create(self, vals):
        vendor_id = vals['partner_id']
        vendor = self.env['res.partner'].search([('id', '=', vendor_id)])
        print 'vendor in black list::', vendor.in_blacklist
        # check option when create purchase whie vendor in black list:
        # get the lastest record has been modify
        option = self._get_warning_option()
        if option == 'no_warning':  # create purcharse, do not show warning
            return super(PurchaseOrder, self).create(vals)
        elif option == 'warning':  # show warning
            return super(PurchaseOrder, self).create(vals)
        elif option == 'eject':  # eject create purchase:
            raise exceptions.UserError(_("You can not create purchase order in case the vendor in black list"))
    @api.model
    def _get_warning_option(self):
        #get warning option from data base
        #comment thu 2
        setting = self.env['purchase.config.settings'].search([])
        if len(setting)==0:
            return 'warning'
        else:
            return setting[-1].warning_option

