# -*- coding: utf-8 -*-
import base64
import cStringIO
import contextlib
import csv

from odoo import api, fields, models


class ExportEmployee(models.Model):
    _inherit = 'hr.employee'

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
                writer.writerow(("TEL;TYPE=CELL", self.mobile_phone if self.mobile_phone else ''))
                writer.writerow(("TEL;TYPE=WORK", self.work_phone if self.work_phone else ''))
                writer.writerow(("EMAIL;TYPE=WORK", self.work_email if self.work_email else ''))
                writer.writerow(
                    ("ORG;CHARSET=UTF-8", self.parent_id.name.encode('utf8') if self.parent_id.name else ''))
                writer.writerow(("TITLE", self.job_id.name.encode('utf8') if self.job_id.name else ''))
                writer.writerow(("END", "VCARD"))

                out = base64.encodestring(buf.getvalue())
            self.write({
                'data': out,
                'file_name': 'contact_info.vcf'
            })

        compose_form = self.env.ref('export_vcard.wizard_employee_vcard')
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'hr.employee',
            'view_mode': 'form',
            'view_type': 'form',
            'res_id': self.id,
            'views': [(compose_form.id, 'form')],
            'view_id': compose_form.id,
            'target': 'new',
        }
