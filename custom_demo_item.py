from odoo import fields, models


class CustomDemoItem(models.Model):
    _name = 'custom.demo.item'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Customer Service Ticket'
    _order = 'priority desc, create_date desc'

    name = fields.Char(string='Ticket Title', required=True, tracking=True)
    customer_name = fields.Char(string='Customer', required=True, tracking=True)
    contact_email = fields.Char(string='Email', tracking=True)
    phone = fields.Char(string='Phone', tracking=True)
    description = fields.Text(string='Description', tracking=True)
    solution = fields.Text(string='Resolution', tracking=True)
    priority = fields.Selection(
        [('low', 'Low'), ('normal', 'Normal'), ('high', 'High')],
        string='Priority',
        default='normal',
        required=True,
        tracking=True,
    )
    state = fields.Selection(
        [
            ('new', 'New'),
            ('in_progress', 'In Progress'),
            ('resolved', 'Resolved'),
            ('closed', 'Closed'),
        ],
        string='Status',
        default='new',
        required=True,
        tracking=True,
    )
    assigned_to = fields.Many2one(
        'res.users',
        string='Assigned to',
        default=lambda self: self.env.user,
        tracking=True,
    )
    amount = fields.Monetary(string='Amount', currency_field='currency_id')
    currency_id = fields.Many2one(
        'res.currency',
        string='Currency',
        default=lambda self: self.env.company.currency_id,
    )
    date_created = fields.Datetime(string='Created On', default=fields.Datetime.now, readonly=True)
    close_date = fields.Datetime(string='Closed On', readonly=True)
    active = fields.Boolean(string='Active', default=True)

    def action_assign(self):
        self.write({'state': 'in_progress'})

    def action_resolve(self):
        self.write({'state': 'resolved', 'close_date': fields.Datetime.now()})

    def action_close(self):
        self.write({'state': 'closed', 'close_date': fields.Datetime.now()})

    def action_reopen(self):
        self.write({'state': 'new', 'close_date': False})
