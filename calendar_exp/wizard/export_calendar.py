import base64
import cStringIO
import contextlib
import csv
import datetime
import pytz

from odoo import models, fields, api


class DownloadContact(models.Model):
    _inherit = 'calendar.event'
    file_name = fields.Char()
    data = fields.Binary(string="File", readonly=True)

    @api.multi
    def download(self):
        if self.id:
            with contextlib.closing(cStringIO.StringIO()) as buf:
                tz = pytz.timezone(self.env.user.tz) if self.env.user.tz else pytz.utc
                if self.start_datetime:
                    start_datetime = self._convert_datetime_format(self.start_datetime)
                else:
                    start_datetime=''
                if self.start_date:
                    start_date =  self._convert_date_format(self.start_date)
                else:
                    start_date=''
                if self.stop_datetime:
                    stop_datetime = self._convert_datetime_format(self.stop_datetime)
                else:
                    stop_datetime=''
                if self.stop_date:
                    stop_date = self._convert_date_format(self.stop_date)
                else:
                    stop_date = ''
                if self.create_date:
                    create_date = self._convert_datetime_format(self.create_date)
                else:
                    create_date = self._convert_date_format(datetime.datetime.now())
                if self.start:
                    start = self._convert_datetime_format(self.start)
                else:
                    start =''
                if self.privacy =='public':
                    method = 'PUBLISH'
                elif self.privacy =='private':
                    method = 'REQUEST'
                elif self.privacy =='confidential':
                    method ='REQUEST'

                writer = csv.writer(buf, delimiter=":", quotechar='"')
                writer.writerow(("BEGIN", "VCALENDAR"))
                writer.writerow(("VERSION", "2.0"))
                writer.writerow(("PRODID", '-//magestore.vn//Calendar 1.0//EN'))
                writer.writerow(("CALSCALE", "GREGORIAN"))

                writer.writerow(("BEGIN", "VEVENT" ))
                writer.writerow(("X-WR-CALNAME", self.user_id.name.encode('utf8') if self.user_id.name else ''))
                writer.writerow(("X-WR-TIMEZONE", tz if tz else ''))
                writer.writerow(("METHOD", method))
                writer.writerow(("DTSTART", start_datetime if start_datetime else start_date))
                writer.writerow(("DTEND", stop_datetime if stop_datetime else stop_date ))
                writer.writerow(("DTSTAMP", start))
                writer.writerow(("UID",  self.user_id.id if self.user_id.id else ''))
                writer.writerow(("CREATED",  create_date))
                writer.writerow(("DESCRIPTION", self.description.encode('utf-8') if self.description else ''))
                writer.writerow(("LAST-MODIFIED", create_date))
                writer.writerow(("LOCATION", self.location.encode('utf-8') if self.location else ''))
                writer.writerow(("SEQUENCE", 0))
                writer.writerow(("STATUS", self.state.upper()))
                writer.writerow(("SUMMARY", self.name.encode('utf-8').upper() ))

                writer.writerow(("TRANSP", 'OPAQUE' ))
                writer.writerow(("END", 'VEVENT' ))
                writer.writerow(("END", 'VCALENDAR' ))

                out = base64.encodestring(buf.getvalue())
            self.write({
                'data': out,
                'file_name': self.name + '.ics'
            })

        compose_form = self.env.ref('calendar_exp.wizard_export_calendar')
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'calendar.event',
            'view_mode': 'form',
            'view_type': 'form',
            'res_id': self.id,
            'views': [(compose_form.id, 'form')],
            'view_id': compose_form.id,
            'target': 'new',
        }

    def _convert_date_format(self, s):
        s = s.replace('-', '')
        s += "T000000"
        return s

    def _convert_datetime_format(self,s):
        s = s.replace('-', '')
        s = s.replace(':', '')
        s = s.replace(' ', 'T')
        return s

