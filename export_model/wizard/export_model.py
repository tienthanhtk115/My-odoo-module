# -*- encoding: utf-8 -*-
import base64
import cStringIO
import contextlib
import unicodecsv as csv

from odoo import api, fields, models


class ExportModel(models.TransientModel):
    _name = 'export.module'

    name = fields.Char(string="File Name", readonly=True)
    data = fields.Binary(string="File", readonly=True)
    ir_model = fields.Many2one('ir.model')
    model_fields = fields.Many2many('ir.model.fields')
    state = fields.Selection([('choose', 'choose'), ('get', 'get')], default='choose')

    @api.multi
    @api.onchange('ir_model')
    def _compute_model(self):
        self.model_fields = self.env['ir.model.fields'].search([('model', '=', self.ir_model.model)])

    @api.multi
    def do_export2(self):
        if self.ir_model:
            limit = ['many2one', 'many2many', 'one2many']
            lst_name = []
            with contextlib.closing(cStringIO.StringIO()) as buf:
                writer = csv.writer(buf, delimiter=";", encoding="utf-8")
                for f in self.model_fields:
                    lst_name.append(f.name)
                writer.writerow((lst_name))
                lst_object = self.env[self.ir_model.model].search([])
                for object in lst_object:
                    line = []
                    for field in self.model_fields:
                        if field.ttype not in limit:
                            for temp in object.mapped(field.name):
                                line.append(temp)
                        else:
                            line.append('')
                    writer.writerow((line))
                out = base64.encodestring(buf.getvalue())
            self.write({
                'state': 'get',
                'data': out,
                'name': 'data.csv'
            })

        return {
            'type': 'ir.actions.act_window',
            'res_model': 'export.module',
            'view_mode': 'form',
            'view_type': 'form',
            'res_id': self.id,
            'views': [(False, 'form')],
            'target': 'new',
        }

        # @api.multi
        # def _export_rows(self, fields):
        #     """ Export fields of the records in ``self``.
        #
        #         :param fields: list of lists of fields to traverse
        #         :return: list of lists of corresponding values
        #     """
        #     lines = []
        #     for record in self:
        #         # main line of record, initially empty
        #         current = [''] * len(fields)
        #         lines.append(current)
        #
        #         # list of primary fields followed by secondary field(s)
        #         primary_done = []
        #
        #         # process column by column
        #         for i, path in enumerate(fields):
        #             if not path:
        #                 continue
        #
        #             name = path[0]
        #             if name in primary_done:
        #                 continue
        #
        #             if name == '.id':
        #                 current[i] = str(record.id)
        #             elif name == 'id':
        #                 current[i] = record.__export_xml_id()
        #             else:
        #                 field = record._fields[name]
        #                 value = record[name]
        #
        #                 # this part could be simpler, but it has to be done this way
        #                 # in order to reproduce the former behavior
        #                 if not isinstance(value, BaseModel):
        #                     current[i] = field.convert_to_export(value, record)
        #                 else:
        #                     primary_done.append(name)
        #
        #                     # This is a special case, its strange behavior is intended!
        #                     if field.type == 'many2many' and len(path) > 1 and path[1] == 'id':
        #                         xml_ids = [r.__export_xml_id() for r in value]
        #                         current[i] = ','.join(xml_ids) or False
        #                         continue
        #
        #                     # recursively export the fields that follow name
        #                     fields2 = [(p[1:] if p and p[0] == name else []) for p in fields]
        #                     lines2 = value._export_rows(fields2)
        #                     if lines2:
        #                         # merge first line with record's main line
        #                         for j, val in enumerate(lines2[0]):
        #                             if val or isinstance(val, bool):
        #                                 current[j] = val
        #                         # check value of current field
        #                         if not current[i] and not isinstance(current[i], bool):
        #                             # assign xml_ids, and forget about remaining lines
        #                             xml_ids = [item[1] for item in value.name_get()]
        #                             current[i] = ','.join(xml_ids)
        #                         else:
        #                             # append the other lines at the end
        #                             lines += lines2[1:]
        #                     else:
        #                         current[i] = False
        #
        #     return lines
        #
        # # backward compatibility
        # __export_rows = _export_rows
        #
        # @api.multi
        # def export_data(self, fields_to_export, raw_data=False):
        #     """ Export fields for selected objects
        #
        #         :param fields_to_export: list of fields
        #         :param raw_data: True to return value in native Python type
        #         :rtype: dictionary with a *datas* matrix
        #
        #         This method is used when exporting data via client menu
        #     """
        #     fields_to_export = map(fix_import_export_id_paths, fields_to_export)
        #     if raw_data:
        #         self = self.with_context(export_raw_data=True)
        #     return {'datas': self._export_rows(fields_to_export)}
        # khsfklsafklsd;flmsdf
