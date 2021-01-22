function setCarousel(){
                    
    if ($('#tm-article-carousel').hasClass('slick-initialized')) {
        $('#tm-article-carousel').slick('destroy');
    } 

    if($(window).width() < 438){
        // Slick carousel
        $('#tm-article-carousel').slick({
            infinite: false,
            dots: true,
            slidesToShow: 1,
            slidesToScroll: 1
        });
    }else {
    $('#tm-article-carousel').slick({
            infinite: false,
            dots: true,
            slidesToShow: 3,
            slidesToScroll: 1
        });   
    }
}

function togglePlayPause() {
    vid = $('.tmVideo').get(0);

    if(vid.paused) {
        vid.play();
        $('.tm-btn-play').hide();
        $('.tm-btn-pause').show();
    }
    else {
        vid.pause();
        $('.tm-btn-play').show();
        $('.tm-btn-pause').hide();   
    }  
}

$(function(){

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
    
    // Slick carousel
    setCarousel();

    $(window).resize(function() {
    setCarousel();
   
    });

    // Close navbar after clicked
    $('.nav-link').click(function(){
        $('#mainNav').removeClass('show');
    });

    // Control video
    $('.tm-btn-play').click(function() {
        togglePlayPause();                                      
    });

    $('.tm-btn-pause').click(function() {
        togglePlayPause();                                      
    });

    // Update the current year in copyright
    $('.tm-current-year').text(new Date().getFullYear()); 

})



function searchCheck(){
   
   if(document.getElementById('departureCity').value == ""){
       window.alert("출발지 입력 필수")
       return false;
   }
   else if(document.getElementById('arrivalCity').value == ""){
       window.alert("도착지 입력 필수")
       return false;
   }
   else if(document.getElementById('departure_data').value == ""){
       window.alert("가는날짜 입력 필수")
       return false;
   }
   else if(document.getElementById('section').value == "round_trip" && document.getElementById('arrival_data').value == ""){
       alert("오는날짜")
       window.alert("오는 입력 필수")
       return false;
   }
   else if(document.getElementById('adult').value == "" && document.getElementById('children') == ""){
       window.alert("인원수 입력 필수")
       return false;
   }
   else if(document.getElementById('seat').value == ""){
       window.alert("좌석 입력 필수")
       return false;
   }
}