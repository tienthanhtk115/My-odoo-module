__author__ = 'evan@trueplus.vn'

from odoo import models, fields, api, exceptions, _
from datetime import timedelta
from odoo.exceptions import UserError, ValidationError
import os


class SaleOrderSendMail(models.Model):
    _inherit = 'sale.order'

    @api.model
    def action_quotation_send(self, vals):

        # self.ensure_one()
        ir_model_data = self.env['ir.model.data']
        try:
            template_id = ir_model_data.get_object_reference('sale_order_send_mail', 'email_template_edi_sale_custom')[
                1]
        except ValueError:
            template_id = False
        try:
            compose_form_id = ir_model_data.get_object_reference('mail', 'email_compose_message_wizard_form')[1]
        except ValueError:
            compose_form_id = False
        ctx = dict()
        ctx.update({
            'default_model': 'sale.order',
            # 'default_res_id': self.ids[0],
            'default_use_template': bool(template_id),
            'default_template_id': template_id,
            'default_composition_mode': 'comment',
            'mark_so_as_sent': True,
            'custom_layout': "sale.mail_template_data_notification_email_sale_order"
        })
        return {
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'mail.compose.message',
            'views': [(compose_form_id, 'form')],
            'view_id': compose_form_id,
            'target': 'new',
            'context': ctx,
        }

        # return super(SaleOrderSendMail, self).action_quotation_send()

