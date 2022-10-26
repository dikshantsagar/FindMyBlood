

   


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



       $('#nextButton').click(function(){
        $('#nextButton').attr("hidden",true);
        $('#info').attr("hidden",true);
        $('#ques').attr("hidden",false);
        $('#backButton').attr("hidden",false);
        $('#submit').attr("hidden",false);
       });

       $('#backButton').click(function(){
        $('#nextButton').attr("hidden",false);
        $('#info').attr("hidden",false);
        $('#ques').attr("hidden",true);
        $('#backButton').attr("hidden",true);
        $('#submit').attr("hidden",true);
       });
       
       
  
      
  
    }); // end of document ready
  
  })(jQuery); // end of jQuery name space
  
  

  
  
  