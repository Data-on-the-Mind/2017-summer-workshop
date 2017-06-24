$(document).ready(function() {
  // Begin the experiment.
  $("#begin-experiment").click(function() {
    window.location.href = '/waiting';
  });

  // Opt out of the experiment.
  $("#opt-out").click(function() {
    window.location.href = "/questionnaire?participant_id=" + participant_id;
  });
});
