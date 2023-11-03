from django.urls import path
from django import views
from . import views


urlpatterns = [
    path("type-creation", views.leave_type_creation, name="type-creation"),
    path("type-view", views.leave_type_view, name="type-view"),
    path("leave-type-individual-view/<int:id>", views.leave_type_individual_view, name="leave-type-individual-view"),
    path("type-update/<int:id>", views.leave_type_update, name="type-update"),
    path("type-delete/<int:id>", views.leave_type_delete, name="type-delete"),
    path("type-filter", views.leave_type_filter, name="type-filter"),
    path("request-creation", views.leave_request_creation, name="request-creation"),
    path(
        "leave-request-creation/<int:type_id>/<int:emp_id>",
        views.leave_request_creation,
        name="leave-request-creation",
    ),
    path("request-view", views.leave_request_view, name="request-view"),
    path(
        "request-approve/<int:id>", views.leave_request_approve, name="request-approve"
    ),
    path(
        "request-approve/<int:id>/<int:emp_id>",
        views.leave_request_approve,
        name="request-approve",
    ),
    path("request-cancel/<int:id>", views.leave_request_cancel, name="request-cancel"),
    path(
        "request-cancel/<int:id>/<int:emp_id>",
        views.leave_request_cancel,
        name="request-cancel",
    ),
    path("request-update/<int:id>", views.leave_request_update, name="request-update"),
    path("request-delete/<int:id>", views.leave_request_delete, name="request-delete"),
    path("user-request/<int:id>", views.user_leave_request, name="user-request"),
    path("request-filter", views.leave_request_filter, name="request-filter"),
    path("assign", views.leave_assign, name="assign"),
    path("assign-one/<int:id>", views.leave_assign_one, name="assign-one"),
    path("assign-view", views.leave_assign_view, name="assign-view"),
    path(
        "available-leave-update/<int:id>",
        views.available_leave_update,
        name="available-leave-update",
    ),
    path("assign-delete/<int:id>", views.leave_assign_delete, name="assign-delete"),
    path(
        "assigned-leave-bulk-delete",
        views.leave_assign_bulk_delete,
        name="assigned-leave-bulk-delete",
    ),
    path(
        "assign-leave-type-excel",
        views.assign_leave_type_excel,
        name="assign-leave-type-excel",
    ),
    path("assign-leave-type-info-import", views.assign_leave_type_import, name="assign-leave-type-info-import"),
    path("assigned-leaves-info-export", views.assigned_leaves_export, name="assigned-leaves-info-export"),
    path("assign-filter", views.leave_assign_filter, name="assign-filter"),
    path("holiday-view", views.holiday_view, name="holiday-view"),
    path("holidays-excel-template", views.holidays_excel_template, name="holidays-excel-template"),
    path("holidays-info-import", views.holidays_info_import, name="holidays-info-import"),
    path("holiday-info-export", views.holiday_info_export, name="holiday-info-export"),
    path("holiday-creation", views.holiday_creation, name="holiday-creation"),
    path("holiday-update/<int:id>", views.holiday_update, name="holiday-update"),
    path("holiday-delete/<int:id>", views.holiday_delete, name="holiday-delete"),
    path("holidays-bulk-delete", views.bulk_holiday_delete, name="holidays-bulk-delete"),
    path("holiday-filter", views.holiday_filter, name="holiday-filter"),
    path(
        "company-leave-creation",
        views.company_leave_creation,
        name="company-leave-creation",
    ),
    path("company-leave-view", views.company_leave_view, name="company-leave-view"),
    path(
        "company-leave-update/<int:id>",
        views.company_leave_update,
        name="company-leave-update",
    ),
    path(
        "company-leave-delete/<int:id>",
        views.company_leave_delete,
        name="company-leave-delete",
    ),
    path(
        "company-leave-filter", views.company_leave_filter, name="company-leave-filter"
    ),
    path("user-leave", views.user_leave_view, name="user-leave"),
    path("user-leave-filter", views.user_leave_filter, name="user-leave-filter"),
    path("user-request-view", views.user_request_view, name="user-request-view"),
    path(
        "user-request-update/<int:id>",
        views.user_request_update,
        name="user-request-update",
    ),
    path(
        "user-request-delete/<int:id>",
        views.user_request_delete,
        name="user-request-delete",
    ),
    path(
        "user-request-cancel/<int:id>",
        views.user_leave_cancel,
        name="user-request-cancel",
    ),
    path("one-request-view/<int:id>", views.one_request_view, name="one-request-view"),
    path("user-request-filter", views.user_request_filter, name="user-request-filter"),
    path("user-request-one/<int:id>", views.user_request_one, name="user-request-one"),
    path("employee-leave", views.employee_leave, name="employee-leave"),
    path("overall-leave", views.overall_leave, name="overall-leave"),
    path("leave-dashboard", views.dashboard, name="leave-dashboard"),
    path(
        "leave-employee-dashboard",
        views.employee_dashboard,
        name="leave-employee-dashboard",
    ),
    path("available-leaves", views.available_leave_chart, name="available-leaves"),
    path(
        "dashboard-leave-requests",
        views.dashboard_leave_request,
        name="dashboard-leave-requests",
    ),
    path(
        "employee-leave-chart", views.employee_leave_chart, name="employee-leave-chart"
    ),
    path(
        "department-leave-chart",
        views.department_leave_chart,
        name="department-leave-chart",
    ),
    path("leave-type-chart", views.leave_type_chart, name="leave-type-chart"),
    path("leave-over-period", views.leave_over_period, name="leave-over-period"),
    path("leave-request-create", views.leave_request_create, name="leave-request-create"),
    path('leave-allocation-request-view',
         views.leave_allocation_request_view,
         name='leave-allocation-request-view',
    ),
    path('user-leave-allocation-request-view',
         views.user_leave_allocation_request_view,
         name='user-leave-allocation-request-view',
    ),
    path(
        'leave-allocation-request-create',
        views.leave_allocation_request_create,
        name= "leave-allocation-request-create"
    ),
    path(
        'leave-allocation-request-filter',
        views.leave_allocation_request_filter,
        name= "leave-allocation-request-filter"
    ),
    path(
        'leave-allocation-request-single-view/<int:req_id>',
        views.leave_allocation_request_single_view,
        name= "leave-allocation-request-single-view"
    ),
    path(
        'leave-allocation-request-update/<int:req_id>',
        views.leave_allocation_request_update,
        name= "leave-allocation-request-update"
    ),
    path(
        'leave-allocation-request-approve/<int:req_id>',
        views.leave_allocation_request_approve,
        name= "leave-allocation-request-approve"
    ),
    path(
        'leave-allocation-request-reject/<int:req_id>',
        views.leave_allocation_request_reject,
        name= "leave-allocation-request-reject"
    ),
    path(
        'leave-allocation-request-delete/<int:req_id>',
        views.leave_allocation_request_delete,
        name= "leave-allocation-request-delete"
    ),

]
