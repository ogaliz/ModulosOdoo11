# -*- coding: utf-8 -*-

from odoo import models, fields #, api

class LibraryBook(models.Model):
    _name = 'Library.book'

    name = fields.Char(string="Name")
    active = fields.Boolean("Is active")
    image = fields.Binary()
    pages = fields.Integer(string="# Pages")
    isbn = fields.Char(string="ISBN", size=13)

    # @api.depends('value')
    # def _value_pc(self):
    #     self.value2 = float(self.value) / 100