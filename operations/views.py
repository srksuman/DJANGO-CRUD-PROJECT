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
            sid = request.POST.get('student_id')
            if (sid==""):
                std_id = Student(full_name= request.POST['full_name'],address = request.POST['address'],phone_number = request.POST['phone_number'],field= request.POST['field'],picture= request.FILES['picture'])
            else:
                std_id = Student(id =int(sid),full_name= request.POST['full_name'],address = request.POST['address'],phone_number = request.POST['phone_number'],field= request.POST['field'],picture= request.FILES['picture'])
            std_id.save()
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
        

def edit_data(request):
    if request.method == "POST":
        print("suman")
        print(request.POST.get('id'))
        dt = Student.objects.get(id=int(request.POST.get('id')))
        full_name = dt.full_name
        address = dt.address
        phone_number = dt.phone_number
        field = dt.field
        img = dt.picture
        id = dt.id
        print(img)
        return JsonResponse({'result':1,'full_name':full_name,'address':address,'phone_number':phone_number,'field':field,'img':str(img),'id':id})
    else:
        return JsonResponse({"result":0})