from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import render, redirect, reverse
from django.views.decorators.csrf import csrf_exempt

from . import forms, models
from django.db.models import Sum
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.conf import settings
from django.core.mail import send_mail

from .filters import StudentFilter, JobFilter
from .models import Job, JobRequest, RecruterExtra, StudentExtra


def home_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request, 'school/index.html')


def recruterclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request, 'school/recruterclick.html')


def studentclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request, 'school/studentclick.html')


def student_signup_view(request):
    form1 = forms.StudentUserForm()
    form2 = forms.StudentExtraForm()
    mydict = {'form1': form1, 'form2': form2}
    if request.method == 'POST':
        form1 = forms.StudentUserForm(request.POST)
        form2 = forms.StudentExtraForm(request.POST)

        if form1.is_valid() and form2.is_valid():
            user = form1.save()
            user.set_password(user.password)
            user.save()
            f2 = form2.save(commit=False)
            f2.user = user
            user2 = f2.save()

            my_student_group = Group.objects.get_or_create(name='STUDENT')
            my_student_group[0].user_set.add(user)
        else:
            print('invalid value')
        return HttpResponseRedirect('studentlogin')
    return render(request, 'school/studentsignup.html', context=mydict)


def recruter_signup_view(request):
    form1 = forms.TeacherUserForm()
    form2 = forms.RecruterExtraForm()
    mydict = {'form1': form1, 'form2': form2}
    if request.method == 'POST':
        form1 = forms.TeacherUserForm(request.POST)
        form2 = forms.RecruterExtraForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            user = form1.save()

            user.set_password(user.password)
            user.save()

            f2 = form2.save(commit=False)
            f2.user = user
            user2 = f2.save()

            my_teacher_group = Group.objects.get_or_create(name='TEACHER')
            my_teacher_group[0].user_set.add(user)

        return HttpResponseRedirect('recruterlogin')
    return render(request, 'school/recrutersignup.html', context=mydict)


# for checking user is techer , student or admin
def is_admin(user):
    return user.groups.filter(name='ADMIN').exists()


def is_recruter(user):
    return user.groups.filter(name='TEACHER').exists()


def is_student(user):
    return user.groups.filter(name='STUDENT').exists()


def afterlogin_view(request):
    if request.user.is_staff:
        return redirect('/admin')
    elif is_recruter(request.user):
        accountapproval = models.RecruterExtra.objects.all().filter(
            user_id=request.user.id, status=True)
        if accountapproval:
            return redirect('recruter-dashboard')
        else:
            return render(request, 'school/recruter_wait_for_approval.html')
    elif is_student(request.user):
        accountapproval = models.StudentExtra.objects.all().filter(
            user_id=request.user.id, status=True)
        if accountapproval:
            return redirect('student-dashboard')
        else:
            return render(request, 'school/student_wait_for_approval.html')


@login_required(login_url='recruterlogin')
@user_passes_test(is_recruter)
def recruter_dashboard_view(request):
    recruter = RecruterExtra.objects.get(user=request.user)
    jobs = Job.objects.filter(recruter=recruter)
    teacherdata = models.RecruterExtra.objects.all().filter(
        status=True, user_id=request.user.id)

    mydict = {
        'jobs': jobs,
        'mobile': teacherdata[0].mobile,

    }
    return render(request, 'school/recruter_dashboard.html', context=mydict)


@login_required(login_url='recruterlogin')
@user_passes_test(is_recruter)
def post_job(request):
    EDUCATION = models.EDUCATION
    edu_list = []
    for edu in EDUCATION:
        print(edu)
        edu_list.append(edu[1])
    print(edu_list)
    if request.POST:
        recruter = RecruterExtra.objects.get(user=request.user)
        title = request.POST.get('title')
        salary = request.POST.get('salary')
        education = request.POST.get('education')
        print(education)
        email = request.POST.get('email')
        description = request.POST.get('description')
        job = Job(recruter=recruter, title=title, salary=salary,
                  education=education, email=email, description=description)
        job.save()
        messages.success(request, 'Job posted successfully')
    context = {'edu_list': edu_list}
    return render(request, 'school/post_job.html', context=context)


@login_required(login_url='recruterlogin')
@user_passes_test(is_recruter)
def students_list(request):
    students = StudentExtra.objects.all()
    filter = StudentFilter(request.GET, queryset=students)
    students = filter.qs
    context = {'students': students, 'filter': filter}
    return render(request, 'school/students_list.html', context)


@login_required(login_url='recruterlogin')
@user_passes_test(is_recruter)
def sent_mail(request, pk):
    student = StudentExtra.objects.get(id=pk)
    email = student.user.email
    if request.POST:
        message = request.POST.get('message')
        try:
            # send mail wont work unless
            send_mail(subject="Recruiter from JobPortal", recipient_list=[email], message=message, from_email=settings.EMAIL_HOST_USER,
                      fail_silently=False)
        except:
            messages.success(request, "email Sent successfully")
    context = {'name': student.user.first_name}
    return render(request, 'school/sent_mail.html', context)


@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def student_dashboard_view(request):
    studentdata = models.StudentExtra.objects.all().filter(
        status=True, user_id=request.user.id)

    mydict = {
        'student': studentdata[0],
    }
    return render(request, 'school/student_dashboard.html', context=mydict)


@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def student_job_view(request):
    job_requests = JobRequest.objects.filter(student=request.user)
    jr = []
    
    for i in job_requests:
        jr.append(i.Job.id)

    student = StudentExtra.objects.get(user=request.user)
    jobs = Job.objects.all()
    filter = JobFilter(request.GET, queryset=jobs)
    jobs = filter.qs
    return render(request, 'school/student_job_view'
                           '.html', {'jobs': jobs, 'filter': filter, 'student': student,'jr':jr})


def aboutus_view(request):
    return render(request, 'school/aboutus.html')


def contactus_view(request):
    sub = forms.ContactusForm()
    if request.method == 'POST':
        sub = forms.ContactusForm(request.POST)
        if sub.is_valid():
            email = sub.cleaned_data['Email']
            name = sub.cleaned_data['Name']
            message = sub.cleaned_data['Message']
            send_mail(str(name) + ' || ' + str(email), message, settings.EMAIL_HOST_USER, settings.EMAIL_RECEIVING_USER,
                      fail_silently=False)
            return render(request, 'school/contactussuccess.html')
    return render(request, 'school/contactus.html', {'form': sub})


def delete_job(request, pk):
    job = Job.objects.get(id=pk)
    job.delete()
    messages.success(request, 'Job deleted successfully')
    return redirect('recruter-dashboard')


def recruter_view_requests(request, pk):
    job = Job.objects.get(id=pk)
    job_requests = JobRequest.objects.filter(Job=job)
    context = {'job_requests': job_requests, 'job': job}
    return render(request, 'school/recruter_view_requests.html', context)


def make_a_request(request,pk):
    
    job = Job.objects.get(id=pk)
    user = request.user
    obj = JobRequest(Job=job,student=user)
    obj.save()
    return redirect('student-job-list')