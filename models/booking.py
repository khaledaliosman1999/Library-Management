from odoo import fields, models


class Booking(models.Model):
    _name = 'booking'
    _description = 'Booking'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    member_id = fields.Many2one('library.members', string='Member', required=True)
    booking_date = fields.Datetime(string='Booking Date', default=fields.Datetime.now)
    return_date = fields.Datetime(string='Return Date')
    booking_line_ids = fields.One2many('booking.line', 'booking_id', string='Booking Line')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('borrowed', 'Borrowed'),
        ('return', 'Returned'),
        ('late', 'Late'),
        ('cancel', 'Cancelled'),
    ],default='draft')

    def action_confirm(self):
        for rec in self:
            rec.state = 'borrowed'

    def action_borrowed(self):
        for rec in self:
            rec.state = "return"



class BookingLine(models.Model):
    _name = 'booking.line'
    _description = 'Booking Line'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    book_id = fields.Many2one('library.books', string='Book Name', required=True)
    booking_id = fields.Many2one('booking', string='Booking')
    author = fields.Char(string='Author')
    category = fields.Selection([
        ('arabic', 'Arabic'),
        ('english', 'English'),
        ('science', 'Science'),
        ('history', 'History')
    ], string='Category', default='arabic')
