from odoo import api, fields, models


class LibraryBookCategory(models.Model):
    _name = 'library.book.category'
    _description = "Library Book's Category"

    name = fields.Char()
    active = fields.Boolean(
        string='Active',
        default=True,
    )
