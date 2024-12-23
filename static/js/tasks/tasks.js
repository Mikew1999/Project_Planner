import { getCookie, handle_errors } from '../main.js';

let tasks_table;

export function get_tasks() {
    if (typeof tasks_table !== 'undefined') {
        tasks_table.destroy();
        tasks_table = undefined;
    }

    tasks_table = $('#tasks_table').DataTable({
        ajax: {
            url: '/Tasks/return_tasks',
            method: 'POST',
            cache: false,
            data: {
                project_id: 2,
                task_list_id: $('#task_list_dropdown').val(),
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
            { data: 'descr' },
            { data: 'Status' },
            { data: 'Task List' }
        ]
    })
}