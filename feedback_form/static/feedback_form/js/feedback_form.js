function hideForm(mobile) {
    $('#feedbackForm').fadeOut('fast', function() {
        if (mobile) {
            $('#feedbackSnippet').animate({bottom: '0'});
        } else {
            $('#feedbackSnippet').animate({left: '-70'});
        }
    });
}

function initiateForm(mobile) {
    var rect = {
        w : $('#feedbackForm').width(),
        h : $('#feedbackForm').height(),
    }
    if(mobile){
        $('#feedbackSuccess').css({'right': 30, 'left': 'auto', 'top': 'auto', 'bottom': 43});
    } else {
        $('#feedbackSuccess').css({'right': 'auto', 'left': 40, 'top': '50%', 'bottom': 'auto'});
    }


    $('#feedbackForm').unbind('submit');
    $('#feedbackForm input, #feedbackForm textarea').each(function() {
        $(this).attr('placeholder', $('[for=' + $(this).attr('id') + ']').text());
    });

    $('#feedbackForm #feedbackClose').click(function() {
        hideForm(mobile);
        return false;
    });

    $('#feedbackForm').submit(function() {
        var form = $(this);
        $.post(form.attr('action'), form.serializeArray(), function(data) {
            if (data.toLowerCase().indexOf('errorlist') == -1) {
                hideForm(mobile);
                if (mobile) {
                    $('#feedbackSuccess').fadeIn().delay(1000).animate({bottom: '-500'}).fadeOut().animate({bottom: '40'});
                } else {
                    $('#feedbackSuccess').fadeIn().delay(1000).animate({left: '-500'}).fadeOut().animate({left: '40'});
                }
            }
            form.html(data);
            initiateForm(mobile);
        });
        return false;
    });

    $('#feedbackSnippet').attr('href', '#');
    $('#feedbackSnippet').click(function() {
        if (mobile) {
            $(this).animate({bottom: '-200'});
            $('#feedbackForm').fadeIn().animate('bottom', rect.height);
        } else {
            $(this).animate({left: '-200'});
            $('#feedbackForm').fadeIn().animate('left',rect.width);
        }
        
        $('html').click(function() {
            hideForm(mobile);
         });

         $('#feedbackForm').click(function(event){
            event.stopPropagation();
         });
        return false;
    });
}

$(document).ready(function() {
    $(window).on('load  resize', function(){
        if ($('body').innerWidth() < 768) {
            initiateForm(true);
        } else {
            initiateForm(false);
        }
    });
});