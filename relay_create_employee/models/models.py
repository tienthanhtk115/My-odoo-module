# -*- coding: utf-8 -*-

from odoo import models, fields, api

class User(models.Model):
    _inherit = ['res.users']

    employee_id = fields.Many2one('hr.employee')

    @api.model
    def create(self, vals):
        # create user
        new_user = super(User, self).create(vals)
        if new_user:
            user = self.search([('id', '=', new_user.id)], limit=1)
            if user:
                new_employee = self.env[
                    'hr.employee'].create({'name': user.name})

                employee = self.env['hr.employee'].search(
                    [('id', '=', new_employee.id)], limit=1)
                user.write({'employee_id': employee.id})
                employee.write({'user_id': user.id, 'work_email': user.login})
        return user

    @api.multi
    def unlink(self):
        # delete user also delete related employee
        for user in self:
            employee = self.env['hr.employee'].search(
                [('id', '=', user.employee_id.id)])
            if employee:
                employee.unlink()
        res = super(User, self).unlink()
        return res

    @api.multi
    def write(self, vals):
        # if login name change
        if 'login' in vals:
            employee = self.env['hr.employee'].search(
                [('id', '=', self.employee_id.id)])
            # change login of user
            employee.write({'work_email': vals['login']})

        res = super(User, self).write(vals)
        return res
