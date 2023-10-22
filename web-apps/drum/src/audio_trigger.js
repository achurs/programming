$(document).ready(function(){
    const drumpads = document.querySelectorAll('.drum-pad');
    drumpads.forEach((drum) => {
        drum.addEventListener('click', () => {
            $("#display").text(drum.id);
            $(drum).children("audio").get(0).play();
        })
        drum.addEventListener('keydown', (event) => {
            if(event.key == drum.id){
                $("#display").text(drum.id);
                $(drum).children("audio").get(0).play();
            }
        });
    })
})