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
    const title = document.querySelector(".title");
    const content = document.querySelector(".mod_content");

    const mod_form = document.getElementById("mod_form")
    const ed_button = document.querySelector(".edit-button");

    const nav_page = document.querySelector(".a");
    const editOptions = document.getElementById("edit-options");

    if(!isEditable){
        title.style.display = 'none';
        content.style.display = 'none';
        mod_content.style.display= 'none';
        mod_form.style.display= 'block';
        editOptions.style.display = "block";
        ed_button.style.display = "none";
        isEditable = true;

    } else{
        title.style.display = 'block';
        content.style.display =  'block';
        mod_content.style.display = 'block';
        mod_form.style.display = 'none';
        editOptions.style.display = "none";
        isEditable = false;

    }

    if (editOptions.style.display === "none") {
        nav_page.style.display = "flex";
    } else {
        nav_page.style.display = "none";
    }
}




const cancelModal = document.getElementById("CancelModal");
const cancelModal2 = document.getElementById("CancelModal2");

const body = document.querySelector("body");
var cancel_btn = document.getElementById("can_btn");
var cancel_btn2 = document.getElementById("can_btn2");


cancel_btn.onclick = function() {
    cancelModal.style.display = "none";
    body.style.overflow = 'auto';

}

cancel_btn2.onclick = function() {
    cancelModal2.style.display = "none";
    body.style.overflow = 'auto';

}


const cls_btn = document.querySelectorAll('.cls_btn');
const cls_btn1 = document.querySelectorAll('.cls_btn1');

const id_val = document.getElementById("id_val");
const id_val2 = document.getElementById("id_val2");

cls_btn.forEach((cls_btn) => {
    cls_btn.addEventListener('click', () => {
        cancelModal.style.display = 'flex';
        body.style.overflow = 'hidden';

        var input = cls_btn.previousElementSibling;
        id_val.value = input.value
    });
});

cls_btn1.forEach((cls_btn1) => {
    cls_btn1.addEventListener('click', () => {
        cancelModal2.style.display = 'flex';
        body.style.overflow = 'hidden';

        var input = cls_btn1.previousElementSibling;
        id_val2.value = input.value
    });
});


function cancelCourse(){
    window.location.href = "../";
}

function cancelCancel(){
    cancelModal.style.display = "none";
    body.style.overflow = 'auto';
    ed_button.style.display = "block";

    isEditable = false;

}

function discardCourse(){
    cancelModal.style.display = 'flex';
    body.style.overflow = 'hidden';
}

function cancelCancel2(){
    cancelModal2.style.display = "none";
    body.style.overflow = 'auto';
    ed_button.style.display = "block";

    isEditable = false;

}

function discardCourse2(){
    cancelModal2.style.display = 'flex';
    body.style.overflow = 'hidden';
}




function cancelModuleEdit(){
    window.location.href = "../../";
}




// Initial state
toggleCourses('active'); // Set 'Active Courses' as the default
