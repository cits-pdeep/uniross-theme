# -*- coding: utf-8 -*-

from logging import getLogger

from odoo import http
from odoo.http import request
from odoo.tools import is_html_empty

_logger = getLogger(__name__)


class UnirossThemController(http.Controller):

    @http.route('/webform', auth='public', website=True)
    def web_form(self, **kwargs):
        return request.render('custom_web_form.web_form_template')

    @http.route('/submit-quote', type='http', auth='public', csrf=False, website=True, methods=['POST'])
    def web_form_submit(self, **post):
        order_id = post.get('order_id')
        order = request.env['sale.order'].sudo().browse(int(order_id))
        # request.env['custom.web.form.booking'].sudo().create({
        #     'name': post.get('name'),
        #     'phone': post.get('phone'),
        #     'email': post.get('email'),
        # })
        customerObj = request.env.ref('uniross_theme_extend.mail_template_sale_send_quote_customer', raise_if_not_found=False)
        ctx = dict(customerObj._context or {})
        ctx['name'] =  post.get('name')
        ctx['phone'] =  post.get('phone')
        ctx['customer_email'] =  post.get('customer_email')
        send_mail = customerObj.sudo().with_context(ctx).send_mail(order.id)
        request.env['mail.mail'].sudo().browse(send_mail).send()

        adminObj = request.env.ref('uniross_theme_extend.mail_template_sale_send_quote_admin', raise_if_not_found=False)
        send_mail = adminObj.sudo().with_context(ctx).send_mail(order.id)
        request.env['mail.mail'].sudo().browse(send_mail).send()
        order.unlink()
        return request.redirect('/contactus-thank-you')
