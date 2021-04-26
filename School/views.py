from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .models import Student
from .forms import UserUpdateForm, StudentForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.core.files.storage import FileSystemStorage
from django.db.models import Q , Avg, Min, Max, Count, Sum
# Create your views here.

def studentview(request):
    if request.method == 'POST':
        forms = StudentForm()
    else:
        forms = StudentForm()
    return render(request, 'School/page.html', {'forms':forms})


def home(request):
    students = Student.objects.all() # delete
    # print('querystudent: ', students.query)
    return render(request, 'School/home.html', {'students':students,'data':'ahmed alaa ramadan'})

# @method_decorator(staff_member_required, name='dispatch')
class TemplateProfView(TemplateView):
    template_name = 'School/home.html'
    #
    # @method_decorator(staff_member_required)
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)

def inside(request):
    return render(request, 'base.html')



def update(request):
    if request.method == 'POST':
        forms = UserUpdateForm(request.POST, instance=request.user)
        if forms.is_valid():
            forms.save()
            return HttpResponse('<h1>Successful Update User</h1>')
    else:
        forms = UserUpdateForm(instance=request.user)
    return render(request, 'School/update.html', {'forms':forms})





#
# from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
# from rest_framework.generics import CreateAPIView
# from .serializers import StudentSerializer
#
# class StudentCreatAPIView(CreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#
#
#
# class StudentListApiView(ListAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#
# class StudentDetailAPIView(RetrieveAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     lookup_field = 'id'
#
#
# class StudentUpdateAPIView(UpdateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     lookup_field = 'id'
#
#
# class StudentDeleteAPIView(DestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     lookup_field = 'id'


def setsession(request):
    request.session['name'] = 'Ahmed'
    return render(request, 'School/set.html')

def getsession(request):
    # name = request.session['name']
    name = request.session.get('name', default='Default Name')
    keys = request.session.keys()
    items = request.session.items()
    age = request.session.setdefault('age',1000)
    return render(request, 'School/get.html', {'name':name,'keys':keys,'items':items,'age':age})


def delsession(request):
    request.session.flush()
    return render(request, 'School/del.html')















