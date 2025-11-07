# from odoo import models, fields, api


# class new_modulo(models.Model):
#     _name = 'new_modulo.new_modulo'
#     _description = 'new_modulo.new_modulo'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

