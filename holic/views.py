from django.shortcuts import render,redirect
from .models import Info
# Create your views here.
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