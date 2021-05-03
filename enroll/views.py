from django.shortcuts import render
from .forms import StudentRegistration
from .models import User
from django.http import JsonResponse

def home(request):
    form=StudentRegistration()
    stud=User.objects.all()
    return render(request,'enroll/home.html',{'form':form,'stu':stud})

def save_data(request):
    if request.method == "POST":
        form=StudentRegistration(request.POST)
        if form.is_valid():
            sid=request.POST.get('stuid')
            name=request.POST['name']
            email=request.POST['email']
            password=request.POST['password']
            if(sid==""):
                usr=User(name=name,email=email,password=password)
            else:
                usr=User(id=sid,name=name,email=email,password=password)
            usr.save()
            stud=User.objects.values()
            employee_data=list(stud)
            return JsonResponse({'status':'Save','employee_data':employee_data})
        else:
            return JsonResponse({'status':0})

def delete_data(request):
    if request.method=='POST':
        id=request.POST.get('sid')
        pi=User.objects.get(pk=id)
        pi.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})


def edit_data(request):
    if request.method=='POST':
        id=request.POST.get('sid')
        pi=User.objects.get(pk=id)
        employee_data={'id':pi.id,'name':pi.name,'email':pi.email,'password':pi.password}
        return JsonResponse(employee_data)
    