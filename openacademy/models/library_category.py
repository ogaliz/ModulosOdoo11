# -*- coding: utf-8 -*-

from odoo import models, fields , api

class LibraryCategory(models.Model):
    _name = 'library.category'

    name = fields.Char(string="Name")
    active = fields.Boolean("Is active")

    # @api.depends('value')
    # def _value_pc(self):
    #     self.value2 = float(self.value) / 100