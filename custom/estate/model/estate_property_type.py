from odoo import models, fields


class EstatePropertyType(models.Model):
    _name = 'estate.property.type'
    _description = 'estate property type description'

    name = fields.Char('Name', required=True)
    _sql_constraints = [
        ('unique_tag', 'UNIQUE(name)', 'tag name should be unique.')
    ]
