# -*- coding: utf-8 -*-
# from odoo import http


# class MassPaymentsGroup(http.Controller):
#     @http.route('/mass_payments_group/mass_payments_group/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mass_payments_group/mass_payments_group/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mass_payments_group.listing', {
#             'root': '/mass_payments_group/mass_payments_group',
#             'objects': http.request.env['mass_payments_group.mass_payments_group'].search([]),
#         })

#     @http.route('/mass_payments_group/mass_payments_group/objects/<model("mass_payments_group.mass_payments_group"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mass_payments_group.object', {
#             'object': obj
#         })
