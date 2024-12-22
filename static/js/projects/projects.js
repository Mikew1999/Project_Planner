import { getCookie } from "../main.js";

let projects_table;

export function get_projects() {
    if (typeof projects_table !== 'undefined') {
        $('#projects_table').DataTable.Destroy();
        projects_table = undefined;
    }

    projects_table = $('#projects_table').DataTable({
        ajax: {
            url: '/Projects/get_projects',
            method: 'POST',
            cache: false,
            data: {
                user_id: 451,
                'csrfmiddlewaretoken': getCookie("csrftoken")
            }
        },
        paging: true,
        serverside: false,
        searching: false,
        ordering: true,
        pageLength: 10,
        columns: [
            { data: 'name' },
            { data: 'completion_perc' },
            { data: 'edit' }
        ]
    })
}

function show_create_proj_modal() {
    $('#project_errors').empty();
    $('.proj_input').val("");
    $('#create_project_modal').modal('show');
}

$('#new_proj_btn').on('click', function() {
    show_create_proj_modal();
});

function edit_project_details(name, descr, start_date, deadline) {
    $.ajax({
        url: "/Projects/edit_project_details",
        method: "POST",
        cache: false,
        data: {
            'name': name,
            'descr': descr,
            'start_date': start_date,
            'deadline': deadline,
            'csrfmiddlewaretoken': getCookie("csrftoken")
        },
        dataType: "json",
        success: function(response) {
            console.log(response);
        },
        error: function(jqXHR, textStatus, errorThrown) {
            console.log(jqXHR, textStatus, errorThrown);
        }
    })
}

$('#save_new_project').on('click', function() {
    edit_project_details($('#project_name').val().trim(), $('#project_descr').val().trim(), $('#project_start_date').val(), $('#project_deadline').val());
});