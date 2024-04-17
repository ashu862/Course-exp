from django.shortcuts import render,HttpResponse
from . models import Jobs, Resume, Inquiry, Mail
from django.db.models import Q


# Create your views here.
def index(request):
    return render(request,'index.html') 

def jobs(request):
    if  request.method == 'POST':
        name = request.POST.get('name')
        exp = request.POST.get('exp')
        location = request.POST.get('location')
        emps = Jobs.objects.all()
        if name:
            emps = emps.filter(name__icontains=name)
        if exp:
            emps = emps.filter(exp=exp)
        if location:
            emps = emps.filter(location__icontains=location)
        
        context = {'emps': emps}
        return render(request, 'jobs.html', context)
    
    elif request.method == 'GET':
        emps = Jobs.objects.all()
        context = {'emps': emps}
        return render(request, 'jobs.html', context)
    
    else:
        return HttpResponse('Invalid occurrence')

def apply(request):
    return render(request,'apply.html') 




def form(request):
    if request.method == 'POST':
       full_name=request.POST['full_name']
       email=request.POST['email']
       phone=int(request.POST['phone'])
       resume_file=request.POST['resume_file']
       role = request.POST.get('role')
       new_emp=Resume(full_name=full_name, email=email, phone=phone, resume_file=resume_file, role=role)
       new_emp.save()
       return HttpResponse('application submitted succesfully')
    
    elif request.method == 'GET':
       return render(request, 'form.html')
    else:
       return HttpResponse('an error encountered,application cannot submitted')
    
def success(request):
    if request.method == 'POST' or request.method == 'GET':
        emps = Resume.objects.all()
        context = {'emps': emps}
        return render(request, 'success.html', context)
    else:
        return HttpResponse('an error occured')
    
def course(request):
    return render(request, 'course.html')
def course1(request):
    return render(request,'course1.html')

def data_ai(request):
    if request.method == 'POST':
        name= request.POST['name']
        email=request.POST['email']
        phone=int(request.POST['phone'])
        new_emp=Inquiry(name=name, email=email, phone=phone)
        new_emp.save()
        return HttpResponse('succesfully inquired!')
    elif request.method=='GET':
        return render(request, 'data_ai.html')
    else:    
        return HttpResponse('an exception occured!') 

def emailview(request):
    emps = Inquiry.objects.all()
    context = {
        'emps': emps
    }
    print(context)
    return render(request,'emailview.html', context) 

def fil_view(request):
    return render(request,'fil_view.html') 

def email(request):
    if request.method == 'POST':
        email=request.POST['email']
        new_emp=Mail(email=email)
        new_emp.save()
        return HttpResponse('succesfully email send!')
    elif request.method=='GET':
        return render(request, 'email.html')
    else:    
        return HttpResponse('an exception occured!')
    

def data_one(request):
    return render(request,'data_one.html') 


def data12(request):
    return render(request,'data12.html') 


def cybers(request):
    return render(request,'cybers.html') 


def cyber11(request):
    if request.method == 'POST':
        email=request.POST['email']
        new_emp=Mail(email=email)
        new_emp.save()
        return HttpResponse('succesfully email subscribed!')
    elif request.method=='GET':
        return render(request, 'cyber11.html')
    else:    
        return HttpResponse('an exception occured!')


def cyber12(request):
    return render(request,'cyber12.html')


def why1(request):
    if request.method == 'POST':
        email=request.POST['email']
        new_emp=Mail(email=email)
        new_emp.save()
        return render(request, 'why1.html') 
    elif request.method=='GET':
        return render(request, 'why1.html')
    else:    
        return HttpResponse('an exception occured!')

    

def why2(request):
    return render(request,'why2.html')

def why3(request):
    return render(request,'why3.html')

def why4(request):
    return render(request,'why4.html')


def p1(request):
    if request.method == 'POST':
        name= request.POST['name']
        email=request.POST['email']
        phone=int(request.POST['phone'])
        new_emp=Inquiry(name=name, email=email, phone=phone)
        new_emp.save()
        return HttpResponse('succesfully inquired! through email')
    elif request.method=='GET':
        return render(request, 'p1.html')
    else:    
        return HttpResponse('an exception occured!') 


def p2(request):
    return render(request,'p2.html')

def p3(request):
    return render(request,'p3.html')

def p4(request):
    return render(request,'p4.html')