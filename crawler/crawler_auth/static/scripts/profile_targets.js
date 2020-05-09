


const useranme=''


const chatSocket = new WebSocket('ws://'+ window.location.host+'/rescan/profile_targets/')
   console.log(chatSocket)


   $('.scanBtn').on('click',function(){
    var r = confirm(" CUATION ! \n All previously fetched records will be deleted  ");
        if (r == true) {
            let _name =$(this).attr("data-id")
            console.log(_name)
            console.log(chatSocket)
            chatSocket.send(JSON.stringify({
            '_username': _name

            }));



          chatSocket.onmessage = function(e) {
            const data = JSON.parse(e.data);
           console.log(data);
          if(data._status_code==1){
            alert("Server Denied request \n  Scanning already completed   ")
          }


        };
      }
      else{
console.log("User Denied Rescanning Request")
        }
      })


        chatSocket.onclose = function(e) {
            console.error('Web-socket closed unexpectedly');
        };



   

  $('#TwitterTargetTable').DataTable({
    dom: 'Bfrtip',
  buttons: [
      'copy', 'excel', 'pdf'
  ]
  })


