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
      this.trigger = $('.detail a.action-button');
      this.phone = $('.detail a.simple-button');

      this.back = $('.detail a.detail__back');
    },
    bind: function() {

      var self = this;

      this.trigger.on('click', function (ev) {
        ev.preventDefault();
        var url = $(this).attr('href');
        $.get(url, function(response) {
          var markup = $.parseHTML(response);
          var form = null;
          $.each(markup, function (i, el) {
            if ($(el).hasClass('main-form')) {
              form = $(el);
              return
            };
          });

          self.el.find('.detail__form').append(form);
        });
        self.openForm();
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
                img: "/static/adzone/images/roof-loader.gif",
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
    /*$container.infinitescroll('unbind');
    $('#next').on('click', function(e) {
        e.preventDefault();
        $container.infinitescroll('retrieve');
    });*/
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