from Hospital.models import hospital
from Patient.models import patient
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.shortcuts import render,redirect
from django.http import HttpResponse
from Hospital.models import hospitalactivity
from Patient.models import patientactivity
from django.contrib.sessions.models import Session
import  random
def home(request):

    return render(request,'home.html')


def aboutus(request):

    return render(request,'aboutus.html')

def contact(request):

    return render(request,'contact.html')

def news(request):

    return render(request,'news.html')

def services(request):

    return render(request,'services.html')


def login(request):
    return render(request,'login.html')



from django.contrib import messages
def valid(request):
    if request.method == 'POST':
        name=request.POST.get('occupation')
        email=request.POST.get('email')
        try:
             validate_email(email)

        except ValidationError:
            messages.add_message(request, messages.INFO, 'Invalid! Email or Email exists already please Enter Correctly')
            return render(request, 'login.html')

        password=request.POST.get('passd')
        if name=='Hospital' and hospital.objects.filter(hospitalemail=email).exists():
            help=hospital.objects.get(hospitalemail=email)
            pas=help.hospitalpassword
            nam=help.hospitalname
            hid=help.id
            profile=help.hospitalprofile


            user=hospitalactivity.objects.all().order_by ('?')[:10]
            user2=patientactivity.objects.all().order_by('?')[:10]



            if hospital.objects.filter(hospitalemail=email).exists() and pas == password:
                try:
                    request.session['logged']=nam
                    return render(request,'Hospital/hospitalhome.html',{"name":nam,'id':hid,'profile':profile,'activity':user,'activity2':user2})
                except:
                    return render(request, 'login.html')
            else:
                messages.add_message(request, messages.INFO, 'Email and Password donot match please Enter Corretctly')
                return render(request, 'login.html')


        elif name=='Patient' and patient.objects.filter(patientemail=email).exists():
            help = patient.objects.get(patientemail=email)
            pas = help.patientpassword
            nam = help.patientfirstname
            nam1 = help.patientlastname
            name=nam +' '+nam1
            num=help.citizennumber
            hid = help.id
            profile = help.patientprofile

            user = hospitalactivity.objects.all().order_by('?')[:10]
            user2 = patientactivity.objects.all().order_by('?')[:10]

            if patient.objects.filter(patientemail=email).exists() and pas == password:
                try:
                    request.session['logged'] = nam
                    return render(request, 'Patient/patienthome.html',{"name":name,'id':hid,'number':num,'profile':profile,'activity':user,'activity2':user2})
                except:
                    return render(request, 'login.html')
            else:
                messages.add_message(request, messages.INFO, 'Email and Password donot match please Enter Corretctly')
                return render(request, 'login.html')

        else:
            messages.add_message(request, messages.INFO, 'Incorrect Email please Enter Correctly')
            return render(request,'login.html')
    else:
        return render(request,'login.html')
def forget(request):
    return render(request,'forget.html')

def checkmail(request):
    if request.method == "POST":
        email=request.POST.get('email')
        if hospital.objects.filter(hospitalemail=email).exists() or patient.objects.filter(patientemail=email).exists():
            from django.core.mail import send_mail
            import random
            pins=str(random.randint(25734,99999))

            send_mail('Your Pin To Reset Password','Hey there,'
                                                   '\n We have received a request that you are trying to reset your account password.'
                                                   '\n Please use this PIN:'+ pins+''
                                                    '\n If you did not initiate this request,You can safely ignore this Email.'
                                                                                   '\n Greetings,\n Team Digital Report' ,'nepaldigital.report@gmail.com', [email],
                      fail_silently=False)


            return render(request,'re-enter.html',{'pin':pins,'email':email})

        else:
            messages.add_message(request, messages.INFO, 'Incorrect Email please Enter Correctly')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

def pinvalid(request):
    if request.method == "POST":
        enterpin = request.POST.get('enterpin')
        reqdpin = request.POST.get('submit')
        useremail = request.POST.get('email')
        if enterpin == reqdpin:
            return render(request,'passreset.html',{'email':useremail})

        else:
            messages.add_message(request, messages.INFO, 'Incorrect PIN please Enter Corretctly')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

def changepassword(request):
    if request.method == "POST":
        email=request.POST.get('email')
        pas1=request.POST.get('pas1')
        pas2=request.POST.get('pas2')
        if pas1 == pas2:
            if hospital.objects.filter(hospitalemail=email).exists():
                hmail=hospital.objects.get(hospitalemail=email)
                hmail.hospitalpassword = pas1
                hmail.save()
                return render(request, 'login.html')

            elif patient.objects.filter(patientemail=email).exists():
                pmail=patient.objects.get(patientemail=email)
                pmail.patientpassword = pas1
                pmail.save()
                return render(request, 'login.html')


        else:
            messages.add_message(request, messages.INFO, 'Password do not Match')
            return render(request,'passreset.html',{'email':email})
    else:
        return render(request, 'login.html')
