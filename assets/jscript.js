


var erp = {
	ur:{
		content_form:"http://127.0.0.1:8000/cml/content_form",
		ip:"https://api.ipify.org?format=json",
	},
	o: {}, // initial object
	btn:{},
	ini: function(){ //initiate required script for page
		a=this;
		a.jax("json",{},"get",a.ur.ip,function(e){a.o.ip=e.ip; console.log("Device IP : "+e.ip);},function(e){});	
		a.jax("json",{},"get",a.ur.content_form,
				
				function(e){
					
					//var d = JSON.parse(e.response)
					
					$("#editor_figgup").html(e.html)
					
					},
				function(e){
					
					console.log(e.responseText);
					$("#editor_figgup").html(e.html)
				}
					);
	},
   

    firstResponse: function (a,b,c,d,e,msg,f,t=this) { // render the first response to the app about features.
	
		f(a,b,c,d,e,t);
		console.log(msg);
    },
	myObject:function(a,msg,f,t=this){
			
		f(a,t);
		//console.log(msg,"// Hide me in deployment //");
	},
	jax:function(t,d,m,u,rfn,efn){
		$.ajax({
			dataType:t,
			data:d,
			method:m,
			url:u,
			processData: false,
			contentType: false,
			success: function(e){return rfn(e)},
			error:function(e){return efn(e)} 
			})
		},
	html:function(par,d,cond){
		par.html(d);
	
		
		
		
	},
	append:function(par,d,cond){
		console.log(d,par);
		par.append(d);
		
		
	},
	pop:function(d,p,fnopen,fnclose){
			
			fnopen(p);
			fnclose(p);
			
	},
	formValidate:function(a,b,msg,fn,t=this){
		fn(a,b,t);
	},
	formPop:function(el,b,msg){
		var f = el.find("form");
		f.each(function(){
			fld = $(this).find("input,select,textarea,radio")
			fld.each(function(){
				if((this.tagName== "INPUT") && (this.value != this.defaultValue)) alert("#name has changed");
			});
			console.log(fld)
		});
		
	},	
	kill:function(e){
		e.remove();
	},
	del:function(e){
		e={}
	},
	jxerr:function(e,p){
		var err = function(e){
			switch(e.status){
				case 0: return {code:"ERR_0 NET_CONNECTION_ERR",text:"Internet connection is lost."};
					break;
				case 403: return {code:"ERR_403 ACCESS_FORBIDDEN",text:"This is an unauthorized request or something is missing."};
					break;
				case 404: return {code:"ERR_404 REQST_NOT_FOUND",text:"This request is unavailable right now."};
					break;
				case 500: return {code:"ERR_500 INTERNAL_ERROR",text:"Something is wrong with server."};
					break;
				case 503: return {code:"ERR_503 SERVICE_ERROR",text:"This services is unavailable."};
					break;
				default: return {code:"Unknown ERROR",text:"There was an error. Please try again."};
1			}
		}
		var eo = err(e)
		this.html(p,'<div class="errcd1">'+ eo.code +"! "+ eo.text +'</div>')
	},
	
	tableFilter(s,filter,msgBefore,msg){
		var el = $('<div class="gomsg">'+msg+'</div>')
		
		s.on("keyup", function() {
			//console.log(new Date().getTime());
			var value = $(this).val().toLowerCase(), allhidden=true;
			filter.find('tr').filter(function(i) {
			  $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
			})
			filter.find('tr').each(function(e){
				if(this.style.display != "none" ) {allhidden=false}
				
				
				
			});
			
			
			if(allhidden){
				el.insertAfter(msgBefore)
			}
			else{
				el.remove();	
			}
			//console.log(new Date().getTime());
		  });
	},
	tpl:{
		
		l:'<div class="loader"></div>'
		
	}
	
	
};

$(document).ready(function(){
	
erp.firstResponse("csrftoken","userid","userhash",new Date(),window.navigator,"ERP Initialized...",function(a,b,c,d,e,t){t.o={a:a,b:b,c:c,d:d,e:e};});
erp.ini();
erp.myObject({"a":"b"},'Emp code object created ...',function(a,t){t.o.emp_code_status=a});
erp.myObject({},'Testing ...',function(a,t){t.o.testObject=a});
erp.myObject($("#dep-sel"),'Button Code s1',function(b,t){	
														t.btn.s1=b;
														t.btn.s1.on('change',function(e){
														$("#id_Department").val($("#dep-sel").val())
														}).trigger("change");
													
													});
												
												
												
									






});



/**  

In MEthODS /funtions/

**/

function logError(){
	
	var v=$("input[name='next']").val();
	console.log(v,"<---");
	if(v!=''){
		var pop1 = $("#username_pop");
		$(".inhead_logger_input").css({'border-color':'red'});
		pop1.children(".msg").html("You need to login first!")
		pop1.show();
		pop1.on("mouseout",function(){ pop1.fadeOut(1000);})
		setInterval(function(){ pop1.fadeOut(1000);}, 10000);
		
		
	}
	
}


