# -*- coding: utf-8 -*-
from odoo import http

# class LibraryBookDate(http.Controller):
#     @http.route('/library_book_date/library_book_date/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/library_book_date/library_book_date/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('library_book_date.listing', {
#             'root': '/library_book_date/library_book_date',
#             'objects': http.request.env['library_book_date.library_book_date'].search([]),
#         })

#     @http.route('/library_book_date/library_book_date/objects/<model("library_book_date.library_book_date"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('library_book_date.object', {
#             'object': obj
#         })