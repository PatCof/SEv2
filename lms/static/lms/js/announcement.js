//var quill = new Quill('#announcement-editor', {
//    theme: 'snow',
//    modules: {
//        toolbar: [
//            ['bold', 'italic', 'underline'],
//            [{ 'align': [] }], // Text alignment options
//            [{ 'list': 'ordered' }, { 'list': 'bullet' }],
//            ['link', 'image', 'video'],
//            ['clean'],
//            [{ 'header': [1, 2, 3, false] }],
//            ['blockquote'],
//            ['file'] // File upload button
//        ]
//    },
//    placeholder: 'Compose your announcement...',
//});
//
//// Enable the file upload module
//var fileUploadModule = quill.getModule('fileUpload');
//fileUploadModule.addHandler('file', function () {
//    var input = document.createElement('input');
//    input.setAttribute('type', 'file');
//    input.setAttribute('accept', '.pdf');
//    input.onchange = function () {
//        if (input.files && input.files[0]) {
//            var file = input.files[0];
//            if (file.type === 'application/pdf') {
//                // Handle the selected PDF file here, e.g., display its name or upload it.
//                console.log('Selected PDF file:', file.name);
//            } else {
//                alert('Please select a valid PDF file.');
//            }
//        }
//    };
//    input.click();
//});


const cancelModal = document.getElementById("CancelModal");
const body = document.querySelector("body");
var cancel_btn = document.getElementById("can_btn");


function cancelAnnouncement(){
    window.location.href = "../";
}

function cancelCancel(){
    cancelModal.style.display = "none";
    body.style.overflow = 'auto';
//    qlblank.contentEditable = "true";
}

function discardAnnouncement(){
    cancelModal.style.display = 'flex';
    body.style.overflow = 'hidden';
}



//
//function cancelAnnouncement() {
//    var confirmation = confirm("Are you sure you want to discard this announcement?");
//    if (confirmation) {
//        // Redirect to dashboard.html
//        window.location.href = "../";
//    }
//}

