# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Caret IT Solutions Pvt. Ltd. (Website: www.caretit.com).           #
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################

from odoo import fields, models
from markupsafe import Markup

class WebsiteMenu(models.Model):
    _inherit = 'website.menu'

    menu_image = fields.Image()

    def set_mega_menu_data(self, content):
        self.mega_menu_content = Markup(content)
