// static/js/ckeditor-init.js

document.addEventListener('DOMContentLoaded', function () {
    // Replace 'content' with the ID of your CKEditor textarea
    CKEDITOR.replace('content', {
        height: 300,
        toolbar: 'Basic',
    });
});
