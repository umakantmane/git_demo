from django.shortcuts import render

# Create your views here.


def emp_example(request):

    return render(request, 'emp.html')