api = "http://127.0.0.1:5000"
$(document).ready(function(){
  $.ajax({
    url: api,
    type: "GET",
    success: function(result)
      {
        console.log(result)
      }
    });
});