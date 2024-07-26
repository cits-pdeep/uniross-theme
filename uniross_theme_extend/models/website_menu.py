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

    def get_menu_name(self):
        words = self.name.split()
        if len(words) == 1:
            return self.name

        first_line = " ".join(words[:-1])
        second_line = words[-1]
        menu_name = "<span>%s</span><span>%s</span>"%(first_line, second_line)
        # first_line + "<br/>" + second_line
        return Markup(menu_name)
