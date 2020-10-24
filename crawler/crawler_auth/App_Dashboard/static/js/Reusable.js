function publishToastMessage(message,type)
{
      console.log("%cToaster Ready !", "color:green;font-size:16px;font-weight:bold;")
      console.log(message)
      // Command: toastr["{{ message.tags }}"]("{{ message }} .")
        Command: toastr[`${type}`](`${message} .`)

      toastr.options = {
          "closeButton": true,
          "debug": false,
          "newestOnTop": false,
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


function getCurrentTime(){
    var d = new Date("2011-04-20T09:30:51.01");
    let hours=d.getHours(); // => 9
    let hour= hours > 9 ? `${hours}`: `0${hours}`  ;
    let minutes=d.getMinutes(); // =>  30
    let minute=minutes > 9 ? `${minutes}`: `0${minutes}`  ;
    let seconds=d.getSeconds(); // => 51
    let second=seconds > 9 ? `${seconds}`: `0${seconds}`  ;
    return `${hour}:${minute}:${second}`;

}