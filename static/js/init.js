

   


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
       
<<<<<<< HEAD
       UIkit.upload('.js-upload', {

        url: '/upload',
        mime: "image/*",
        


        beforeSend: function (environment) {
            console.log('beforeSend', arguments);

            // The environment object can still be modified here.
            // var {data, method, headers, xhr, responseType} = environment;

        },
        beforeAll: function () {
            console.log('beforeAll', arguments);
        },
        load: function () {
            console.log('load', arguments);
        },
        error: function () {
            console.log('error', arguments);
        },
        complete: function () {
            console.log('complete', arguments);
        },

        loadStart: function (e) {
            console.log('loadStart', arguments);

            bar.removeAttribute('hidden');
            bar.max = e.total;
            bar.value = e.loaded;
        },

        progress: function (e) {
            console.log('progress', arguments);

            bar.max = e.total;
            bar.value = e.loaded;
        },

        loadEnd: function (e) {
            console.log('loadEnd', arguments);

            bar.max = e.total;
            bar.value = e.loaded;
        },

        completeAll: function () {
            console.log('completeAll', arguments);
              var uid = $('#uid').val();
              console.log('static/uploads/'+uid+'.png');
            $('.pic').attr('src','static/uploads/'+uid+'.png');
            

            alert('Upload Completed');
        }

    });

=======
       
>>>>>>> 6f2dfae9675b4761fc6e62a5cfc0f06d8148784b
  
      
  
    }); // end of document ready
  
  })(jQuery); // end of jQuery name space
  
  

  
  
  