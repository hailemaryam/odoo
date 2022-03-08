from odoo import models, fields, api
from datetime import date, datetime, timedelta


class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "estate property offer"

    price = fields.Float('Price', required=True)
    status = fields.Selection(
        selection=[('Accepted', 'Accepted'), ('Refused', 'Refused')],
        copy=False
    )
    validity = fields.Integer('Validity')
    date_deadline = fields.Date('Dead Line', compute='_compute_date_deadline', inverse='_inverse_date_deadline')
    partner_id = fields.Many2one('res.partner', string='Buyer', required=True)
    property_id = fields.Many2one('estate.property', string="Property", required=True)

    @api.depends('validity')
    def _compute_date_deadline(self):
        for record in self:
            if record.create_date:
                record.date_deadline = record.create_date + timedelta(days=record.validity)
            else:
                record.date_deadline = datetime.now() + timedelta(days=record.validity)

    def _inverse_date_deadline(self):
        for record in self:
            if record.create_date:
                delta_days = record.date_deadline - record.create_date.date()
                record.validity = delta_days.days
            else:
                delta_days = record.date_deadline - date.today()
                record.validity = delta_days.days

    def action_accept(self):
        self.status = 'Accepted'
        return True

    def action_reject(self):
        self.status = 'Refused'
        return True
