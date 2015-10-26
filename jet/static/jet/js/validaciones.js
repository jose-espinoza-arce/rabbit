/**
 * Created by jose on 24/10/15.
 */
(function(){
    var jq = jet.jQuery;
    // formulario agregar banners

    jq(document).on('ready', function () {
        jq('#advertiser_form').validate({
            rules : {
                'company_name' : 'required'
            },
            messages: {
                'company_name': 'Tu Publiciación debe tener un titulo.'
            }
        });
        console.log(jq('#advertiser_form').length>0);
    });


})();