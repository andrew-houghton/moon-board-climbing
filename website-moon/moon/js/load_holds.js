function clear_contents(container) {
    while (container.firstChild) {
        container.removeChild(container.firstChild);
    }
}

function updateHoldset() {
    var selected_year = document.querySelector('input[name="year"]:checked').value;
    if (selected_year == "2016") {
        holds = holds_2016
        climbs = climbs_2016
    } else {
        holds = holds_2017
        climbs = climbs_2017
    }

    var container = document.getElementById("moon-board");
    clear_contents(container)

    for (i = 0; i < holds.length; i++) {
        var div = document.createElement('div');

        if (holds[i]) {
            var img = document.createElement('img');
            img.src = 'moon/img/holds/' + holds[i][0];
            img.id = holds[i][1]
            img.alt = ""
            img.className = "hold " + holds[i][2]
            div.append(img)
        }

        container.append(div)
    }
    random_climb()
}
window.onload = updateHoldset;
