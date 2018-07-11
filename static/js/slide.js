$(function(){
	var $slides = $('.slide_pics li');
	var len = $slides.length;
	var nowli = 0;
	var prevli = 0;
	var $prev = $('.prev');
	var $next = $('.next');
	var ismove = false;
	var timer = null;
	$slides.not(':first').css({left:760});
	$slides.each(function(index, el) {
		var $li = $('<li>');

		if(index==0)
		{
			$li.addClass('active');
		}

		$li.appendTo($('.points'));
	});
	$points = $('.points li');
	timer = setInterval(autoplay,4000);

	$('.slide').mouseenter(function() {
		clearInterval(timer);
	});

	$('.slide').mouseleave(function() {
		timer = setInterval(autoplay,4000);
	});

	function autoplay(){
		nowli++;
		move();
		$points.eq(nowli).addClass('active').siblings().removeClass('active');
	}

	$points.click(function(event) {
		if(ismove)
		{
			return;
		}
		nowli = $(this).index();

		if(nowli==prevli)
		{
			return;
		}
		
		$(this).addClass('active').siblings().removeClass('active');
		move();

	});

	$prev.click(function() {
		if(ismove)
		{
			return;
		}		
		nowli--;
		move();
		$points.eq(nowli).addClass('active').siblings().removeClass('active');

	});
	
	$next.click(function() {
		if(ismove)
		{
			return;
		}		
		nowli++;
		move();
		$points.eq(nowli).addClass('active').siblings().removeClass('active');

	});


	function move(){

		ismove = true;

		if(nowli<0)
		{
			nowli=len-1;
			prevli = 0;
			$slides.eq(nowli).css({left:-760});
			$slides.eq(nowli).animate({left:0},800,'easeOutExpo');
			$slides.eq(prevli).animate({left:760},800,'easeOutExpo',function(){
				ismove = false;
			});
			prevli=nowli;
			return;
		}

		if(nowli>len-1)
		{
			nowli = 0;
			prevli = len-1;
			$slides.eq(nowli).css({left:760});
			$slides.eq(nowli).animate({left:0},800,'easeOutExpo');
			$slides.eq(prevli).animate({left:-760},800,'easeOutExpo',function(){
				ismove = false;
			});
			prevli=nowli;
			return;
		}


		if(prevli<nowli)
		{
			$slides.eq(nowli).css({left:760});			
			$slides.eq(prevli).animate({left:-760},800,'easeOutExpo');
			$slides.eq(nowli).animate({left:0},800,'easeOutExpo',function(){
				ismove = false;
			});
			prevli=nowli;
			
		}
		else
		{			
			$slides.eq(nowli).css({left:-760});			
			$slides.eq(prevli).animate({left:760},800,'easeOutExpo');	
			$slides.eq(nowli).animate({left:0},800,'easeOutExpo',function(){
				ismove = false;
			});
			prevli=nowli;		
		}

	}
	// 登录信息显示
	if($('.login_info').next().val()>0){
		$('.login_info').display = display
	}
	$('#user_info').click(function () {
		$('#user_order').removeClass('active');
		$('#user_site').removeClass('active');
		$('#user_info').addClass('active');
		$('#user_chg_pwd').removeClass('active');
    });
	$('#user_order').click(function () {
		$('#user_order').addClass('active');
		$('#user_site').removeClass('active');
		$('#user_info').removeClass('active');
		$('#user_chg_pwd').removeClass('active');

    });
	$('#user_site').click(function () {
		$('#user_order').removeClass('active');
		$('#user_info').removeClass('active');
		$('#user_site').addClass('active');
		$('#user_chg_pwd').removeClass('active');
    });
	$('#user_chg_pwd').click(function () {
		$('#user_order').removeClass('active');
		$('#user_info').removeClass('active');
		$('#user_site').removeClass('active');
		$('#user_chg_pwd').addClass('active');
    });
	// 添加购物车1
	$('.add_goods').click(function () {
		var $goodsid = $(this).attr('id');
		var $count = 1;
		console.log($goodsid,$count);
		$.ajax({
			url:'/cart/add_cart/'+$goodsid + '/' +$count,
			type :'GET',
			success:function (response) {
                // console.log(response)
				alert(response)
            },
            error:function () {
				alert('添加失败，请查看是否等陆')
            }
		})
    });
	// 添加购物车2
	$('#add_cart').click(function () {
		var $goodsid = $(this).attr('goodid');
		var $count = $('.num_show').val();
		console.log($goodsid,$count);
		$.ajax({
			url:'/cart/add_cart/'+$goodsid + '/' +$count,
			type :'GET',
			success:function (response) {
                // console.log(response)
				alert(response)
            },
            error:function () {
				alert('添加失败，请查看是否等陆')
            }
		});
    });
	//商品详细页面动态显示小计
	function sub() {
		var $count = $('.num_show').val();
		var $price = $('.show_pirze').text().split(' ');
		var $subtotal = parseFloat($count) * parseFloat($price[1]);
		// console.log($count);
		// console.log($price[1]);
		// console.log($subtotal);
		$('.totalem').text($subtotal.toFixed(2)+'元')
    }
	// 数字修改
	$('.add').click(function () {
		var num =  $(this).parent().children(':input').val();
		num++;
		 $(this).parent().children(':input').val(num);
		 sub();
		 var date = $(this).next().attr('id');
		 // console.log(date);
		if(date != undefined){
			cart_change(date);
		}


    });
	$('.minus').click(function () {
		var num =   $(this).parent().children(':input').val();
		if (num>1){
			num--;
		}
		else {
			num = 1
		}
		 $(this).parent().children(':input').val(num);
		sub();
		 var date = $(this).prev().attr('id');
		 // console.log(date);
		 if(date != undefined){
			cart_change(date);
		}

    });
	$('.num_show').blur(function () {
		sub();
    });
	//计算总计的方法
	function total() {
		var total1 = 0;
        var total_count = 0;
        $(":checked:not(#check_all)").each(function () {
            obj = $(this).parent().parent().children('.col07');
            //获取小计数量
            subtotal = obj.text();
            // console.log(subtotal);
            //计算总计
            total1 += parseFloat(subtotal);
            total_count += 1;
            // console.log(total_count);
        });
		$('#total').text(total1.toFixed(2));
		$('#total').next().val(total1.toFixed(2));
		$('#total_count').text(total_count);
		$('#total_count').next().val(total_count);
    }
     total();
	//全选全消
	$('#check_all').click(function () {
		state = $(this).prop('checked');
		//
		$(':checkbox:not(#check_all)').prop('checked', state);
		total();
	});

	//选择购物车条目
	$(':checkbox:not(#check_all)').click(function () {
		if ($(this).prop('checked')) {
			if ($(':checked').length + 1 == $(':checkbox').length) {
				$('#check_all').prop('checked', true);
			}
		} else {
			$('#check_all').prop('checked', false);
		}
		total();
	});

	//删除购物车条目
	$('.col08').click(function () {
		del = confirm('确定要删除吗？');
		if (del) {
			cart_id = $(this).next().val();
			$.ajax({
				url:'/cart/cart_del/'+cart_id + '/',
				type :'GET',
				success:function (data) {
					if(data.status == 'ok')
						if (data.count == '0') {
							$('#gods_item_' + cart_id).remove();
						}
						else {
							obj = $('#gods_item_' + cart_id);
							// console.log(data.count);
 							$('#'+cart_id).val(data.count);
 							// console.log($('#'+cart_id).val());
							obj.children('.col07').text(data.subtotal.toFixed(2)+'元');
							// console.log($('#gods_item_' + cart_id).children('.col07').text());
							// console.log(obj.children('.col06').children('.num_add').children(':input').val());
							// console.log(data.count);
						}
						total();
						alert('删除成功');
				},
				error:function () {
					console.log('请求失败');
					total();
				}
			})
		}
	});

	// 修改购物车条目
	function cart_change(date) {
		obj =  $('#gods_item_'+date);
		count = obj.children('.col06').children('.num_add').children('.cart_chg').val();
		// console.log(count);
		// console.log(date);
		$.ajax({
			url:'/cart/cart_chg/'+date + '/'+count+'/',
			type :'GET',
			success:function (data) {
				if(data.status == 'ok')
					if (data.count == '0') {
						$('#gods_item_' + date).remove();
					}
					else {
						obj.children('.co106').children('.num_add').children(':input').val(data.count);
						obj.children('.col07').text(data.subtotal.toFixed(2)+'元');
						// console.log(obj.children('.col07').text());
						// console.log(obj.children('.col06').children('.num_add').children(':input').val());
						// console.log(data.count);
					}
					total();
					alert('修改成功');
			},
			error:function () {
				console.log('修改失败');
				total();
			}
		})
    }
	$('.cart_chg').blur(function () {
		date = $(this).attr('id');
		// console.log(date);
		cart_change(date);
	});

	//删除地址
	$('.del_address').click(function () {
		address_id = $(this).parent().attr('id');
		$.ajax({
			url:'/user/del_address/'+address_id + '/',
			type :'GET',
			success:function (date) {
               if(date.status == 'ok'){
               		$('#' + address_id).remove();
			   }
			   alert('删除成功')
            },
            error:function () {
				alert('删除失败')
            }
		});

    });

	//购物车提交结算
	// $('#cart_account').click(function () {
	// 	var cartinfo_list = '';
	// 	$(":checked:not(#check_all)").each(function () {
     //        cartinfo = $(this).parent().parent().children('.col06').children('.num_add').children('.num_show').attr('id');
	// 		// console.log(cartinfo);
	// 		cartinfo_list = cartinfo_list + '|'+ cartinfo;
     //    });
	// 	// console.log(cartinfo_list);
	// 	$.ajax({
	// 		url:'/myorder/place_order/'+cartinfo_list + '/',
	// 		type :'GET',
	// 		success:function (data) {
	// 			if(data.status == 'ok')
	// 				if (data.count == '0') {
	// 					$('#gods_item_' + date).remove();
	// 				}
	// 				else {
	// 					obj.children('.co106').children('.num_add').children(':input').val(data.count);
	// 					obj.children('.col07').text(data.subtotal.toFixed(2)+'元');
	// 					// console.log(obj.children('.col07').text());
	// 					// console.log(obj.children('.col06').children('.num_add').children(':input').val());
	// 					// console.log(data.count);
	// 				}
	// 				alert('提交成功');
	// 		},
	// 		error:function () {
	// 			console.log('提交失败');
	// 		}
	// 	})
    // })
});