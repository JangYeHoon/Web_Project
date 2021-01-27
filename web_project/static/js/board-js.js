function setPageNav(){
    if($(window).width() > 991) {
        $('#tm-top-bar').singlePageNav({
            currentClass:'active',
            offset: 79
        });   
    }
    else {
        $('#tm-top-bar').singlePageNav({
            currentClass:'active',
            offset: 65
        });   
    }
}

$(document).ready(function(){

    $(window).on("scroll", function() {
        if($(window).scrollTop() > 100) {
            $(".tm-top-bar").addClass("active");
            $(".login").addClass("active");
        } else {
            //remove the background property so it comes transparent again (defined in your css)
           $(".tm-top-bar").removeClass("active");
           $(".login").removeClass("active");
        }
    });      

  
    $(window).resize(function() {
      setCarousel();
      setPageNav();
    });

    // Close navbar after clicked
    $('.nav-link').click(function(){
        $('#mainNav').removeClass('show');
    });


    // Update the current year in copyright
    $('.tm-current-year').text(new Date().getFullYear());                           
   
    //a태그로 post 보내기
    formSubmit = function(board_id){  
        document.getElementById("board_id").value =board_id;
        document.board.submit();
    }

    boardContentsMD = function(route){
        var form =document.board_contents_md;
        if(route == "del"){
            form.action = "board_delete";
        }else if( route == "mod"){
            form.action = "board_modify_input";
        } else if (route == "reply") {
            form.action = "board_input";
        }
        form.submit();
    }
});