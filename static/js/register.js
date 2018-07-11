$(function(){
	var error_name = false;
	var error_password = false;
	var error_check_password = false;
	var error_email = false;
	var error_phone = false;
	var error_check = false;


	$('#username').blur(function() {
		check_username();
	});

	$('#pwd').blur(function() {
		check_pwd();
	});
	$('#opwd').blur(function() {
		check_opwd()
	});

	$('#cpwd').blur(function() {
		check_cpwd();
	});

	$('#email').blur(function() {
		check_email();
	});
	$('#phone').blur(function() {
		check_phone();
	});

	$('#allow').click(function() {
		if($(this).is(':checked'))
		{
			error_check = false;
			$(this).siblings('span').hide();
		}
		else
		{
			error_check = true;
			$(this).siblings('span').html('请勾选同意');
			$(this).siblings('span').show();
		}
	});


	function check_username(){
		var len = $('#username').val().length;
		if(len<5||len>20)
		{
			$('#username').next().html('请输入5-20个字符的用户名');
			$('#username').next().show();
			error_name = true;
		}
		else
		{
			$('#username').next().hide();
			error_name = false;
		}
	}

	function check_phone(){
		var len = $('#phone').val().length;
		if(len!=11)
		{
			$('#phone').next().html('电话号码为11位');
			$('#phone').next().show();
			error_phone = true;
		}
		else
		{
			$('#phone').next().hide();
			error_phone = false;
		}
	}

	function check_pwd(){
		var len = $('#pwd').val().length;
		if(len<8||len>20)
		{
			$('#pwd').next().html('密码最少8位，最长20位');
			$('#pwd').next().show();
			error_password = true;
		}
		else
		{
			$('#pwd').next().hide();
			error_password = false;
		}		
	}

	function check_opwd(){
		var len = $('#opwd').val().length;
		if(len<8||len>20)
		{
			$('#opwd').next().html('密码最少8位，最长20位');
			$('#opwd').next().show();
			error_password = true;
		}
		else
		{
			$('#pwd').next().hide();
			error_password = false;
		}
	}


	function check_cpwd(){
		var pass = $('#pwd').val();
		var cpass = $('#cpwd').val();

		if(pass!=cpass)
		{
			$('#cpwd').next().html('两次输入的密码不一致');
			$('#cpwd').next().show();
			error_check_password = true;
		}
		else
		{
			$('#cpwd').next().hide();
			error_check_password = false;
		}		
		
	}

	function check_email(){
		var re = /^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$/;

		if(re.test($('#email').val()))
		{
			$('#email').next().hide();
			error_email = false;
		}
		else
		{
			$('#email').next().html('你输入的邮箱格式不正确');
			$('#email').next().show();
			error_check_password = true;
		}

	}


	$('#reg_form').submit(function() {
		check_user_name();
		check_pwd();
		check_cpwd();
		check_email();
		check_phone();

		if(error_name == false && error_password == false && error_check_password == false && error_email == false && error_check == false && error_phone == false )
		{
			return true;
		}
		else
		{
			return false;
		}

	});
	if($('#flag').val()=='0'){
        alert('注册失败')
    }
    if($('#flag').val()=='1'){
        alert('注册成功，进入登录页面')
    }








});