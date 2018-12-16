$(document).ready(function(){
    //'what I do' icons at the landing page
    $("div.what div, div.text-wrapper a").on({
        mouseenter: function () {
            $(this).animate({'color': '#e3e0cf'}, 'fast');
            $(this).find('p').animate({'color': '#86A5BA'}, 'fast');
            $(this).find('i').animate({'color': '#86A5BA'}, 'fast');
        },
        mouseleave: function () {
            $(this).animate({'color': '#86A5BA'}, 'fast');
            $(this).find('p').animate({'color': '#9fa8a3'}, 'fast');
            $(this).find('i').animate({'color': '#9fa8a3'}, 'fast');
        }
    });

    //social icons:
    $("div.social i").on({
        mouseenter: function () {
            $(this).animate({'color': '#86A5BA'}, 'fast');
        },
        mouseleave: function () {
            $(this).animate({'color': '#d6d6d6'}, 'fast');
        }
    });

    //contact button at the landing page:
    $("button.contact-button").on({
        mouseenter: function () {
            $(this).animate({'background-color': '#86A5BA'}, 'fast');
        },
        mouseleave: function () {
            $(this).animate({'background-color': '#e3e0cf'}, 'fast');
        }
    });

    //links at the top navbar:
    $("nav.top-header li a, nav.top-header i").on({
        mouseenter: function () {
            $(this).animate({'color': '#85C7BE'}, 'fast');
        },
        mouseleave: function () {
            $(this).animate({'color': '#86A5BA'}, 'fast');
        }
    });

    //blog post list:
    $("div.blog-posts a").on({
        mouseenter: function () {
            $(this).animate({'color': '#4890A8'}, 'fast');
        },
        mouseleave: function () {
            $(this).animate({'color': '#90C0D8'}, 'fast');
        }
    });

    //initialize Bootstrap tooltips:
    $(function () {
      $('[data-toggle="tooltip"]').tooltip()
    })

    //contact form
    $('span.form-errors').fadeOut('fast');

    $('form.hello').submit(function(e){
      e.preventDefault();
      var form = $(this);
      $('span.form-errors').fadeOut('fast');

      var submit_button = $('button.contact-button')
      submit_button.blur() // clear focus

      $.ajax({
          data: form.serialize(),
          type: form.attr('method'),
          url: form.attr('action'),
          success: function(response) {
              response = jQuery.parseJSON(response)
              if (response.success) {
                submit_button.html('Thanks! <i class="fa fa-star"></i>');
                form.find('input, textarea').attr('disabled', 'disabled');
                submit_button.attr('disabled', 'disabled');
              } else {
                $.each(response, function(field, error) {
                  $('span.form-errors.' + field)
                    .fadeIn('fast')
                    .text(error)
                });
              }
          }
      });

    })

    // Instagram feed:
    var elem = document.querySelector('.m-p-g');
    var gallery = new MaterialPhotoGallery(elem);

})


