document.addEventListener('DOMContentLoaded', function(){


document.onkeypress=function(e){
    console.log("aaa")
    $('#urlfil').text($('input[type=text][name=short]').val())
}

$('input[type=checkbox][name=premium]').change(function() {
        if (document.getElementById('premium').checked) {
            $('#premium-show').show();
            $('#premiumasd').hide();
        } else {
            $('#premium-show').hide();
            $('#premiumasd').show();
            $('input[=premium]').val("");
        }
    });


}, false);
