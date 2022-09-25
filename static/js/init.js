

   


(function($){
    $(function(){
  
        navigator.geolocation.getCurrentPosition((position) => {
            let lat = position.coords.latitude;
            let long = position.coords.longitude;
            
            $('#lat').val(lat);
            $('#long').val(long);
            console.log(lat);
            console.log(long);
          });


    

  
      
  
    }); // end of document ready
  
  })(jQuery); // end of jQuery name space
  
  
function validateForm(){
    
  }
  
  
  