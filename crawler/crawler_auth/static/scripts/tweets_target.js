
      // const _username='maliksblr92'
    //const chatSocket = new WebSocket('ws://'+ window.location.host+'/re_scan/'+ _username+ '/')
    const re_scan_socket = new WebSocket('ws://'+ window.location.host+'/re_scan/')
    console.log(re_scan_socket)
          $('.scanBtn').on('click',function(){

            var r = confirm(" CUATION ! \n All previously fetched records will be deleted  ");
        if (r == true) {
            let _name =$(this).attr("data-id")

            console.log(_name)

            console.log(re_scan_socket)
            re_scan_socket.send(JSON.stringify({
            '_username': _name

            }));


          }
        else{
console.log("User Denied Rescanning Request")
        }


           })
          re_scan_socket.onmessage = function(e) {
            const data = JSON.parse(e.data);
           console.log(data);
          if(data._status_code==1){
            alert("Server Denied request \n  Scanning already completed   ")
          }


        };



        re_scan_socket.onclose = function(e) {
            console.error('Web-socket closed unexpectedly');
        };

     








   const get_count_socket = new WebSocket('ws://'+ window.location.host+'/getCount/')
   console.log(get_count_socket)

         $('.getCount').on('click',function(){
           const _name =$(this).attr("data-id")

           console.log(_name)

           console.log(get_count_socket)
           get_count_socket.send(JSON.stringify({
           '_username': _name

           }));

           get_count_socket.onmessage = function(e) {
           const data = JSON.parse(e.data);
          console.log(data);
          $('#'+_name).empty().append(" [ "+data._tweets_count+" ]")
       };


       get_count_socket.onopen = function(e) {
           console.log('connection opened')
          
        };

          })




       get_count_socket.onclose = function(e) {
           console.error('Web-socket closed unexpectedly');
       };

   













  const celery_notifier_socket = new WebSocket('ws://'+ window.location.host+'/celery_notifications/Twitter_Crawler/')
   console.log(celery_notifier_socket)




   celery_notifier_socket.onclose=function(e){
    console.log("closing websocket ")
    //location.reload(true);
   }

   celery_notifier_socket.onmessage=function(e){
    const data = JSON.parse(e.data);
          console.log(data);
          console.log(data.username);


          $('#'+data.username).empty().append(" [ "+data.message+" ]")
   }



  $('#TwitterTargetTable').DataTable({
    dom: 'Bfrtip',
  buttons: [
      'copy', 'excel', 'pdf'
  ]
  })

