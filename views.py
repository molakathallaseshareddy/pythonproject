from django.db.models.fields import return_None
from django.shortcuts import render
from App.models import Bank,Transactions
# Create your views here.
def home(req):
    return render(req,'home.html')
def register(req):
    if req.method=='POST':
        a=req.POST.get('cid')
        b=req.POST.get('cname')
        c=req.POST.get('gender')
        d=req.POST.get('phno')
        e=req.POST.get('amount')
        f=req.POST.get('uname')
        g=req.POST.get('password')
        data=Bank(cid=a,cname=b,gender=c,phno=d,amount=e,uname=f,password=g)
        data.save()
        return render(req,'register.html',{'res':'Data is stored'})
    else:
        return render(req,'register.html')
def login(req):
    if req.method=='POST':
        a=req.POST.get('uname')
        b=req.POST.get('password')
        try:
            c=Bank.objects.get(uname=a,password=b)
            return render(req,'welcome.html')
        except Bank.DoesNotExist:
            return render(req,'login.html',{'res':'User Name and Password Invalid'})
    else:
        return render(req,'login.html')
def withdraw(req):
    if req.method=='POST':
        a=req.POST.get('cid')
        b=req.POST.get('type')
        c=req.POST.get('Amt')
        d=req.POST.get('date')
        try:
            r=Bank.objects.get(cid=a)
            r.amount=r.amount-int(c)
            r.save()
        except Bank.DoesNotExist:
            return render(req,'withdraw.html',{'w':'DoesNotExist'})
        res=Transactions(cid=a,type=b,Amt=c,date=d)
        res.save()
        return render(req,'withdraw.html',{'res':'Withdraw completed'})
    else:
        return render(req,'withdraw.html')
def deposit(req):
    if req.method=='POST':
        a=req.POST.get('cid')
        b=req.POST.get('type')
        c=req.POST.get('Amt')
        d=req.POST.get('date')
        r=Transactions(cid=a,type=b,Amt=c,date=d)
        r.save()
        try:
            res=Bank.objects.get(cid=a)
            res.amount=res.amount+int(c)
            res.save()
        except Bank.DoesNotExist:
            return render(req,'deposit.html',{'e':'Record Not Inserted'})
        return render(req,'deposit.html',{'d':'record is stored'})
    else:
        return render(req,'deposit.html')
def cust(req):
    if req.method=='POST':
        a=req.POST.get('cid')
        res=Transactions.objects.filter(cid=a)
        return render(req,'mini.html',{'res':res})
    else:
        return render(req,'mini.html')