function WebSocketTest()
         {
            
               
               // Let us open a web socket
               var ws = new WebSocket("ws://localhost:8888/socket");
				
               ws.onopen = function()
               {
                console.log("websocket opened")  
               };
				
               ws.onmessage = function (evt) 
               { 
                  var received_msg = evt.data;
                  console.log(JSON.parse(received_msg));
               };
				
               ws.onclose = function()
               { 
                  // websocket is closed.
                  alert("Connection is closed..."); 
               };
            
         
            
         }
window.onload = function(){
WebSocketTest();

}