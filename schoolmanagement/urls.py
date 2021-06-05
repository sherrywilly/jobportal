"""
by sumit kumar
written by fb.com/sumit.luv

"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from school import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('delete_job/<int:pk>', views.delete_job, name='delete_job'),
    path('admin/', admin.site.urls),
    path('', views.home_view, name=''),

    path('recruterclick', views.recruterclick_view),
    path('studentclick', views.studentclick_view),



    path('studentsignup', views.student_signup_view, name='studentsignup'),
    path('recrutersignup', views.recruter_signup_view),


    path('studentlogin', LoginView.as_view(
        template_name='school/studentlogin.html')),
    path('recruterlogin', LoginView.as_view(
        template_name='school/recruterlogin.html')),


    path('afterlogin', views.afterlogin_view, name='afterlogin'),
    path('logout', LogoutView.as_view(
        template_name='school/index.html'), name='logout'),



    path('recruter-dashboard', views.recruter_dashboard_view,
         name='recruter-dashboard'),
    path('recruter-job-post', views.post_job, name='recruter-attendance'),
    path('students_list', views.students_list, name='students_list'),
    path('sent_mail/<int:pk>', views.sent_mail, name='sent_mail'),
    path('recruter_view_requests<int:pk>',
         views.recruter_view_requests, name='recruter_view_requests'),
    path('student-dashboard', views.student_dashboard_view,
         name='student-dashboard'),
    path('student-job-list', views.student_job_view, name='student-job-list'),
    path('make_a_request/<int:pk>',views.make_a_request,name='make_a_request'),
    path('aboutus', views.aboutus_view),
    path('contactus', views.contactus_view),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
