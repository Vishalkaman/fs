from django.shortcuts import render
from django.views.generic.base import HttpResponse
from stud_reg_app.models import student, course
# Create your views here.


def student_list(req):
    students = student.objects.all()
    return render(req, 'student_list.html', {'students':students})


def course_list(req):
    courses = course.objects.all()
    return render(req, 'course_list.html', {'courses': courses})


def register(req):
    if req.method == 'POST':
        sid = req.POST.get('student')
        cid = req.POST.get('course')
        stu_ob = student.objects.get(id=sid)
        cou_ob = course.objects.get(id=cid)

        res = stu_ob.courses.filter(id=cid)
        if res:
            resp = "Student already registered"
            return HttpResponse(resp)
        stu_ob.courses.add(cou_ob)
        resp = "Student has been enrolled"
        return HttpResponse(resp)
    else:
        s = student.objects.all()
        c = course.objects.all()
        return render(req, 'register.html', {'students':s, 'courses':c})


def enrolled_list(req):
    if req.method == 'POST':
        cid = req.POST.get('enrolled')
        c_ob = course.objects.get(id = cid)
        s = c_ob.student_set.all()
        return render(req, 'enrolled_list.html', {'students':s})
    else:
        c = course.objects.all()
        return render(req, 'enrolled_list.html', {'courses':c})
