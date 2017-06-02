# -*- coding: utf-8 -*-
import base64
import cStringIO
import contextlib
import csv

from odoo import api, fields, models


class DownloadContact(models.Model):
    _inherit = 'res.partner'

    file_name = fields.Char()
    data = fields.Binary(string="File", readonly=True)

    @api.multi
    def download(self):
        if self.id:
            with contextlib.closing(cStringIO.StringIO()) as buf:
                writer = csv.writer(buf, delimiter=":", quotechar='"')
                writer.writerow(("BEGIN", "VCARD"))
                writer.writerow(("VERSION", "3.0"))
                writer.writerow(("N", self.name.encode('utf8') if self.name else ''))
                writer.writerow(("FN", self.name.encode('utf8') if self.name else ''))
                writer.writerow(("TEL;TYPE=CELL", self.phone if self.phone else ''))
                writer.writerow(("TEL;TYPE=WORK", self.mobile.encode('utf8') if self.mobile else ''))
                writer.writerow(("EMAIL;TYPE=WORK", self.email if self.email else ''))
                writer.writerow(
                    ("ORG;CHARSET=UTF-8", self.parent_id.name.encode('utf8') if self.parent_id.name else ''))
                writer.writerow(("TITLE", self.title.name if self.title.name else ''))
                writer.writerow(("END", "VCARD"))

                out = base64.encodestring(buf.getvalue())
            self.write({
                'data': out,
                'file_name': 'contact_info.vcf'
            })
        compose_form = self.env.ref('Export_Vcard.wizard_export_contact')
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'res.partner',
            'view_mode': 'form',
            'view_type': 'form',
            'res_id': self.id,
            'views': [(compose_form.id, 'form')],
            'view_id': compose_form.id,
            'target': 'new',
        }
