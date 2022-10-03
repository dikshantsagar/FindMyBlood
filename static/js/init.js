

   


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


      
        setTimeout(function() {
            $('#main').attr("hidden",false);
            $('#loader').attr("hidden",true); // Do something after 5 seconds
       }, 500);


    

  
      
  
    }); // end of document ready
  
  })(jQuery); // end of jQuery name space
  
  
function validateForm(){
    
  }
  
  
  