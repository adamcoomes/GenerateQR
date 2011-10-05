$(document).ready(function() {
	$("#qr_form").submit(function() {
		$("#qrsubmit").attr("disabled", "disabled");
		if ($("#qrcode").val() == $("#qrlast").val()) {
			if ($(".alert-message").hasClass("error")) {
				$("#qrsubmit").removeAttr("disabled");
				return false;
			}

			$(".alert-message").removeClass("success").addClass("error");
			$(".alert-message > p").html("<strong>Sorry!</strong> You just created that QR Code!");
			$(".alert-message").fadeIn().alert().delay(5000).fadeOut(); 
			$("#qrsubmit").removeAttr("disabled");
			return false;
		}

		$("#qrlast").val($("#qrcode").val());
			
		$("<div>").load("/", { 'q' : encodeURI($("#qrcode").val()), 'name' : encodeURI($("#qrname").val()) }, function() {
      		$("#qr_row").prepend($(this).html());
      		/*
    		$("a.copyLink").zclip({
        		path: "http://zeroclipboard.googlecode.com/svn-history/r10/trunk/ZeroClipboard.swf",
        		copy: function(){
   					return "hi";
    			}
    		});
    		*/
	      	$("#qr:hidden").fadeIn();
	      	var bgcolor = $("#qr_row tr:hidden>td:first").css('background-color');
	      	$("#qr_row tr:hidden>td").css('background-color', '#fef9ad');
	      	$("#qr_row tr:hidden").fadeIn();
	      	$("#qr_row tr:first>td").delay(2000).queue(function() {
	      		$(this).css('background-color', bgcolor);
			});
		});
		
		$("#qrsubmit").removeAttr("disabled");
		return false;
	});
	
	$("#examples-trigger").click(function() {
		if ($("#examples").is(":animated")) {
			return false;
		}

		$("#examples").slideToggle();
	});
});