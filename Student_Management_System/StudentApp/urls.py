from django.urls import path
from.import views

urlpatterns = [
    path('', views.log_fun, name = 'log'), # It will display login.html page
    path('logdata',views.logdata_fun), # It will read the data from login page

    path('reg', views.reg_fun, name  = 'reg'), # It will redirect to Registration.html page
    path('regdata', views.regdata_fun), # It will create superuser account

    path('home', views.home_fun, name = 'home'), # It will redirect to home.html

    path('add_students', views.addstudents_fun, name = 'add'), # It will redirect to addstudent.html
    path('readdata', views.readdata_fun), # It will insert records into student table

    path('display', views.display_fun, name = 'display'), # It will display student table data in display.html
    path('update/<int:id>', views.update_fun, name = 'up'), # It will update the student data
    path('delete/<int:id>', views.delete_fun, name = 'del'), # It will delete the student data
    path('log_out', views.log_out_fun, name = 'log_out'),
]
