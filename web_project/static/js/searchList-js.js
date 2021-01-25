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

    //날짜 재검색 부분
    $('#selectedDate').hide();

    $('#dateIcon').click(function(){
        $('#selectedDate').show();
        $('#selectedDate').focus();
    })

   $('#selectedDate').datepicker({
       dateFormat:"yy-mm-dd",
       onSelect:function(dateText,inst){
           $('#departure_data').val(dateText);
           $('#selectedDate').hide();
            $('#research').submit();
       }
   });

   $('#selectedDate').blur(function(){
       $('#selectedDate').hide();
   })

});