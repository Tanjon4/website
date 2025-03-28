from django.urls import path
from.views import home_page,about_page,service_page,contact_page,admin_page

urlpatterns = [
    path('',home_page, name= "app_home"),
    path('about/',about_page, name= "app_about"),
    path('service/',service_page, name= "app_service"),
    path('contact/',contact_page, name= "app_contact"),
    path('admins/',admin_page, name="app_admin")
]