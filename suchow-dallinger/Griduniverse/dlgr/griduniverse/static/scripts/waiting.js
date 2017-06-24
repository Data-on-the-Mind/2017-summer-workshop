$(document).ready(function() {
    // wait for participant to be created and quorum to be reached
    create_participant().done(function () {
        go_to_page("grid");
    });
});
