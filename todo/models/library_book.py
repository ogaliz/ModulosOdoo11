# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class todo(models.Model):
#     _name = 'todo.todo'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

class LibraryBook(models.Model):
    _inherit =  'library.book'
    
    date =  fields.Date(string="Release Date")