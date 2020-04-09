# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from inst.models import Inst

def hello(request):

    return render(request, 'index.html')

def hello_python(request):
    return render(request, 'python.html')

def sum_two(request, a, b):
    s = int(a)  + int (b)
    return HttpResponse(s)

def inst_list(request):
    instr = Inst.objects.all()
    return render(request, 'instructors.html', {"instructors_list" : instr})