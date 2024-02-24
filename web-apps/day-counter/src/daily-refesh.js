console.log("Hello, World!");
const time = 24 * 60 * 60 * 1000;
$(document).ready(function(){
    $("#date-button").click(function(){
        window.location.reload();
    })
})
setInterval(function () {
    //window reload
    window.location.reload();
},time)