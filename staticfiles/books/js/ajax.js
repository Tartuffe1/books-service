//My JavaScript Document
$(function(){
       $('#search').keyup(function() {
           
           $.ajax({
              type:'POST',
              url:'/books/search/',
              data: {
                 'search_text': $('#search').val(),
                 'csrfmiddlewaretoken' : $('input[name=csrfmiddlewaretoken]').val(),
              },
              success: searchSuccess,
              dataType: 'html'
           });
       });
    });
    
    function searchSuccess(data, textStatus,jqXHR) {
       
       $('#content_layer').html(data);
    
    }
