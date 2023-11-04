const edit_form = document.querySelectorAll(".edit-form");
const default_profile = document.querySelectorAll(".def-profile");
const edit = document.getElementById("edit_btn");
const prof_btn = document.getElementById("pr-btn");

function editProfile(){
    edit_form.forEach(edit_prof => {
        edit_prof.style.display = "inline-block";
    });

    default_profile.forEach(def_prof => {
        def_prof.style.display = "none";
    });
}

function cancelProfile(){
//    var bio = document.getElementsByClassName("ql-editor");
//
//    bio[0].innerHTML = "";
//    bio[1].innerHTML = "";

    edit_form.forEach(edit_prof => {
        edit_prof.style.display = "none";
    });

    default_profile.forEach(def_prof => {
        def_prof.style.display = "block";
    });

    edit.style.display= "inline-block";
}


