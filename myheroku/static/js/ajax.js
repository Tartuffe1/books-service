// JavaScript Document
$(document).ready(function(){
    // Uveo sam klase logged i not_logged u template-u(u ovisnosti o user.is_authenticated) da bih 
    // mogao ograniciti upotrebu click dogadjaja
    $("a.not_logged").click(function(){
          alert('Morate biti prijavljeni ako želite predati oglas!');
    });

    $('#searchbutton').click(function() {
       
       $.ajax({
          type:'POST',
          url:'/books/search/',
          data: {
             'search_text': $('#searchbar').val(),
             'csrfmiddlewaretoken' : $('input[name=csrfmiddlewaretoken]').val(),
          },
          success: searchSuccess,
          dataType: 'html'
       });
    });
    
    function searchSuccess(data, textStatus,jqXHR) {
       
       $('.container .col-md-9 .row').html(data);
    
    }
});