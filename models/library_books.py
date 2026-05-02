from odoo import api, fields, models

class LibraryBooks(models.Model):
    _name = 'library.books'
    _description = 'Library Books'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Title', required=True)
    author = fields.Char(string='Author')
    category = fields.Selection([
        ('arabic', 'Arabic'),
        ('english', 'English'),
        ('science', 'Science'),
        ('history', 'History')
    ], string='Category', default='arabic')
