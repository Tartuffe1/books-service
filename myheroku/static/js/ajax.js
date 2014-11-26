// JavaScript Document
$(function(){
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
    });
    
    function searchSuccess(data, textStatus,jqXHR) {
       
       $('.container .col-md-9 .row').html(data);
    
    }
