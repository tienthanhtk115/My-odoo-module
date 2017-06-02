# -*- coding: utf-8 -*-
import re

from odoo import http
from odoo.http import request
from odoo.addons.website_portal.controllers.main import website_account
from odoo.addons.auth_signup.controllers.main import AuthSignupHome
from odoo.addons.web.controllers.main import Home
from odoo.addons.website_my_profile.models.models import ResetDirectError, ChangeMailError
from odoo.addons.auth_signup.models.res_users import SignupError


# from odoo.addons.auth_signup.models.res_users import SignupError


def check_correct_format_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def password_check(password):
    """
    Verify the strength of 'password'
    Returns a dict indicating the wrong criteria
    A password is considered strong if:
        8 characters length or more
        1 digit or more
        1 symbol or more
        1 uppercase letter or more
        1 lowercase letter or more
    """

    # calculating the length
    length_error = len(password) < 8

    # searching for digits
    digit_error = re.search(r"\d", password) is None

    # searching for uppercase
    uppercase_error = re.search(r"[A-Z]", password) is None

    # searching for lowercase
    lowercase_error = re.search(r"[a-z]", password) is None

    # searching for symbols
    symbol_error = re.search(r"[ !#$%&'()*+,-./[\\\]^_`{|}~" + r'"]', password) is None

    # overall result
    password_ok = not (length_error or digit_error or uppercase_error or lowercase_error or symbol_error)

    return {
        'password_ok': password_ok,
        'length_error': length_error,
        'digit_error': digit_error,
        'uppercase_error': uppercase_error,
        'lowercase_error': lowercase_error,
        'symbol_error': symbol_error,
    }


# add more fields to my/account page
class AccountInfo(website_account):
    @http.route()
    def details(self, redirect=None, **post):
        result = super(AccountInfo, self).details(redirect, **post)
        self.MANDATORY_BILLING_FIELDS.extend(['birthday', 'login'])
        self.OPTIONAL_BILLING_FIELDS.extend(['active', 'gender'])
        qcontext = result.qcontext
        genders = request.env['res.partner'].get_value_gender()
        qcontext['genders'] = genders
        qcontext['login'] = request.env['res.users'].sudo().search(
            [('id', '=', request.session.uid)]).login
        return result


# add birthday to signup page
class UserAccount(AuthSignupHome):
    @http.route()
    def web_auth_signup(self, *args, **kw):
        res = super(UserAccount, self).web_auth_signup(*args, **kw)
        qcontext = res.qcontext
        if request.session.uid:
            return request.redirect('/')
        if qcontext.get('error_detail'):
            qcontext['error'] = qcontext['error_detail']
        return res

    def do_signup(self, qcontext):
        values = {key: qcontext.get(key) for key in (
            'login', 'name', 'birthday', 'password')}
        user = request.env['res.users'].sudo().search(
            [('login', '=', values.get('login'))])
        if not user:
            if not re.match(r"[^@]+@[^@]+\.[^@]+", values.get('login')):
                qcontext['error_detail'] = 'Your email is invalid'
                raise SignupError

        if not values.values():
            qcontext['error_detail'] = 'The form was not properly filled in.'
            raise SignupError

        if not password_check(qcontext.get('password')).get('password_ok'):
            qcontext['error_detail'] = 'Password needs : 8 characters length or more, at least 1 digit,\n' \
                                       '1 symbol, 1 uppercase, 1 lowercase'
            raise SignupError

        if not values.get('password') == qcontext.get('confirm_password'):
            qcontext['error_detail'] = 'Passwords do not match; please retype them.'
            raise SignupError

        supported_langs = [lang['code'] for lang in request.env[
            'res.lang'].sudo().search_read([], ['code'])]
        if request.lang in supported_langs:
            values['lang'] = request.lang
        self._signup_with_values(qcontext.get('token'), values)
        request.env.cr.commit()

    @http.route()
    def web_auth_reset_password(self, *args, **kw):
        res = super(UserAccount, self).web_auth_reset_password(*args, **kw)
        if request.session.uid:
            return request.redirect('/')
        return res


# change password and change login name
class PasswordEmail(Home):
    @http.route('/web/reset_password_direct', type='http', auth='public', website=True)
    def reset_password_direct(self, *args, **kw):
        if not request.session.uid:
            return request.redirect('/')
        qcontext = request.params.copy()
        if 'error' not in qcontext and request.httprequest.method == 'POST':
            try:
                self.do_reset_password_direct(qcontext)
                if check_correct_format_email(qcontext.get('login')):
                    request.env['res.users'].sudo().reset_password(
                        qcontext.get('login'))
                return request.redirect('/web')
            except ResetDirectError:
                qcontext['error'] = qcontext.get('error_detail')
            except Exception:
                qcontext['error'] = 'Could not reset password.'
        return request.render('website_my_profile.form_reset', qcontext)

    def do_reset_password_direct(self, qcontext):
        values = {key: qcontext.get(key) for key in (
            'old_password', 'new_password', 'retype_password')}
        uid = request.session.uid
        login = request.env['res.users'].sudo().search(
            [('id', '=', uid)]).login
        qcontext['login'] = login

        if not login:
            qcontext['error_detail'] = 'No login provided.'
            raise ResetDirectError

        if not password_check(qcontext.get('password')).get('password_ok'):
            qcontext['error_detail'] = 'Password needs : 8 characters length or more, at least 1 digit,\n' \
                                       '1 symbol, 1 uppercase, 1 lowercase'
            raise ResetDirectError

        if values.get('new_password') != values.get('retype_password'):
            qcontext['error_detail'] = 'Passwords do not match, please retype them.'
            raise ResetDirectError

        request.env['res.users'].sudo().change_password(
            values.get('old_password'), values.get('new_password'))

    @http.route('/web/change_email', type='http', auth='public', website=True)
    def change_email(self, *args, **kw):
        if not request.session.uid:
            return request.redirect('/')
        qcontext = request.params.copy()
        uid = request.session.uid
        current_login = request.env['res.users'].sudo().search(
            [('id', '=', uid)]).login
        if kw:
            qcontext.update({'login': kw['login']})
        if not qcontext.get('login'):
            qcontext['login'] = current_login
        if 'error' not in qcontext and request.httprequest.method == 'POST':
            try:
                self.do_change_email(qcontext)
                user = request.env['res.users'].sudo().search([('login', '=', current_login)])[0]
                if user:
                    user.write({'login': qcontext.get('login')})
                    return request.redirect('/web/session/logout?redirect=/web/login')
            except ChangeMailError:
                qcontext['error'] = qcontext.get('error_detail')
            except Exception:
                qcontext['error'] = 'Could not change email.'
        return request.render('website_my_profile.form_email', qcontext)

    def do_change_email(self, qcontext):
        uid = request.session.uid
        current_login = request.env['res.users'].sudo().search(
            [('id', '=', uid)]).login

        if not qcontext.get('login') or not current_login:
            qcontext['error_detail'] = 'No login provided.Please go to Sign in page'
            raise ChangeMailError

        if qcontext.get('login') != current_login and request.env['res.users'].sudo().search(
                [('login', '=', qcontext.get('login'))]):
            qcontext[
                'error_detail'] = 'Another user is already registered using this login name.'
            raise ChangeMailError

        request.env['res.users'].change_password(
            qcontext.get('password'), qcontext.get('password'))

    @http.route()
    def web_login(self, redirect=None, **kw):
        res = super(PasswordEmail, self).web_login(redirect, **kw)
        if request.session.uid:
            return request.redirect('/')
        return res
