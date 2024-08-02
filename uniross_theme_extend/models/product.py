from odoo import api, fields, models


class Product(models.Model):
    _inherit = "product.template"

    dimension_type = fields.Char()
    product_volts = fields.Float(digits=(12, 2))
    product_diameter = fields.Float(digits=(12, 2))
    product_height = fields.Float(digits=(12,2))
    product_width = fields.Float(digits=(12,2))
    product_depth = fields.Float(digits=(12,2))
    lifespan = fields.Char()
    uni_product_description = fields.Html()