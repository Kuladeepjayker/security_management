from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.login, name = 'login'),
    path('login_validate/', views.login_validate, name = 'login_validate'),
    path('access_denied/', views.access_denied, name = 'access_denied'),
    path('logout/', views.logout, name = 'logout'),

    path('home/', views.home, name = 'home'),

    path('visitor/', views.visitor, name = 'visitor'),
    path('visitor/visitor_details/', views.visitor_details, name = 'visitor_details'),

    path('visitor_exit/', views.visitor_exit, name = 'visitor_exit'),

    path('staff_vehicle/', views.staff_vehicle, name = 'staff_vehicle'),
    path('staff_vehicle/staff_vehicle_details/', views.staff_vehicle_details, name = 'staff_vehicle_details'),

    path('staff_vehicle_exit/', views.staff_vehicle_exit, name = 'staff_vehicle_exit'),

    path('other_vehicle/', views.other_vehicle, name = 'other_vehicle'),
    path('other_vehicle/other_vehicle_details/', views.other_vehicle_details, name = 'other_vehicle_details'),
    path('export_data/', views.export_data, name = 'export_data'),
    path('export_data/get_excel/', views.get_excel, name = 'get_excel'),
    path('exit/', views.exit, name = 'exit'),
    path('check_for_exit/', views.check_for_exit, name = 'check_for_exit'),
    path('confirm_exit/', views.confirm_exit, name = 'confirm_exit')
]
