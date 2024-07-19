from django.shortcuts import render

# Create your views here.

def stu_fru(req):
    fruits = ["Lychee", "Lemon", "Banana"]
    students = ["Sonu", "Bow", "Moon"]

    return render(req, 'base.html', {'fruits':fruits, 'students':sorted(students)})
