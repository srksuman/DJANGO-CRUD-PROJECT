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
            all_data = Student.objects.values()
            print(all_data)
            return JsonResponse({'process':'done','all_data':list(all_data)})
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


def delete_data(request):
    if request.method == 'GET':
        id = int(request.GET.get('id'))
        dt = Student.objects.get(id=id)
        dt.delete()
        return JsonResponse({"result":"success"})
    else:
        return JsonResponse({"result":"failed"})
        