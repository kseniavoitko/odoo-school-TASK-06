from odoo import api, fields, models, _


class LibraryBookCategory(models.Model):
    _inherit = 'library.book.category'

    description = fields.Text(translate=True)

    def action_book_list(self):
        """Return all books with this category"""
        self.ensure_one()
        return {
            'name': _('Author Books'),
            'type': 'ir.actions.act_window',
            'view_mode': 'tree,form',
            'res_model': 'library.book',
            'context': {'default_category_id': self.id},
            'domain': [('category_id', '=', self.id)],
        }
