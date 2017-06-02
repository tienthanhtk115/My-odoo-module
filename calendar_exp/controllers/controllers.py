import csv
import json
from StringIO import StringIO

import datetime
import pytz
import odoo.http as http
from odoo.addons.web.controllers.main import serialize_exception, ExportFormat

from odoo.service import model


class CalendarExport(ExportFormat, http.Controller):
    @serialize_exception
    def index(self, data, token):
        return self.base(data, token)

    @property
    def content_type(self):
        return 'text/csv;charset=utf8'

    def filename(self, base):
        return base + '.ics'

    def from_data_calendar(self, fields, rows):
        fp = StringIO()
        writer = csv.writer(fp, delimiter=":", quotechar='"')
        writer.writerow(("BEGIN", "VCALENDAR"))
        writer.writerow(("VERSION", "2.0"))
        writer.writerow(("PRODID", '-//magestore.vn//Calendar 1.0//EN'))
        writer.writerow(("CALSCALE", "GREGORIAN"))

        for data in rows:
            lst_data2 = []
            lst_data2.append(data)
            for index,lst_data in enumerate(lst_data2):
                event = http.request.env['calendar.event'].search([('id', '=', lst_data[0])], limit=1)
                tz = pytz.timezone(event.env.user.tz) if event.env.user.tz else pytz.utc
                if event.start_datetime:
                    start_datetime = self._convert_datetime_format(event.start_datetime)
                else:
                    start_datetime = ''
                if event.start_date:
                    start_date = self._convert_date_format(event.start_date)
                else:
                    start_date = ''
                if event.stop_datetime:
                    stop_datetime = self._convert_datetime_format(event.stop_datetime)
                else:
                    stop_datetime = ''
                if event.stop_date:
                    stop_date = self._convert_date_format(event.stop_date)
                else:
                    stop_date = ''
                if event.create_date:
                    create_date = self._convert_datetime_format(event.create_date)
                else:
                    create_date = self._convert_date_format(datetime.datetime.now())
                if event.start:
                    start = self._convert_datetime_format(event.start)
                else:
                    start = ''
                if event.privacy == 'public':
                    method = 'PUBLISH'
                elif event.privacy == 'private':
                    method = 'REQUEST'
                elif event.privacy == 'confidential':
                    method = 'REQUEST'

                writer.writerow(("BEGIN", "VEVENT"))
                writer.writerow(("X-WR-CALNAME", event.user_id.name.encode('utf8') if event.user_id.name else ''))
                writer.writerow(("X-WR-TIMEZONE", tz if tz else ''))
                writer.writerow(("METHOD", method))
                writer.writerow(("DTSTART", start_datetime if start_datetime else start_date))
                writer.writerow(("DTEND", stop_datetime if stop_datetime else stop_date))
                writer.writerow(("DTSTAMP", start))
                writer.writerow(("UID", event.user_id.id if event.user_id.id else ''))
                writer.writerow(("CREATED", create_date))
                writer.writerow(("DESCRIPTION", event.description.encode('utf-8') if event.description else ''))
                writer.writerow(("LAST-MODIFIED", create_date))
                writer.writerow(("LOCATION", event.location.encode('utf-8') if event.location else ''))
                writer.writerow(("SEQUENCE", 0))
                writer.writerow(("STATUS", event.state.upper()))
                writer.writerow(("SUMMARY", event.name.encode('utf-8').upper()))
                writer.writerow(("TRANSP", 'OPAQUE'))
                writer.writerow(("END", 'VEVENT'))
                if index == len(lst_data2) - 1:
                    writer.writerow(("END", 'VCALENDAR'))


        fp.seek(0)
        data = fp.read()
        fp.close()
        return data

    def _convert_date_format(self, s):
        s = s.replace('-', '')
        s += "T000000"
        return s

    def _convert_datetime_format(self, s):
        s = s.replace('-', '')
        s = s.replace(':', '')
        s = s.replace(' ', 'T')
        return s

class Vcalendar(CalendarExport):
    def __getattribute__(self, name):
        if name == 'fmt':
            raise AttributeError()
        return super(Vcalendar, self).__getattribute__(name)

    @http.route('/web/export/xls_view', type='http', auth='user')
    def export_xls_view(self, data, token):
        data = json.loads(data)
        model = data.get('model', [])
        columns_headers = data.get('headers', [])
        rows = data.get('rows', [])
        if model == 'calendar.event':
            return http.request.make_response(
                self.from_data_calendar(columns_headers, rows),
                headers=[
                    ('Content-Disposition', 'attachment; filename="%s"'
                     % self.filename(model)),
                    ('Content-Type', self.content_type)
                ],
                cookies={'fileToken': token}
            )
        else:
            return http.request.make_response(
                self.from_data(columns_headers, rows),
                headers=[
                    ('Content-Disposition', 'attachment; filename="%s"'
                     % self.filename(model)),
                    ('Content-Type', self.content_type)
                ],
                cookies={'fileToken': token}
            )
