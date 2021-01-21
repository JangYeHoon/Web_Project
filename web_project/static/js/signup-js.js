$('#signUp').click(function(){
    if($('#contact_email').attr("check_result")=="fail"){
        alert("아이디 중복체크를 해주세요")
        $('#contact_email').focus();
        return false;
    }

})
$('#id_overlap_check').click(function(){               
    $('#contact_email').change(function(){
        $('#id_check_sucess').hide();
        $('#id_overlap_check').show();
        $('#contct_email').attr("check_result","fail");
    })

    if($('#contact_email').val() == ""){
        alert('이메일을 입력해주세요')
        return;
    }

    id_overlap_input = document.querySelector('input[name="email"]')
    
     $.ajax({
         url:'id_overlap_check',
         data : {
             'email': id_overlap_input.value
         },
         datatype : 'json',
         success:function(data){

             if(data['overlap'] == "fail"){
                 alert("이미 존재하는 이메일 입니다.");
                 id_overlap_input.focus();
                 return;
             }else{
                 alert("사용가능한 이메일입니다.");
                 $('#contact_email').attr("check_result","success");
                 $('#id_check_sucess').show();
                $('#id_overlap_check').hide();
                return;
             }
         }
     })
})




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

    // Control video
    $('.tm-btn-play').click(function() {
        togglePlayPause();                                      
    });

    $('.tm-btn-pause').click(function() {
        togglePlayPause();                                      
    });

    // Update the current year in copyright
    $('.tm-current-year').text(new Date().getFullYear());                           
});

function check_pw() {
    let pw = document.getElementById('contact_pw').value;
    const SC = /[~!@#$%^&*]/;
    const num = /[0-9]/;
    const eng = /[a-zA-Z]/;

    if (pw.length < 8)
    {
        window.alert('비밀번호는 8글자 이상 입력해야 합니다.');
        document.getElementById('contact_pw').value = '';
    }
    else if (!num.test(pw) || !eng.test(pw) || !SC.test(pw))
    {
        window.alert('비밀번호는 숫자, 영어, 특수문자 조합으로 만들어야 합니다.');
        document.getElementById('contact_pw').value = '';
    }
}

let autoHypenPhone = function(str){
    str = str.replace(/[^0-9]/g, '');
    let tmp = '';
    if( str.length < 4){
        return str;
    }else if(str.length < 7){
        tmp += str.substr(0, 3);
        tmp += '-';
        tmp += str.substr(3);
        return tmp;
    }else if(str.length < 11){
        tmp += str.substr(0, 3);
        tmp += '-';
        tmp += str.substr(3, 3);
        tmp += '-';
        tmp += str.substr(6);
        return tmp;
    }else{              
        tmp += str.substr(0, 3);
        tmp += '-';
        tmp += str.substr(3, 4);
        tmp += '-';
        tmp += str.substr(7);
        return tmp;
    }

    return str;
}
var phoneNum = document.getElementById('contact_phone');

phoneNum.onkeyup = function(){
    console.log(this.value);
    this.value = autoHypenPhone( this.value ) ;  
}