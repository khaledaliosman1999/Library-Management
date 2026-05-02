from odoo import api, fields, models

class LibraryMembers(models.Model):
    _name = 'library.members'
    _description = 'Library Members'

    name = fields.Char(string='Name', required=True)
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    address = fields.Text(string='Address')
    register_data = fields.Date(string='Register Date')
    user_id = fields.Many2one('res.users', string='Responsible', default=lambda self: self.env.user)
