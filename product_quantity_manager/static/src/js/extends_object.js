odoo.define('pos_product_available', function (require) {

"use strict";

	var module = require('point_of_sale.models');
	var ProductScreenWidget = require('point_of_sale.screens');

    var models = module.PosModel.prototype.models;
//    add field qty_available when load data
    for(var i=0; i<models.length; i++){

        var model=models[i];

        if(model.model === 'product.product'){

             model.fields.push('qty_available');

        }

    }
//override action when product widget is clicked

    var ProductScreenWidget = ProductScreenWidget.ProductScreenWidget.include({
        click_product: function(product){
            if (product.qty_available==0){
                alert('Sorry, this product temporary not available!');
            }
            else{
                this._super(product);
            }
        },


        alertWithoutNotice: function(message){
        setTimeout(function(){
            alert(message);
        }, 1000);
}
    });
});
