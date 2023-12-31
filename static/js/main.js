
$(document).ready(function() {
// Trigger the event when the page loads
$('#add_course').trigger('change');

// Attach the change event to #add_course
$(document).on('change', '#add_course', function() {
var courseId = $(this).val();
console.log(courseId);
var unitSelect = $('#add_unit');

// Clear existing options
unitSelect.empty();

// Fetch units for the selected course
$.ajax({
    url: '/get_units_and_lessons/' + courseId + '/',
    dataType: 'json',
    success: function(data) {
        // Check if 'units' property exists in the data
        if (data.units && Array.isArray(data.units)) {
            // Add new options based on the fetched units
            $.each(data.units, function(index, unit) {
                var option = $('<option>');
                option.val(unit.id);
                option.text('Unit ' + unit.number + ' - ' + unit.title);
                unitSelect.append(option);
            });
        } else {
            console.error('Error: Units array not found in the response.');
        }
    },
    error: function(error) {
        console.error('Error fetching units:', error);
    }
});
});
});

document.addEventListener('DOMContentLoaded', function () {

let courseId;
let selectedCourseId;


$(document).on('change', '#course', function() {
    courseId = $(this).val();
    selectedCourseId = $(this).val();
    console.log(courseId)
    console.log(selectedCourseId)
    secondDiv = document.getElementById('content');
            secondDiv.innerHTML = '';
});


var courseDropdown = document.getElementById('course');
var accordion = document.getElementById('accordion-collapse');

courseDropdown.addEventListener('change', function () {
    selectedCourseId = courseDropdown.value;

    fetch('/get_units_and_lessons/' + selectedCourseId + '/')
        .then(response => response.json())
        .then(data => {
            console.log('Received data:', data);

            var accordion = document.getElementById('accordion-collapse');
            accordion.innerHTML = `
                <div class="flex justify-between p-2">
                    <label class="block font-medium text-gray-700">Units</label>
                    <button onclick="add_unit(${selectedCourseId})" type="button" id="addUnit" class="text-green-600 bg-green-100 font-semibold items-center bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800">
                        + Add Unit
                    </button>
                </div>`;

            if (data.units && Array.isArray(data.units)) {
                data.units.forEach(function (unit, index) {
                    var accordionItem = document.createElement('div');
                    accordionItem.innerHTML = `
                        <div class="p-2 border border-b-0 rounded-b-xl p-4 border-gray-200 dark:border-gray-700">
                            <h2 id="accordion-collapse-heading-${index + 1}">
                                <button type="button" class="hover:underline flex items-center justify-between w-full p-4 font-medium rtl:text-right text-gray-500 border border-b-0 border-gray-200 rounded-t-xl focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-800 dark:border-gray-700 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-800 gap-3" data-accordion-target="#accordion-collapse-body-${index + 1}" aria-expanded="false" aria-controls="accordion-collapse-body-${index + 1}">
                                    <span onclick="edit_unit(${unit.id})">Unit ${unit.number} - ${unit.title}</span>
                                    <svg data-accordion-icon class="w-3 h-3 rotate-180 shrink-0" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 10 6">
                                        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5 5 1 1 5"/>
                                    </svg>
                                </button>
                            </h2>
                            <div id="accordion-collapse-body-${index + 1}" class="hidden" aria-labelledby="accordion-collapse-heading-${index + 1}">
                                <ul id="lesson-list-${index + 1}">
                                </ul>
                                <button onclick="add_lesson(${unit.id})" class="text-green-600 bg-green-100 font-semibold text-center inline-flex items-center bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm text-center text-sm px-5 py-2.5 dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800">
                                    + Add Lesson
                                </button>
                            </div>
                        </div>
                    `;

                    accordion.appendChild(accordionItem);

                    // Populate lessons if available
                    if (unit.lessons && Array.isArray(unit.lessons)) {
                        var lessonList = accordionItem.querySelector(`#lesson-list-${index + 1}`);
                        unit.lessons.forEach(function (lesson) {
                            var lessonItem = document.createElement('li');
                            lessonItem.innerHTML = `
                                <li class="hover:underline rounded-md p-2 cursor-pointer flex justify-between">
                                    <a class="text-gray-500" data-lesson-id="${lesson.id}" href="/lesson/${lesson.id}">${lesson.title}</a>
                                </li>
                            `;
                            lessonList.appendChild(lessonItem);
                        });
                    }

                    accordionItem.querySelector('button').addEventListener('click', function () {
                        var isExpanded = accordionItem.querySelector('button').getAttribute('aria-expanded') === 'true';
                        accordionItem.querySelector('button').setAttribute('aria-expanded', !isExpanded);
                        accordionItem.querySelector('svg').classList.toggle('rotate-180', !isExpanded);
                        accordionItem.querySelector(`#accordion-collapse-body-${index + 1}`).classList.toggle('hidden', isExpanded);
                    });
                });
            } else {
                console.error('Error: Units array not found in the response.');
            }
        })
        .catch(error => console.error('Error fetching units and lessons:', error));
});


});

let lessonId;
let secondDiv;
let selectedCourseId;
let unit_id;

// Click the lessons 
document.addEventListener('click', function (event) {
    var lessonTitleLink = event.target.closest('#lesson_link');

    if (lessonTitleLink) {
        event.preventDefault();
        lessonId = lessonTitleLink.dataset.lessonId;
        // unitId = lessonTitleLink.dataset.unitId;
        handleLessonTitleClick(lessonId);
    }
});

function handleLessonTitleClick(lessonId) {
    fetch(`/edit_lesson/` + lessonId + `/`)
        .then(response => response.text())
        .then(htmlContent => {
            // Update the content in the second div
            secondDiv = document.getElementById('content');
            secondDiv.innerHTML = htmlContent;
            CKEDITOR.replaceAll();
        })
        .catch(error => {
            console.error('Error fetching lesson HTML content:', error);
        });
}

function add_lesson(unitId) {
    selectedCourseId = $('#course').val();
    let addlessonbtn = $('#addlessonbtn');
    // let unitId = addlessonbtn.data('unit-id');
    console.log(unitId);

    fetch(`/add_lesson/`)
        .then(response => response.text())
        .then(htmlContent => {
            // Update the content in the second div
            secondDiv = document.getElementById('content');
            secondDiv.innerHTML = htmlContent;
            
            // Auto-select the dropdown value based on courseId
            $('#add_course').val(selectedCourseId);
            // $('#add_unit').val(unitId);
             // Trigger the event when the page loads
            $('#add_course').trigger('change');
            
            // Wait for the dropdown to be populated before setting its value
            setTimeout(() => {
                $('#add_unit').val(unitId);
            }, 100); // Adjust the delay as needed
            

            console.log('must',unitId);
            CKEDITOR.replaceAll();
        })
        .catch(error => {
            console.error('Error fetching lesson HTML content:', error);
        });
}

function edit_unit(unitId) {
    selectedCourseId = $('#course').val();
    unit_id = unitId;
    // let unitId = addlessonbtn.data('unit-id');
    console.log(unit_id);
    console.log(unitId);

    fetch(`/edit_unit/`+unitId+`/`)
        .then(response => response.text())
        .then(htmlContent => {
            // Update the content in the second div
            secondDiv = document.getElementById('content');
            secondDiv.innerHTML = htmlContent;

            console.log(unitId);
            
            // Auto-select the dropdown value based on courseId
            $('#add_course').val(selectedCourseId);
        })
        .catch(error => {
            console.error('Error fetching lesson HTML content:', error);
        });
}

function add_unit(courseId) {
    selectedCourseId = $('#course').val();
    // let unitId = addlessonbtn.data('unit-id');
    console.log(courseId);

    fetch(`/add_unit/`)
        .then(response => response.text())
        .then(htmlContent => {
            // Update the content in the second div
            secondDiv = document.getElementById('content');
            secondDiv.innerHTML = htmlContent;
            
            // Auto-select the dropdown value based on courseId
            $('#add_course').val(courseId);
        })
        .catch(error => {
            console.error('Error fetching lesson HTML content:', error);
        });
}

function discard() {
    secondDiv.innerHTML = '';
}

// Add custom CSS to set the button text color
var style = document.createElement('style');
style.innerHTML = `
    .confirm-button-class {
        color: #dc2626 !important;
    }
    .cancel-button-class {
        color: #fff !important;
    }
`;
document.head.appendChild(style);

function delete_lesson(){
            cid = lessonId;

            // Confirm deletion using SweetAlert2
            Swal.fire({
                icon: 'warning',
                title: 'Are you sure?',
                text: 'You are about to delete this lesson.',
                showCancelButton: true,
                confirmButtonColor: 'rgba(220,38,38,0.2)',
                cancelButtonColor: 'rgba(220,38,38,100)',
                confirmButtonText: 'Delete',
                customClass: {
                    confirmButton: 'confirm-button-class',
                    cancelButton: 'cancel-button-class',
                },
            }).then((result) => {
                if (result.isConfirmed) {
                    var csrf_token = $('input[name=csrfmiddlewaretoken]').val();

                    // Make AJAX request to delete_lesson endpoint
                    $.ajax({
                        type: 'POST',
                        url: '/delete_lesson/' + cid + '/',
                        data: {
                            'csrfmiddlewaretoken': csrf_token
                        },
                        success: function (data) {
                            if (data.success) {
                                Swal.fire({
                                icon: 'success',
                                title: 'Deleted',
                                text: 'Lesson deleted permanently!',
                                showConfirmButton: false,
                            }).then((result) => {
                                if (result.isConfirmed || result.isDismissed) {
                                    location.reload();
                                }
                            });
                            } else {
                                Swal.fire({
                                    icon: 'error',
                                    title: 'Error',
                                    text: 'Error deleting course: ' + data.error
                                });
                            }
                        },
                        error: function (error) {
                            console.log("Error deleting courses:", error);
                        }
                    });
                }
            });
}
function delete_unit(){
            cid = unit_id;
            console.log('deleting unit id ', unit_id);
            // Confirm deletion using SweetAlert2
            Swal.fire({
                icon: 'warning',
                title: 'Are you sure?',
                text: 'It will also delete all the lesson under this unit.',
                showCancelButton: true,
                confirmButtonColor: 'rgba(220,38,38,0.2)',
                cancelButtonColor: 'rgba(220,38,38,100)',
                confirmButtonText: 'Delete',
                customClass: {
                    confirmButton: 'confirm-button-class',
                    cancelButton: 'cancel-button-class',
                },
            }).then((result) => {
                if (result.isConfirmed) {
                    var csrf_token = $('input[name=csrfmiddlewaretoken]').val();

                    // Make AJAX request to delete_lesson endpoint
                    $.ajax({
                        type: 'POST',
                        url: '/delete_unit/' + cid,
                        data: {
                            'csrfmiddlewaretoken': csrf_token
                        },
                        success: function (data) {
                            if (data.success) {
                                Swal.fire({
                                icon: 'success',
                                title: 'Deleted',
                                text: 'Unit deleted permanently!',
                                showConfirmButton: false,
                            }).then((result) => {
                                if (result.isConfirmed || result.isDismissed) {
                                    location.reload();
                                }
                            });
                            } else {
                                Swal.fire({
                                    icon: 'error',
                                    title: 'Error',
                                    text: 'Error deleting course: ' + data.error
                                });
                            }
                        },
                        error: function (error) {
                            console.log("Error deleting courses:", error);
                        }
                    });
                }
            });
}


$(document).on('submit', '#lessonForm', function (event) {
    event.preventDefault();

    // Get form data
    var formData = new FormData(this);

    // Perform AJAX request
    $.ajax({
        url: '/edit_lesson/' + lessonId + '/',
        method: 'POST',
        data: formData,
        processData: false,
        contentType: false,
        dataType: 'json',
        success: function (data) {
            // Check for success status and message
            if (data.success) {
                Swal.fire({
                    icon: 'success',
                    title: 'Success!',
                    text: data.message,
                    showConfirmButton: false,
                    timer: 2500
                });
            } else {
                Swal.fire({
                    icon: 'error',
                    title: 'Error!',
                    text: 'An error occurred while processing your request.',
                });
            }
        },
        error: function (error) {
            console.error('Error submitting form via AJAX:', error);
            Swal.fire({
                icon: 'error',
                title: 'Error!',
                text: 'An error occurred while processing your request.',
            });
        }
    });
});
$(document).on('submit', '#addLessonForm', function (event2) {
    event2.preventDefault();

    // Get form data
    var formData = new FormData(this);

    // Perform AJAX request
    $.ajax({
        url: '/add_lesson/',
        method: 'POST',
        data: formData,
        processData: false,
        contentType: false,
        dataType: 'json',
        success: function (data) {
            // Check for success status and message
            if (data.success) {
                Swal.fire({
                    icon: 'success',
                    title: 'Success!',
                    text: data.message,
                    showConfirmButton: false,
                    timer: 2500
                });
            } else {
                Swal.fire({
                    icon: 'error',
                    title: 'Error!',
                    text: 'An error occurred while processing your request.',
                });
            }
        },
        error: function (error) {
            console.error('Error submitting form via AJAX:', error);
            Swal.fire({
                icon: 'error',
                title: 'Error!',
                text: 'An error occurred while processing your request.',
            });
        }
    });
});
$(document).on('submit', '#addUnitForm', function (event3) {
    event3.preventDefault();

    // Get form data
    var formData = new FormData(this);

    // Perform AJAX request
    $.ajax({
        url: '/add_unit/',
        method: 'POST',
        data: formData,
        processData: false,
        contentType: false,
        dataType: 'json',
        success: function (data) {
            // Check for success status and message
            if (data.success) {
                Swal.fire({
                    icon: 'success',
                    title: 'Success!',
                    text: data.message,
                    showConfirmButton: false,
                    timer: 2500
                });
            } else {
                Swal.fire({
                    icon: 'error',
                    title: 'Error!',
                    text: 'An error occurred while processing your request.',
                });
            }
        },
        error: function (error) {
            console.error('Error submitting form via AJAX:', error);
            Swal.fire({
                icon: 'error',
                title: 'Error!',
                text: 'An error occurred while processing your request.',
            });
        }
    });
});
$(document).on('submit', '#editUnitForm', function (event4) {
    event4.preventDefault();

    // Get form data
    var formData = new FormData(this);

    // Perform AJAX request
    $.ajax({
        url: '/edit_unit/'+unit_id+'/',
        method: 'POST',
        data: formData,
        processData: false,
        contentType: false,
        dataType: 'json',
        success: function (data) {
            // Check for success status and message
            if (data.success) {
                Swal.fire({
                    icon: 'success',
                    title: 'Success!',
                    text: data.message,
                    showConfirmButton: false,
                    timer: 2500
                });
            } else {
                Swal.fire({
                    icon: 'error',
                    title: 'Error!',
                    text: 'An error occurred while processing your request.',
                });
            }
        },
        error: function (error) {
            console.error('Error submitting form via AJAX:', error);
            Swal.fire({
                icon: 'error',
                title: 'Error!',
                text: 'An error occurred while processing your request.',
            });
        }
    });

    
});
