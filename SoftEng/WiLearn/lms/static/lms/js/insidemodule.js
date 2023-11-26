function toggleDisplay(section) {
    if (section === 'modules') {
        modulesSection.style.display = 'block';
        calendarSection.style.display = 'none';
        modulesButton.classList.add('active');
        calendarButton.classList.remove('active');
        
        // Set text color
        modulesButton.style.color = 'black';
        calendarButton.style.color = '#828282';
    } else if (section === 'calendar') {
        modulesSection.style.display = 'none';
        calendarSection.style.display = 'block';
        modulesButton.classList.remove('active');
        calendarButton.classList.add('active');
        
        // Set text color
        modulesButton.style.color = '#828282';
        calendarButton.style.color = 'black';
    }
}


function toggleCollapsible(section) {
    const content = document.querySelectorAll(".contents")[section - 1];
    content.style.display = content.style.display === "block" ? "none" : "block";
    const collapsible = document.querySelectorAll(".collapsible")[section - 1];
    collapsible.classList.toggle("active");
  }




const cancelModal = document.getElementById("CancelModal");
const body = document.querySelector("body");
var cancel_btn = document.getElementById("can_btn");


function cancelModule(){
    window.location.href = "../../";
}

function cancelCancel(){
    cancelModal.style.display = "none";
    body.style.overflow = 'auto';
}

function discardModule(){
    cancelModal.style.display = 'flex';
    body.style.overflow = 'hidden';
}












// Initial state (Modules is active by default)
toggleDisplay('modules');

//function discardCourse() {
//    // Display a confirmation dialog
//    var confirmDiscard = confirm("Are you sure you want to discard this Module?");
//
//    // If the user confirms, navigate to dashboard.html
//    if (confirmDiscard) {
//        window.location.href = "../../";
//    }
//}




