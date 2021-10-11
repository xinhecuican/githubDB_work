$( document ).ready(function() {

    //autenticação sptrans
    $.ajax( "/auth_sptrans/" )
        .done(function() {
            console.log( "success" );
        })
        .fail(function() {
            console.log( "error" );
        })
        .always(function() {
            console.log( "complete" );
        });

});
