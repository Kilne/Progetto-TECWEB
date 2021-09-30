$(function () {
    $('#btnSignUp').click(function () {
        $.ajax({
            url: '/Sign_Up/',
            data: $('form').serialize(),
            type: 'POST',
            success: function (response) {
                console.log(response);
            },
            error: function (error) {
                console.log(error);
                $('#message').html(error);
            }
        })
    })
})