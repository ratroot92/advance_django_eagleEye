







const chatSocket = new WebSocket('ws://'+ window.location.host+'/celery_notifications/Twitter_Crawler/')
console.log(chatSocket)
chatSocket.onclose=function(e){
 console.log("closing websocket ")
//  location.reload(true);
}

chatSocket.onmessage=function(e){
 const data = JSON.parse(e.data);
       console.log(data);
       console.log(data.message);
if(data.info=='followers_scanning_complete'){
console.log(data.info)
Command: toastr["info"]('<div class="text-center "><button class="btn btn-warning  font-weight-bold ">CELERY NOTIFIER</button></div><div class="text-white font-weight-bold ">'+data.message+'</div>')

toastr.options = {
  "closeButton": true,
  "debug": false,
  "newestOnTop": true,
  "progressBar": true,
  "positionClass": "toast-top-right",
  "preventDuplicates": false,
  "onclick": null,
  "showDuration": "300",
  "hideDuration": "1000",
  "timeOut": "5000",
  "extendedTimeOut": "1000",
  "showEasing": "swing",
  "hideEasing": "linear",
  "showMethod": "fadeIn",
  "hideMethod": "fadeOut"
}
}
else if(data.info=='following_scanning_complete'){
  console.log(data.info)
  Command: toastr["info"]('<div class="text-center "><button class="btn btn-warning  font-weight-bold ">CELERY NOTIFIER</button></div><div class="text-white font-weight-bold ">'+data.message+'</div>')

toastr.options = {
  "closeButton": true,
  "debug": false,
  "newestOnTop": true,
  "progressBar": true,
  "positionClass": "toast-top-right",
  "preventDuplicates": false,
  "onclick": null,
  "showDuration": "300",
  "hideDuration": "1000",
  "timeOut": "5000",
  "extendedTimeOut": "1000",
  "showEasing": "swing",
  "hideEasing": "linear",
  "showMethod": "fadeIn",
  "hideMethod": "fadeOut"
}
}
else if(data.info=='tweets_insertion'){

}




}


