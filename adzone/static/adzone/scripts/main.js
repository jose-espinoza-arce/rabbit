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
