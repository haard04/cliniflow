from django.shortcuts import render,redirect
from django.http import HttpResponse,FileResponse,Http404
import os
from django.contrib.auth.models import auth,User
from django.contrib import messages
from .forms import DiseaseMedicationForm
from .models import Disease,Medication
# Create your views here.
def home(request):
    return render(request, 'home.html')

def login(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(os.path.join(BASE_DIR, 'db.sqlite3'))
    if request.method =='POST':
        username= request.POST['username']
        password= request.POST['password']

        user= auth.authenticate(username = username,password=password)
        
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')
    else:
        return render(request,'login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('/')

def sp(request):
    return render(request, 'sphome.html')

def ca(request):
    return render(request, 'cahome.html')

def doctor_speech(request):
    # Your view logic for the doctor panel
    return render(request, 'doctor_speech.html')

def staff_speech(request):
    # Your view logic for the staff panel
    return render(request, 'staff_speech.html')

def doctor_custom(request):
    # Your view logic for the doctor panel in custom approach
    return render(request, 'doctorCustom.html')

def staff_custom(request):
    # Your view logic for the staff panel in custom approach
    return render(request, 'staffCustom.html')

from django.shortcuts import render, redirect
from .forms import DiseaseMedicationForm
from .models import Disease, Medication

def add_disease_medication(request):
    if request.method == 'POST':
        form = DiseaseMedicationForm(request.POST)
        if form.is_valid():
            disease_name = form.cleaned_data['disease_name']
            new_medications = form.cleaned_data['new_medications'].split(',')
            
            if disease_name:
                disease, created = Disease.objects.get_or_create(name=disease_name)
                for med_name in new_medications:
                    med_name = med_name.strip()
                    if med_name:
                        medication, created = Medication.objects.get_or_create(name=med_name)
                        disease.preset_medications.add(medication)
            else:
                disease = None
            
            return redirect('presets')
    else:
        form = DiseaseMedicationForm()
    
    return render(request, 'presets.html', {'form': form})

def all_presets(request):
    presets = Disease.objects.all()
    return render(request, 'all_presets.html', {'presets': presets})