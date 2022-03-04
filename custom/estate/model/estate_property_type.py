from odoo import models, fields


class EstatePropertyType(models.Model):
    _name = 'estate.property.type'
    _description = 'estate property type description'

    name = fields.Char('Name', required=True)
