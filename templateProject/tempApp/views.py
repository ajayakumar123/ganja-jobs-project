from django.shortcuts import render
from django.http import HttpResponse
from tempApp.models import Student

# Create your views here.
def test_view(request):
    print("welcome",request)
    return render(request,'first.html')

def get_student_details(request):
    print("student information function")
    student_list=Student.objects.all()
    print("student list",student_list)

    student=Student.objects.get(name="jinna")
    print("student list2", student,type(student),student.marks)

    return render(request,'first.html',context={'student_list':student_list})
