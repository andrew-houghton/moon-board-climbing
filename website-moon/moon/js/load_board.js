function reset_board() {
    clear_contents_grade()
    var myClasses = document.querySelectorAll('.hold'),
        i = 0,
        l = myClasses.length;

    for (i; i < l; i++) {
        myClasses[i].classList.add('m-fadeIn');
        myClasses[i].classList.remove('m-fadeOut');
    }
}

function clear_board() {
    clear_contents_grade()
    var myClasses = document.querySelectorAll('.hold'),
        i = 0,
        l = myClasses.length;

    for (i; i < l; i++) {
        myClasses[i].classList.add('m-fadeOut');
        myClasses[i].classList.remove('m-fadeIn');
    }
}

function random_climb() {
    var model = document.querySelector('input[name="model"]:checked').value;
    var index = Math.floor(Math.random() * climbs[model].length)
    display(climbs[model][index].moves)
    display_grades(climbs[model][index].grade)
}

function display(moves) {
    clear_board();
    for (var i = moves.length - 1; i >= 0; i--) {
        var hold = document.getElementById(moves[i]);
        if (hold != null) {
            hold.classList.add('m-fadeIn');
            hold.classList.remove('m-fadeOut');
        }
    }
}

function clear_contents_grade() {
    var container = document.getElementsByClassName("grade");
    for (var i = 0; i < container.length; i++) {
        container.item(i).innerText = "";
    }
}

function display_grades(grades) {
    var container = document.getElementsByClassName("grade");
    for (var i = 0; i < container.length; i++) {
        if(grades.hasOwnProperty(container.item(i).id)) {
          container.item(i).innerText = grades[container.item(i).id];
        }
        else {
          container.item(i).innerText = "-";
        }
    }
}
