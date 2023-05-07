from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate,logout,login

def index(request):
    country = Country.objects.all()
    d = {'country': country}
    return render(request,'index.html',d)

def load_states(request):
    country_id = request.GET.get('country')
    states = State.objects.filter(country_id=country_id).order_by('name')
    return render(request, 'state_dropdown_list_options.html', {'states': states})

def load_districts(request):
    state_id = request.GET.get('state')
    districts = District.objects.filter(state_id=state_id).order_by('name')
    return render(request,'district_dropdown_list_options.html',{'districts':districts})

def load_cities(request):
    district_id = request.GET.get('district')
    city = City.objects.filter(district_id=district_id).order_by('name')
    return render(request,'city_dropdown_list_options.html',{'cities':city})

def submit_form(request):
    name=request.POST.get('name')
    country=Country.objects.get(id=request.POST.get('country'))
    state=State.objects.get(id=request.POST.get('state'))
    district=District.objects.get(id=request.POST.get('district'))
    city=City.objects.get(id=request.POST.get('city'))
    form=Form()
    form.name=name
    form.city=city
    form.district=district
    form.state=state
    form.country=country
    form.save()
    return redirect('index')
    

def show(request):
    form=Form.objects.all()
    return render(request,"show.html",{'form':form})