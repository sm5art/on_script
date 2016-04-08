var source = {};
var ws;
function WebSocketTest()
{
    ws = new WebSocket("ws://localhost:8888/socket");
				
   ws.onopen = function()
   {
                
   };
				
   ws.onmessage = function (evt) 
   {
         var received_msg = JSON.parse(evt.data);
         if(received_msg['header']==("populate")){
            delete received_msg['header'];
            populate(received_msg);

         }
         else if(received_msg['header']==("output")){
            delete received_msg['header'];
            output(received_msg);
         }
      };
				
   ws.onclose = function()
   { 
                  
               
   };
            
         
            
}
window.onload = function(){
WebSocketTest();
btnclick();
}

function populate(package)
{

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

$(document).on("click",".run",function()
   {
      run($(this).attr('name'))
   });

}

function retrieve(name)
{
   var content = "<div class='jumbotron'><h1>"+name+"</h1>"+'<button name="'+name+'" style="width:10%;" class="run btn btn-default" aria-hidden="true"><span class="glyphicon glyphicon-play" aria-hidden="true"></span></button></div>'
    
   content += "<div class='col-xs-11 col-sm-11'>";
   for(var i in source[name])
   {
      content += "<code style='display:block;'>"+source[name][i]+ '</code>';

   }
   content += "</div></div>";


   $("#main").html(content);
}

function run(name)
{
ws.send(name);
}

function output(str){
console.log(str);
}