setTimeout(function() {
    $.get("{% url 'pcstudent' %}") // Do something after 5 seconds
}, 2000);