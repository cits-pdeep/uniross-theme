# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Caret IT Solutions Pvt. Ltd. (Website: www.caretit.com).           #
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################

{
    'name': 'Theme Extended',
    'version': '1.0',
    'license': 'OPL-1',
    'summary': 'Theme Extended',
    'category': 'Website',
    'description': """ Theme modification """,
    'author': 'Caret IT Solutions Pvt. Ltd.',
    'website': 'http://www.caretit.com',
    'depends': ['website_sale'],
    'data': [
        'views/website_menu.xml',
        'views/website_templates.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            '/uniross_theme_extend/static/src/css/style.css',
            '/uniross_theme_extend/static/src/js/cit_public_widget.js',
        ],
    },
}
