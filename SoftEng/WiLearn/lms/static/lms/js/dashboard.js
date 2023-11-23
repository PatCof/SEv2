// JavaScript code to control the visibility and text color of courses

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

// Add a click event listener to all announcements
//const announcements = document.querySelectorAll('.announcement');
//
//announcements.forEach((announcement) => {
//    announcement.addEventListener('click', () => {
//        // Perform an action when an announcement is clicked
//        alert('You clicked on an announcement: ' + announcement.querySelector('.announcement-title').textContent);
//    });
//});

document.addEventListener("DOMContentLoaded", function() {
    const addCourseButton = document.getElementById("addCourseButton");
    const currentUrl = window.location.href;
    // Add an onclick event handler to the button
    addCourseButton.addEventListener("click", function() {
      // Navigate to another HTML page
        window.location.href = 'add_course/';
    });
  });


function discardCourse() {
    // Display a confirmation dialog
    var confirmDiscard = confirm("Are you sure you want to discard this course?");

    // If the user confirms, navigate to dashboard.html
    if (confirmDiscard) {
        window.location.href = "../";
    }
}
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


//
//function deletePopup() {
//    cancelModal.style.display = 'flex';
//    body.style.overflow = 'hidden';
//
//    var get_id =
//
//}


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





function nextPage() {
    // Add your code for navigating to the next page here.
}


// Initial state
toggleCourses('active'); // Set 'Active Courses' as the default
