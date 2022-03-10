from odoo import models, fields


class EstatePropertyType(models.Model):
    _name = 'estate.property.type'
    _description = 'estate property type description'
    _order = "name"

    name = fields.Char('Name', required=True)
    property_ids = fields.One2many('estate.property', 'property_type_id', string='Properties')
    sequence = fields.Integer('Sequence', default=1, help="Used to order stages. Lower is better.")
    _sql_constraints = [
        ('unique_tag', 'UNIQUE(name)', 'tag name should be unique.')
    ]
