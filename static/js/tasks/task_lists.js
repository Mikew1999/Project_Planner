import { getCookie, handle_errors } from '../main.js'

let task_list_table;

let task_lists = {};

export function setup_task_list_dropdown() {
    $('#task_list_dropdown').empty();
    $('#task_list_dropdown').append('<option value="">-- All --</option>');
    for (let key in task_lists) {
        $('#task_list_dropdown').append('<option value="' + key + '">' + task_lists[key].name + '</option>');
    }
}

export function get_task_lists() {
    if (typeof task_list_table !== 'undefined') {
        task_list_table.destroy();
        task_list_table = undefined;
    }

    task_list_table = $('#task_list_table').DataTable({
        ajax: {
            url: '/Tasks/return_task_lists',
            method: 'POST',
            cache: false,
            data: {
                project_id: 2,
                'csrfmiddlewaretoken': getCookie("csrftoken")
            },
            dataSrc: function (json) {
                task_lists = {};
                if (json.success) {
                    for (let i = 0; i < json.data.length; i++) {
                        task_lists[json.data[i].id] = json.data[i];
                    }
                }
                setup_task_list_dropdown();
                return json.data;
            }
        },
        paging: true,
        serverside: false,
        searching: false,
        ordering: true,
        pageLength: 10,
        columns: [
            { data: 'name' },
            { data: 'descr' }
        ]
    })
}

function setup_list_modal(row_data={}) {
    $('.task_list_input').val("");
    $('#task_list_errors').empty();

    if (!Object.keys(row_data).length) {
        $('#task_list_id').val("0");
    } else {
        $('#task_list_id').val(row_data.id);
        $('#task_list_name').val(row_data.name);
        $('#task_list_descr').val(row_data.descr);
        $('#task_list_colour').val(row_data.color);
    }

    $('#task_list_modal').modal('show');
}

$('#create_list_btn').on('click', function() {
    setup_list_modal({});
});


function edit_task_list(name, descr, color) {
    $.ajax({
        url: "/Tasks/edit_task_list",
        method: "POST",
        cache: false,
        data: {
            'task_list_id': $('#task_list_id').val(),
            'task_list_name': name,
            'task_list_colour': color,
            'task_list_descr': descr,
            'csrfmiddlewaretoken': getCookie("csrftoken")
        },
        dataType: "json",
        success: function(response) {
            if (response.success) {
                $('#task_list_modal').modal('hide');
                get_task_lists();
            } else {
                handle_errors(response.message, response.errors, $('#task_list_errors'));
            }
        },
        error: function(jqXHR, textStatus, errorThrown) {
            console.log(jqXHR, textStatus, errorThrown);
            handle_errors("Something went wrong", [], $('#task_list_errors'));
        }
    })
}


$('#save_task_list').on('click', function() {
    edit_task_list($('#task_list_name').val().trim(), $('#task_list_descr').val().trim(), $('#task_list_colour').val());
});