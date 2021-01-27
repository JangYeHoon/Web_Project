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
function loginStateCheck(){
    $.ajax({
        url:'loginStateCheck',
        datatype: 'json',
        success:function(data){
           str = data["state"]+"";
           if (str == "login"){
                return $('#comment_add').submit();
            }else{
                alert("로그인이 필요합니다")
                return false;
            }
        }
    })
}
function addCheck()
{
    if (document.getElementById('board_name').value == '0')
    {
        window.alert("말머리 입력 필수");
        return false;
    }
    else if (document.getElementById('title').value == '')
    {
        window.alert("제목 입력 필수");
        return false;
    }
    else if (document.getElementById('contents').value == '')
    {
        window.alert("내용 입력 필수");
        return false;
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

    recommentBoxOpen = function(commentId,boardId){
        $.ajax({
            url:'loginStateCheck',
            datatype: 'json',
            success:function(data){
               str = data["state"]+"";
               if (str == "login"){
                var commentBox = "<input type='hidden' id='board_id' name='board_id' value='"+boardId+"'></input>";
                    commentBox += "<input type='hidden' id='c_list' name='c_list' value='"+commentId+"'></input>";
                    commentBox += "<input type='hidden' id='c_level' name='c_level' value='1'></input>";
                    commentBox += "<textarea class='form-control' id='comment_contents' name='comment_contents' rows='2' placeholder='What are you thinking?'>";
                    commentBox += "</textarea>";
                    commentBox += "<div class='mar-top clearfix'>";
                    commentBox += " <button class='btn btn-sm btn-primary pull-right' type='submit'>";
                    commentBox += " <i class='fa fa-pencil fa-fw'></i> 등록</button>";
                    commentBox += " </div>";
                   
                document.getElementById("recomment-box-"+commentId).innerHTML=commentBox;
                }else{
                    alert("로그인이 필요합니다")
                }
            }
        })
       

    }
});

