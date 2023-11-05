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

function addCourse() {
    // Redirect to postannouncement.html
    window.location.href = "createmodule.html";
}

function toggleCollapsible(section) {
    const content = document.querySelectorAll(".contents")[section - 1];
    content.style.display = content.style.display === "block" ? "none" : "block";
    const collapsible = document.querySelectorAll(".collapsible")[section - 1];
    collapsible.classList.toggle("active");
  }

// Initial state (Modules is active by default)
toggleDisplay('modules');