# -*- coding: utf-8 -*-
# from odoo import http


# class Sekolah(http.Controller):
#     @http.route('/sekolah/sekolah/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sekolah/sekolah/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sekolah.listing', {
#             'root': '/sekolah/sekolah',
#             'objects': http.request.env['sekolah.sekolah'].search([]),
#         })

#     @http.route('/sekolah/sekolah/objects/<model("sekolah.sekolah"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sekolah.object', {
#             'object': obj
#         })
