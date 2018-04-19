$(document).ready(function() {
    $(document).on('click', "#login_btn", function(e) {
        e.preventDefault();
        var url = 'js_login';
        $.ajax({
            type: "POST",
            url: url,
            data: $("#login_form").serialize(),
            success: function(response) {
                $('#results').fadeOut(400);
                setTimeout(function() {$('#results').html(response);}, 400);
                $('#results').fadeIn(400);
            },
            error: function(error) {
                console.log("Not Working");
            }
        });
        
    });
    $(document).on('click', "#submit_btn", function(e) {
        e.preventDefault();
        var url = 'js_submit_answer';
        $.ajax({
            type: "POST",
            url: url,
            data: $("#submit_answer_form").serialize(), // serializes the form's elements.
            success: function(response) {
                $('#results').fadeOut(400);
                setTimeout(function() {$('#results').html(response);}, 400);
                $('#results').fadeIn(400);
            },
            error: function(error) {
                console.log("Not Working");
            }
        });
        
    });
    $(document).on('click', "#skip_btn", function(e) {
        e.preventDefault();
        var url = 'js_skip_question';
        $.ajax({
            type: "POST",
            url: url,
            success: function(response) {
                $('#results').fadeOut(400);
                setTimeout(function() {$('#results').html(response);}, 400);
                $('#results').fadeIn(400);
            },
            error: function(error) {
                console.log("Not Working");
            }
        });
        e.preventDefault();
    });

});
