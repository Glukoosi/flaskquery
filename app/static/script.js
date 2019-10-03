document.addEventListener('DOMContentLoaded', function(){



$('input[type=checkbox][name=premium]').change(function() {
        if (document.getElementById('premium').checked) {
            $('#premium-show').show();
        } else {
            $('#premium-show').hide();
            $('input[=premium]').val("");
        }
    });


}, false);
