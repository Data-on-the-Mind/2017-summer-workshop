$(document).ready(function() {
  // Begin the experiment.
  $("#begin-experiment").click(function() {    
    allow_exit();
    window.location.href = "/grid?participant_id=" + participant_id;
  });

  // Opt out of the experiment.
  $("#opt-out").click(function() {
    allow_exit();
    window.location.href = "/questionnaire?participant_id=" + participant_id;
  });
});
