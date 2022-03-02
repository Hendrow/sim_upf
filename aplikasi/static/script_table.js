$(document).ready(function(){
    $('#input_alat').keyup(function(){
        var alat = $(this).val();        
        if (alat!=""){
            load_data(alat)
        }        
    })

    function load_data(hasil){
        var url= $('form').attr('action')
        $.ajax({
            url: url,
            method:'POST',
            data: {hasil},
            success: function(data){
                $('#result').html(data);
                $('#result').append(data.htmlresponse)
                console.log(url)

            }
        })
    }
})