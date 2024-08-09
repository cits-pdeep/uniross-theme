from odoo import api, fields, models
from markupsafe import Markup

class Product(models.Model):
    _inherit = "product.template"

    dimension_type = fields.Char()
    product_volts = fields.Float(digits=(12, 2))
    product_diameter = fields.Float(digits=(12, 2))
    product_height = fields.Float(digits=(12,2))
    product_width = fields.Float(digits=(12,2))
    product_depth = fields.Float(digits=(12,2))
    lifespan = fields.Char()
    uni_product_description = fields.Text()
    download_product_technical_sheet = fields.Char()
    download_product_image = fields.Char()

    def get_uni_product_description(self):
        return self.uni_product_description and Markup(self.uni_product_description) or ''