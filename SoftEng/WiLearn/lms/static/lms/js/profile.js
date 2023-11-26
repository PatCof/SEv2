const edit_form = document.querySelectorAll(".edit-form");
const default_profile = document.querySelectorAll(".def-profile");
const edit = document.getElementById("edit_btn");
const prof_btn = document.getElementById("pr-btn");


function editProfile(){
    const bio_form = document.getElementById("id_biography");
    const contact_form = document.getElementById("id_contacts");

    const hidden_bio = document.getElementById("hidden_bio");
    const hidden_contacts = document.getElementById("hidden_contacts");

    contact_form.value = hidden_contacts.textContent;
    bio_form.value = hidden_bio.textContent;

    edit_form.forEach(edit_prof => {
        edit_prof.style.display = "inline-block";
    });

    default_profile.forEach(def_prof => {
        def_prof.style.display = "none";
    });
}

const cancelModal = document.getElementById("CancelModal");
const body = document.querySelector("body");
var cancel_btn = document.getElementById("can_btn");


function discardModal(){
    cancelModal.style.display = 'flex';
    body.style.overflow = 'hidden';
}

function cancelCancel(){
    cancelModal.style.display = "none";
    body.style.overflow = 'auto';

}


function cancelProfile(){
    const bio_form = document.getElementById("id_biography");
    const contact_form = document.getElementById("id_contacts");

    const hidden_bio = document.getElementById("hidden_bio");
    const hidden_contacts = document.getElementById("hidden_contacts");

    bio_form.value = hidden_bio.textContent;
    contact_form.value = hidden_contacts.textContent;

    edit_form.forEach(edit_prof => {
        edit_prof.style.display = "none";
    });

    default_profile.forEach(def_prof => {
        def_prof.style.display = "block";
    });

    edit.style.display= "inline-block";

    cancelCancel();
}


