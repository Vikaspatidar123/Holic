from django.shortcuts import render,redirect
from .models import Info
# Create your views here.
# https://dashboard.heroku.com/apps/teaholiccafe/deploy/github
# https://teaholiccafe.herokuapp.com/
def Index(request):
    if request.method=='GET':
        a=Info.objects.all()
        return render(request,'index.html',{'a':a})
    else:
        data=request.POST.get('data')
        milk=request.POST.get('milk')
        spend=request.POST.get('spend')
        ptm=request.POST.get('ptm')
        Case=request.POST.get('Case')
        Duy=request.POST.get('Duy')
        total=int(milk) + int(spend) + int(ptm) + int(Case) + int(Duy)
        print(total)
        cut=Info(data=data,Milk=milk,Other=spend,PTM=ptm,Case=Case,Duy=Duy,Total=total)
        cut.save()
        
        
        return redirect('home')

def Serach(request):
    if request.method=="POST":
        month=request.POST.get('month')
        all=request.POST.get('all')
        date=request.POST.get('date')
        if all:
            a=Info.objects.all()
            return render(request,'index.html',{'a':a})
        else:
            if date:
                a=Info.objects.filter(data=date)
                print(month,date)
                return render(request,'index.html',{'a':a})
            else:
                
                year,month=month.split('-')
                # month='-'.join(month)
                print(month) 
                a=Info.objects.filter(data__month=month,data__year=year)
                return render(request,'index.html',{'a':a})

