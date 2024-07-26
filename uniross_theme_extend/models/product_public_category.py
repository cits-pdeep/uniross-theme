# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Caret IT Solutions Pvt. Ltd. (Website: www.caretit.com).           #
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################

from odoo import fields, models
from markupsafe import Markup

class ProductPublicCategory(models.Model):
    _inherit = 'product.public.category'

    is_industrial_category = fields.Boolean()
