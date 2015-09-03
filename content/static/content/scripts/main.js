/**
 *
 * Author: Noe Sanchez
 * Module: Cookie
 * Task: Get the CSRF required by Django
 *
 */

 var Cookie = (function ($) {
   var cookie = {
      init: function(){
        this.csrftoken = this.getCookie("csrftoken");
        this.inject();
        return this;
      },

      inject: function() {
        var self = this;

        $.ajaxSetup({
          beforeSend: function(xhr, settings) {
            if (!self.csrfSafeMethod(settings.type) && !this.crossDomain) {
              xhr.setRequestHeader("X-CSRFToken", self.csrftoken);
            }
          }
        });
      },

      csrfSafeMethod: function(method){
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
      },

      getCookie: function(name){
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
          var cookies = document.cookie.split(';');
          for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
            }
          }
        }
        return cookieValue;
      }
   };

   return cookie.init();
 })(jQuery);

/**
 *
 * Author: Noe Sanchez
 * Module: Header
 * Task: Update logo position and open the menu.
 *
 */

var Header = (function($){

  var header = {
    init: function() {

      this.open = false;

      this.elements = {
        'brand' : $('.header__brand'),
        'logo' : $('.logo'),
        'trigger': $('.trigger-nav'),
        'container' : $('.container'),
        'win' : $(window)
      };

      this.bind();
      return this;
    },

    bind: function(){
      var self = this;

      this.elements.win.on('load resize', function(){
        var offsetLeft =  Math.ceil ( ( $( this ).outerWidth() - self.elements.container.outerWidth() ) / 2 );

        var spacing = 148;

        self.elements.brand.css({
          'margin-left': offsetLeft + spacing
        });

        self.elements.logo.css({
          'width' : offsetLeft + spacing,
          'margin-left': -offsetLeft - spacing
        });

        self.elements.trigger.css({
          'right' : offsetLeft + 40
        });

      });

      this.elements.trigger.on('click', function (ev) {
        ev.preventDefault();
        self.toggle();
      });

    },
    toggle: function(){
      var self = this;
      var doc = $(document.body);

      if(this.open) {
        doc.removeClass('nav-active');
      } else {
        doc.addClass('nav-active');
      }

      this.open =!this.open;
    }
  };

  return header.init();
})(jQuery);

/**
 *
 * Author: Noe Sanchez
 * Module: Detail
 * Task: Handler action like phone button and form side
 *
 */

var Detail = (function ($) {
  var detail = {
    init: function(){

      this.cache();
      this.bind();

      return this;
    },
    cache: function(){
      this.el = $('div.detail');
      this.trigger = $('.detail a.action-button, .detail a.action-image');
      this.phone = $('.detail a.simple-button');

      this.back = $('.detail a.detail__back');
      this.submit = $('.detail :submit');
    },
    bind: function() {

      var self = this;

      function loadsuccess(response) {
              var markup = $.parseHTML(response);
              var form = null;
              if ( $('.form-wrapper').length ) {
                  self.el.find('.form-wrapper').remove();
              }

              if ( $('.success-wrapper').length ) {
                  /*  Uncomment to reload form after submit
                  self.el.find('.success-wrapper').remove();
                  */
                  /* Comment to reload form after submit*/
                  return
              }
              $.each(markup, function (i, el) {
                if ($(el).hasClass('form-wrapper')) {
                  form = $(el);
                  self.el.find('.detail__form').append(form);
                  $.getScript("https://www.google.com/recaptcha/api.js?hl=es-419");
                  setTimeout(bindform, 500);
                  return
                };
                if ($(el).hasClass('success-wrapper')) {
                  exito = $(el);
                  self.el.find('.detail__form').append(exito);
                  return
                };
              });
      }

      function bindform(){
          $('#action-call-form').submit(function () { // catch the form's submit event
              var that = $(this);

              $.ajax({ // create an AJAX call...
                  data: that.serialize(), // get the form data
                  type: $(this).attr('method'), // GET or POST
                  url: $(this).attr('action'), // the file to call
                  success: loadsuccess,
                  error: function () {
                      console.log('error')
                  }
              });
              return false;
          });
          if ($('#id_fecha').length) {
              console.log('hay fecha');
              $('#id_hora').datetimepicker({
                  datepicker: false,
                  format: 'H:i',
                  step: 20
              });
              $('#id_fecha').datetimepicker({
                  yearOffset: 0,
                  lang: 'es',
                  timepicker: false,
                  format: 'd/m/Y',
                  formatDate: 'Y/m/d',
                  minDate: '0', // yesterday is minimum date
                  maxDate: '2020/09/01' // and tommorow is maximum date calendar
              });
          }
      }

      this.trigger.on('click', function (ev) {
        ev.preventDefault();
        var url = $(this).attr('href');
        if ( !$('.form-wrapper').length && !$('.success-wrapper').length ) {
            $.get(url, loadsuccess);
            self.openForm();
        }
        else {
            self.openForm();
        }
      });

      this.back.on('click', function (ev) {
        ev.preventDefault();
        self.closeForm();
      });

      this.phone.on('click', function(ev){
        ev.preventDefault();

        self.phone.addClass('simple-button--active');
        var that = $(this);
        var pk = that.attr('data-pk');
        var url = '/phone/';

        $.post( url , { pk : pk }, function (response) {
          console.log('response:', response);
          that.off('click');
        });

      });
    },
    openForm: function(){
      this.el.addClass('detail--open');
    },
    closeForm: function(){
      this.el.removeClass('detail--open');
    },
  }

  return detail.init()
})(jQuery);



// Autor: Jose




$(function () {
    var $container = $("ul.wall .row");

    $container.imagesLoaded(function () {
        console.log('en el imageslodwed');
        $container.masonry({
            itemSelector : '.brick',
            columnWidth: '.grid-sizer'
        });
        console.log($container.masonry);
    });

    $container.infinitescroll(
        {
            navSelector: ".pagination",
            nextSelector: ".pagination .next",
            itemSelector: ".brick",
            loading: {
                finishedMsg: "The End",
                img: "/static/content/images/roof-loader.gif",
                msg: null,
                msgText: ""
            },
            debug: true
        },
        function (newProducts) {
            var $newProds = $(newProducts).css({"opacity": 0});
            $newProds.imagesLoaded(function () {
                $newProds.animate({"opacity": 1});
                $container.masonry("appended", $newProds, true);
            });
        }
    );
});

// autocomplete

Snippets = window.Snippets || {};


(function(S, $) {

  var TagCompletion = function(options) {
    this.options = options || {};
    this.default_url = '/taghint/';
  };

  // other code here...
  TagCompletion.prototype.bind_listener = function(input_sel) {
    var self = this;

    this.input_element = $(input_sel);

    this.input_element.autocomplete({
      minLength: self.options.min_length || 3,
      source: function(request, response) {self.fetch_results(request, response);},
    });
  };

  TagCompletion.prototype.fetch_results = function(request, response) {
    var url = this.options.url || this.default_url,
        term = request.term,
        last_piece = get_last_piece(term);

    if (!last_piece)
      response([]);

    var pieces = clean_and_split(term),
        all_but_last = '';
    pieces.pop();

    // if there are already some tags present, then grab everything up to the
    // current phrase and add a comma
    if (pieces.length > 0)
      all_but_last = pieces.join(', ') + ', ';

    $.getJSON(url, {'q': last_piece}, function(data) {
      var results = [];
      $.each(data, function(k, v) {
        v.label = v.tag + ' (' + v.count + ')';
        v.value = all_but_last + v.tag + ', ';
        results.push(v);
      });
      response(results);
    });
  };

  /* helper functions for splitting the string */
  function clean_and_split(text, delimiter) {
    var cleaned = [],
        pieces = text.split(delimiter || ',');

    for (var i = 0; i < pieces.length; i++) {
      if (pieces[i].match(/\w+/)) {
        cleaned.push(pieces[i].replace(/^\s+|\s+$/, ''));
      }
    }
    return cleaned;
  }

  function get_last_piece(text) {
    var cleaned = clean_and_split(text, ',');
    if (cleaned.length > 0) {
      var last = cleaned[cleaned.length - 1];
      if (last.match(/\w+/))
        return last;
    }
  }



  S.TagCompletion = TagCompletion;

})(Snippets, jQuery);
