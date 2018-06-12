# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class MVCController(http.Controller):
    @http.route('/mvc', type='http', auth="public", website=True)
    def mvc_overview(self, **kwargs):
        products = request.env['product.product'].search([])
        return request.render("mvc.overview", {'products': products})

    @http.route('/mvc/<model("product.product"):product>', type='http', auth="public", website=True)
    def mvc_detail(self, product=None, **kwargs):
        if product:
            return request.render("mvc.detail", {'product': product})
