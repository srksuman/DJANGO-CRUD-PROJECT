from django.http.response import JsonResponse
from django.shortcuts import render
from .forms import StudentForm
from django.http import HttpResponseRedirect
from . models import Student

# Create your views here.
def form_init(request):
    form = StudentForm()
    student = Student.objects.all()
    return render (request, 'html/index.html',{'form':form,'student':student})

def save_form(request):
    form = StudentForm(request.POST or None,request.FILES or None)
    if request.is_ajax():
        if form.is_valid():
            form.save()
            return JsonResponse({'process':'done'})
        else:
            error_list = form.errors.as_data()
            error_list_name = []
            error_list_value = []

            for i in error_list.keys():
                error_list_name.append(i)
                
                for j in error_list[i][0]:
                    error_list_value.append(j)
            return JsonResponse({'error_name':error_list_name,'error_value':error_list_value})
    else:
        return JsonResponse({'process':'error'})
