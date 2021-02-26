# -*- coding: utf-8 -*-
# from odoo import http


# class AdquatAudit(http.Controller):
#     @http.route('/adquat_audit/adquat_audit/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/adquat_audit/adquat_audit/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('adquat_audit.listing', {
#             'root': '/adquat_audit/adquat_audit',
#             'objects': http.request.env['adquat_audit.adquat_audit'].search([]),
#         })

#     @http.route('/adquat_audit/adquat_audit/objects/<model("adquat_audit.adquat_audit"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('adquat_audit.object', {
#             'object': obj
#         })
