from odoo import models, fields, api

class Course(models.Model):
    _name = 'new_modulo.course'
    name = fields.Char()
    title = fields.Char()
    description = fields.Text()
