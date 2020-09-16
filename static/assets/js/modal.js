$(document).ready(function() {
    $("button").click(function() {
      var favorite = [];
      $.each($("input[name='check_repair']:checked"), function() {
        favorite.push($(this).val());
      });
      $('#modal_repair1').modal('show').on('shown.bs.modal', function() {
        var str = $("#check_repair").html("My favourite sports are: " + favorite.join(", "));
        console.log(str);
      });
    });
  });