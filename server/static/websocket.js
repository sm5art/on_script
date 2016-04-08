var source = {};
function WebSocketTest()
{
   var ws = new WebSocket("ws://localhost:8888/socket");
				
   ws.onopen = function()
   {
                
   };
				
   ws.onmessage = function (evt) 
   {
         var received_msg = evt.data;
         populate(received_msg);
         btnclick();
      };
				
   ws.onclose = function()
   { 
                  
               
   };
            
         
            
}
window.onload = function(){
WebSocketTest();

}

function populate(wow)
{
var package = JSON.parse(wow);
for(var i in package){
   $("#list").append($("<li><button type='button' id='button' class='btn btn-link'>"+i+"</button></li>"));
   source[i]=package[i]["src"];
   console.log(source)
}

}

function btnclick()
{

$(document).on("click","#button",function()
   {
      retrieve($(this).html())
   });

}

function retrieve(name)
{
   var content = "";
   for(var i in source[name])
   {
      content += "<code style='display:block;'>"+source[name][i]+ "</code>"

   }


   $("#main").html(content);
}
