$(document).ready(function() {
    $('form').on('submit', function(event) {
        $('#loading').show();
        $.ajax({
            data : {
                name : $('#fullname').val()
            },
            type : 'POST',
            url : '/process'
        })
        .done(function(data) {
            if (data.error) {
                $('#errorAlert').text(data.error).show();
                $('#successAlert').hide();
                $('#loading').hide();
            }
            else {
                $('#successAlert').text(data.name).show();
                $('#errorAlert').hide();
                $('#loading').hide();
            } 
        });
        event.preventDefault();
    });
});
