from odoo import models, fields, api


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "estate property"
    # _order = "sequence"

    name = fields.Char('Name', required=True)
    description = fields.Text('Your Description')
    postcode = fields.Char('Postal Code')
    date_availability = fields.Date('Available From', copy=False, default=lambda self: fields.Datetime.now())
    expected_price = fields.Float('Expected Price', required=True)
    selling_price = fields.Float('Selling Price', readonly=True, copy=False)
    bedrooms = fields.Integer('Bedrooms', default=2)
    living_area = fields.Integer('Living Area')
    facades = fields.Integer('Facades')
    garage = fields.Boolean('Garage', default=True)
    garden = fields.Boolean('Garden', default=True)
    garden_area = fields.Integer('Garden Area')
    total_area = fields.Integer('Total Area', compute='_compute_total_area')
    garden_orientation = fields.Selection(
        string='Orientation',
        selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')],
        help="chose garden orientation"
    )
    active = fields.Boolean(default=True)
    state = fields.Selection(
        selection=[('New', 'New'), ('Offer', 'Offer'), ('Received', 'Received'), ('Offer', 'Offer'), ('Accepted', 'Accepted'), ('Sold', 'Sold'), ('Canceled', 'Canceled')],
        default='New'
    )
    property_type_id = fields.Many2one('estate.property.type', string='Property Type')
    buyer_id = fields.Many2one('res.partner', string='Buyer', copy=False)
    sales_person_id = fields.Many2one('res.users', string='Sales Person', default=lambda self: self.env.user)
    tag_ids = fields.Many2many('estate.property.tag', string='Tags')
    offer_ids = fields.One2many('estate.property.offer', 'property_id', string='Offer')

    @api.depends("living_area", "garden_area")
    def _compute_total_area(self):
        for records in self:
            records.total_area = records.living_area + records.garden_area
