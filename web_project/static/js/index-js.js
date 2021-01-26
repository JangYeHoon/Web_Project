
function airlineSelected(self){
    airline_id = self;
    result = "";
    $.ajax({
        url:"specials_tickets",
        data:{
            'airline_id':airline_id
        },
        datatype : 'json',
        success:function(resultData){

            for(let i=0;i<resultData.length;i++){
                result +=" <article class='col-sm-6 col-md-4 col-lg-3 col-xl-3 tm-article'> ";
                result +="<h4 class='tm-color-primary tm-article-title-1'>" +resultData[i].departure_place+" -> " +resultData[i].arrival_place +"</h4>";
                result +="<p class='tm-article-content'>" +resultData[i].departure_data+"</p>";
                result +="<a href='#' class='text-uppercase tm-color-primary tm-font-semibold  tm-article-price'>최저가 : " +resultData[i].economy_price+ "원</a>";
                result += "<form action='air_app/searchList_go_get' method='get'>"
                result += "<input type='hidden' id='departure_place' name='departure_place' value=" + resultData[i].departure_place + "></input>"
                result += "<input type='hidden' id='arrival_place' name='arrival_place' value=" + resultData[i].arrival_place + "></input>"
                result += "<input type='hidden' id='departure_data' name='departure_data' value=" + resultData[i].departure_data + "></input>"
                result += "<input type='hidden' id='arrival_data' name='arrival_data' value=" + resultData[i].departure_data + "></input>"
                result += "<input type='hidden' id='adult' name='adult' value='1'></input>"
                result += "<input type='hidden' id='children' name='children' value=''></input>"
                result += "<input type='hidden' id='seat' name='seat' value='1'></input>"
                result += "<input type='hidden' id='section' name='section' value='one_way'></input>"
                result += "<button type='submit' class='text-uppercase btn-primary tm-btn-primary'>검색</a>"
                result += "</form>"
                result += " </article>";
            }
            
            $('#special_ticket').html(result);
            
        },
        error : function(){
            alert('ajax요청 실패');
        }

    })
}
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
    }else if(document.getElementById('arrivalCity').value == ""){
        window.alert("도착지 입력 필수")
        return false;
    }else if(document.getElementById('departure_data').value == ""){
        window.alert("가는날짜 입력 필수")
        return false;
     }else if(document.getElementById('adult').value == 0 && document.getElementById('children').value == 0){
         window.alert("인원수 입력 필수")
         return false;
     }
    else if(document.getElementById('section').value == "round_trip" && document.getElementById('arrival_data').value == ""){
        window.alert("오는날짜 입력 필수")
        return false;
    }
    else if(document.getElementById('seat').value == ""){
        window.alert("좌석 입력 필수")
        return false;
    }
 }
