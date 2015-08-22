var Header = (function(){

  var h = {
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

        console.log('offsetLeft', offsetLeft);

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

  return h.init();
})();



// Autor: Jose

var $container = $(".container");


$(function () {
    $container.imagesLoaded(function () {
        console.log('en el imageslodwed');
        $container.masonry({
            itemSelector : '.brick',
            gutter: 50,
            //columnWidth: 50
            /* function () {
                var screenWidth = parseInt(
                    document.documentElement.getBoundingClientRect().width,
                    10
                ) || parseInt(screen.width, 10);

                if (screenWidth < 768) {
                    return $container.width();
                } else if (screenWidth > 768 && screenWidth < 980) {
                    return ($container.width() / 2) - 20;
                }
                console.log($container.width());
                return ($container.width() / 3) - 20;
            }*/
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
                img: "http://pathtoyour.com/loading.gif",
                msg: null,
                msgText: ""
            },
            debug: true,
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