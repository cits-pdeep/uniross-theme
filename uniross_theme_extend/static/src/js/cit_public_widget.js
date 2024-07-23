/** @odoo-module **/

import { WebsiteSale } from '@website_sale/js/website_sale';
import publicWidget from "@web/legacy/js/public/public_widget";

publicWidget.registry.WebsiteSaleLayout.include({
    async start() {
        await this._super(...arguments);
        this.updateLayoutInfo();
    },

    _onApplyShopLayoutChange: function (ev) {
        this._super(...arguments);
        this.updateLayoutInfo();
    },

    updateLayoutInfo(){
        var clickedValue = $('input[name=wsale_products_layout]:checked').val();
        var isList = clickedValue === 'list';
        if (isList) {
            $('.extra-buttons, .extra-name, .o_wsale_filmstip_container').removeAttr('style');
        } else {
            $('.extra-buttons').attr('style','display: none !important')
            $('.extra-name').attr('style','width: 100% !important')
            $('.o_wsale_filmstip_container').attr('style','display: none !important')
        }
    },
});
