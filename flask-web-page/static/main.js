function generate_report(val){
$.ajax({
    url:"/app="+val
}).done(function(data){
    $("#test").attr('data', data)
//    console.log(data)
//window.open("data:application/pdf," + encodeURI(data));
})
}