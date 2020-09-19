function getvalues() {
    var selected = new Array();
    var chbox = document.getElementById("checkbox_field");
    var selectbox = chbox.getElementsByTagName("input");
    for (var i = 0; i < selectbox.length; i++) {
        if (selectbox[i].checked) {
            selected.push(selectbox[i].value);
        }

    }
    if (selected.length > 0) {
        document.getElementById("id_textinput").innerHTML = selected;
        console.log(selected);
    }
    console.log(selected);
}