# from odoo import http


# class NewModulo(http.Controller):
#     @http.route('/new_modulo/new_modulo', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/new_modulo/new_modulo/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('new_modulo.listing', {
#             'root': '/new_modulo/new_modulo',
#             'objects': http.request.env['new_modulo.new_modulo'].search([]),
#         })

#     @http.route('/new_modulo/new_modulo/objects/<model("new_modulo.new_modulo"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('new_modulo.object', {
#             'object': obj
#         })

