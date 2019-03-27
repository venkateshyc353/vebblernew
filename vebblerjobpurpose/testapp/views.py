from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . forms import v_iosinfoo,v_coustmerinfo,v_serviceinfo,v_jobinfoo

def vebbler_home(request):
    return render(request,'testapp/base.html')

@login_required
def vebbler_job(request):
    return render(request,'testapp/job.html')
@login_required
def vebbler_servies(request):
    if request.method=='POST':
        form=v_serviceinfo(request.POST)
        if form.is_valid():
            form.save()
    form=v_serviceinfo()
    return render(request,'testapp/service.html',{'form':form})
@login_required
def vebbler_ios_app(request):
    return render(request,'testapp/ios.html')
@login_required
def vebbler_empolyes(request):
    return render(request,'testapp/empolyees.html')
@login_required
def vebbler_coustmer(request):
    if request.method=='POST':
        form=v_coustmerinfo(request.POST)
        if form.is_valid():
            form.save()
            return vebbler_home(request)
    form=v_coustmerinfo()
    return render(request,'testapp/coustmers.html',{'form':form})
from django.http import HttpResponse
def fox(request):
    b=v_coustmerinfo()
    return render(request,'testapp/for.html',{'b':b})

@login_required()
def vebbler_homm(request):
    return render(request,'testapp/home.html')