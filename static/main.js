$(document).ready(function() {
    $(document).on('click', "#submit_btn", function(e) {
        e.preventDefault();
        var url = 'js_submit_answer';
        $.ajax({
            type: "POST",
            url: url,
            data: $("#submit_answer_form").serialize(), // serializes the form's elements.
            success: function(response) {
                $('#results').fadeOut(100).fadeIn(1000);
                $('#results').html(response);
            },
            error: function(error) {
                console.log("Not Working");
            }
        });
        e.preventDefault();
    });

});
