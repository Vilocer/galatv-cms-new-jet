$(function() {
    // WOW effect
    $('.wow-effect').each(function(i, element) {
        $(element).addClass('wow-effect__active');
    });
    
    $(window).on('load', function (e) {
        // Active labels if inputs not empty on load
        $('.form__item').each( function( i, form_item ) {
            var $form_item = $(form_item),
                input = $form_item.find('input');
    
            if(input.length == 0) {
                input = $form_item.find('textarea');
        
            }
        
            if( input.val() ) { 
                $form_item.find('label').addClass('active')
    
            }
            else {
            $form_item.find('label').removeClass('active')
    
            }
    
        });
    
    });
    
    // Active Labels if inputs not empty on edit
    $('.form__item').each( function( i, form_item ) {
        var $form_item = $(form_item),
            input = $form_item.find('input');
    
        if(input.length == 0) {
            input = $form_item.find('textarea');
    
        }
    
        input.blur( function() {
            if( $(this).val() ) { 
                $form_item.find('label').addClass('active')
    
           }
           else {
            $form_item.find('label').removeClass('active')
    
           }
    
        });
    
    });

});