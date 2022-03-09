from odoo import models, fields


class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "estate property tag"

    name = fields.Char('Name', required=True)
    _sql_constraints = [
        ('unique_tag', 'UNIQUE(name)', 'tag name should be unique.')
    ]
