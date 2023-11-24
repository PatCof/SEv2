const activeCourses = document.getElementById('activeCourses');
const inactiveCourses = document.getElementById('inactiveCourses');
const activeButton = document.getElementById('activeButton');
const inactiveButton = document.getElementById('inactiveButton');

function toggleCourses(type) {
    if (type === 'active') {
        activeCourses.style.display = 'block';
        inactiveCourses.style.display = 'none';
        activeButton.classList.add('active');
        inactiveButton.classList.remove('active');
        // Set text color
        activeButton.style.color = 'black';
        inactiveButton.style.color = '#828282';
    } else if (type === 'inactive') {
        activeCourses.style.display = 'none';
        inactiveCourses.style.display = 'block';
        activeButton.classList.remove('active');
        inactiveButton.classList.add('active');
        // Set text color
        activeButton.style.color = '#828282';
        inactiveButton.style.color = 'black';
    }
}


document.addEventListener("DOMContentLoaded", function() {
    const addCourseButton = document.getElementById("addCourseButton");
    const currentUrl = window.location.href;
    // Add an onclick event handler to the button
    addCourseButton.addEventListener("click", function() {
      // Navigate to another HTML page
        window.location.href = 'add_course/';
    });
  });



function navigateToPostAnnouncement() {
    // Redirect to postannouncement.html
    window.location.href = "create_announcement/";
}


let isEditable = false;

function editModule() {
    const moduleTitle = document.getElementById("module-title");
    const editButton = document.getElementById("edit-button");
//    const contentTextarea = document.getElementById("mod_content");
    const mod_content = document.getElementById("mod_content");
    const mod_form = document.getElementById("mod_form")
    const nextPageButton = document.querySelector(".next-page-button");
    const editOptions = document.getElementById("edit-options");

    if(!isEditable){
        mod_content.style.display= 'none';
        mod_form.style.display= 'block';
        isEditable = true;
        editButton.classList.add("editable");
        editOptions.style.display = "block"; // Show the three buttons
    } else{
        mod_content.style.display = 'block';
        mod_form.style.display = 'none';
        isEditable = false;
        editButton.classList.remove("editable");
        editOptions.style.display = "none"; // Hide the three buttons
    }

    if (editOptions.style.display === "none") {
        nextPageButton.style.display = "block"; // Show the "Next Page" button
    } else {
        nextPageButton.style.display = "none"; // Hide the "Next Page" button
    }
}


const cancelModal = document.getElementById("CancelModal");
const body = document.querySelector("body");
var cancel_btn = document.getElementById("can_btn");


cancel_btn.onclick = function() {
    cancelModal.style.display = "none";
    body.style.overflow = 'auto';

}

const cls_btn = document.querySelectorAll('.cls_btn');
const id_val = document.getElementById("id_val");
cls_btn.forEach((cls_btn) => {
    cls_btn.addEventListener('click', () => {
        cancelModal.style.display = 'flex';
        body.style.overflow = 'hidden';

        var input = cls_btn.previousElementSibling;
        id_val.value = input.value
    });
});


function cancelCourse(){
    window.location.href = "../";
}

function cancelCancel(){
    cancelModal.style.display = "none";
    body.style.overflow = 'auto';
}

function discardCourse(){
    cancelModal.style.display = 'flex';
    body.style.overflow = 'hidden';
}

function cancelModuleEdit(){
    window.location.href = "../../";
}




// Initial state
toggleCourses('active'); // Set 'Active Courses' as the default
