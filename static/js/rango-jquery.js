$(document).ready(function() {
      // JQuery code to be added in here.
      $("#about-btn").click( function(event) {
          alert("You clicked the button using JQuery!");
          $("#about-btn").removeClass('btn-primary').addClass('btn-success');
      });

      // $('p').hover( function(){
      //       $(this).css('color', 'red')
      // },
      // function() {
      //       $(this).css('color', 'black')
      // });

      $("#about-btn").click( function(event) {
            msgstr = $("#msg").html()
            msgstr = msgstr + "ooo"
            $("#msg").html(msgstr)
      });

      $('.rango-add').click(function(){
          var catid = $(this).attr("data-catid");
          var url = $(this).attr("data-url");
          var title = $(this).attr("data-title");
          var me = $(this)
          $.get('/rango/add/', {category_id: catid, url: url, title: title}, function(data){
              $('#pages').html(data);
              me.hide();
          });
      });

});
