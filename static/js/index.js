/**
 * Created by Administrator on 2018/5/14.
 */
$(function () {
    var flag =$('.login_info').children().text();
    if(flag!='游客' && flag.length >0){
        $('.login_info').css('display','block');
        $('#login').css('display','none');
        $('#logout').css('display','block');
        $('#login').next().css('display','none');
        $('#register').css('display','none');
    }
});