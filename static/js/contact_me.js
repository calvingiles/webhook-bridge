$(function() {

    $("input,textarea").jqBootstrapValidation({
        preventSubmit: true,
        submitError: function($form, event, errors) {
            // additional error messages or events
        },
        submitSuccess: function($form, event) {
            event.preventDefault(); // prevent default submit behaviour
            // get values from FORM
            var in_hook = $("input#in_hook").val();
            var email = $("input#email").val();
            var bridge_hook_url = "http://api.suspension.io"
            bridge_hook_url = bridge_hook_url + "/bridge_webhook"
            var bridge_hook_url_args = "?"
            // bridge_hook_url = bridge_hook_url + "email="
            // bridge_hook_url = bridge_hook_url + email
            // bridge_hook_url = bridge_hook_url + "&"
            bridge_hook_url_args = bridge_hook_url_args + "destination_hook_url="
            bridge_hook_url_args = bridge_hook_url_args + encodeURIComponent(in_hook)
            bridge_hook_url = bridge_hook_url + bridge_hook_url_args

            var extra_args = "&" + "email=" + email

            $.ajax({
                url: "/contact_me" + bridge_hook_url_args + extra_args,
                type: "POST",
                // contentType: "application/json",
                data: {
                    in_hook: in_hook,
                    email: email
                },
                cache: false,
                success: function() {
                    // Success message
                    $('#success').html("<div class='alert alert-success'>");
                    $('#success > .alert-success').html("<button type='button' class='close' data-dismiss='alert' aria-hidden='true'>&times;")
                        .append("</button>");
                    $('#success > .alert-success')
                        .append("<strong>Your bridge webhook url is: <br />" + '<pre>' + bridge_hook_url + '</pre>' + "</strong>");
                    $('#success > .alert-success')
                        .append('</div>');

                    //clear all fields
                    // $('#contactForm').trigger("reset");
                },
                error: function() {
                    // Fail message
                    $('#success').html("<div class='alert alert-danger'>");
                    $('#success > .alert-danger').html("<button type='button' class='close' data-dismiss='alert' aria-hidden='true'>&times;")
                        .append("</button>");
                    $('#success > .alert-danger').append("<strong>Sorry, it seems that my mail server is not responding. Please try again later!");
                    $('#success > .alert-danger').append('</div>');
                    //clear all fields
                    $('#contactForm').trigger("reset");
                },
            })
        },
        filter: function() {
            return $(this).is(":visible");
        },
    });

    $("a[data-toggle=\"tab\"]").click(function(e) {
        e.preventDefault();
        $(this).tab("show");
    });
});


/*When clicking on Full hide fail/success boxes */
$('#name').focus(function() {
    $('#success').html('');
});
