from django.shortcuts import render, render_to_response,redirect,get_object_or_404
from django.db import transaction
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from . import models
from django.contrib import auth, messages
from login.models import user,report,hospital
from login.forms import UserForm, ReportForm
#from login.forms import PatientsinfoForm, ReportForm, EquipmentForm

# Create your views here.


def index(request):
    if request.method == "GET":
        allrep = report.objects.all()[:10]
    return render(request, 'login/index.html', { 'allrep' : allrep })


def login(request):
    if request.session.get('is_login',None):
        return redirect("/index/")
    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = "Please check again!"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = models.user.objects.get(name=username)
                if user.password == password:
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
                    request.session['user_levels'] = user.levels
                    return redirect('/index/')
                else:
                    message = "Wrong password!"
            except:
                message = "User is not existed!"
        return render(request, 'login/login.html', locals())

    login_form = UserForm()
    return render(request, 'login/login.html', locals())



def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("/index/")
    request.session.flush()
    # 或者使用下面的方法
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return redirect("/index/")


def creat(request):
    if request.method == "GET":
        rf = ReportForm()
        uf = UserForm()
        
        return render(request, 'login/creat.html',{ 'rf': rf ,  'uf': uf })
    elif request.method == "POST":
        rf = ReportForm(request.POST)
        if rf.is_valid():
            try:
                with transaction.atomic():
                    newrep = models.report.objects.create()
                    newrep.examnum = rf.cleaned_data['examnum']
                    newrep.name = rf.cleaned_data['name']
                    newrep.sex = rf.cleaned_data['sex']
                    newrep.age = rf.cleaned_data['age']
                    newrep.ageunit = rf.cleaned_data['ageunit']
                    newrep.position = rf.cleaned_data['position']
                    newrep.examtype = rf.cleaned_data['examtype']
                    newrep.method = rf.cleaned_data['method']
                    newrep.hospital = rf.cleaned_data['hospital']
                    newrep.indication = rf.cleaned_data['indication']
                    newrep.findings = rf.cleaned_data['findings']
                    newrep.comments = rf.cleaned_data['comments']
                    newrep.examdate = rf.cleaned_data['examdate']
                    newrep.reportdate = rf.cleaned_data['reportdate']
                    newrep.repdoctor = request.POST['repdoctor']
                    newrep.status = rf.cleaned_data['status']
                    newrep.save()

            except Exception as e:
                message ="Something wrong..."
        message = "Report saved."
    return redirect("/creat/")
            
def edit(request, nid):
    uf = UserForm()
    rfv = report.objects.get(pk = nid)
    if request.method == 'GET':
        if request.session['user_name'] == rfv.repdoctor :
            rf = ReportForm(initial={'name': rfv.name, 'examnum':rfv.examnum, 'sex':rfv.sex, 'age': rfv.age, 'ageunit':rfv.ageunit, 'position':rfv.position, 'examtype':rfv.examtype, 'method': rfv.method, 'hospital':rfv.hospital, 'indication':rfv.indication, 'findings':rfv.findings, 'comments':rfv.comments, 'examdate':rfv.examdate, 'reportdate':rfv.reportdate, 'status':rfv.status})
            return render(request, 'login/edit.html',{ 'nid':nid, 'rf': rf ,  'uf': uf })
    else: 
        rf = ReportForm(request.POST)
        if rf.is_valid():
            try:
                with transaction.atomic():
                    edrep = models.report.objects.get(pk = nid)
                    edrep.examnum = rf.cleaned_data['examnum']
                    edrep.name = rf.cleaned_data['name']
                    edrep.sex = rf.cleaned_data['sex']
                    edrep.age = rf.cleaned_data['age']
                    edrep.ageunit = rf.cleaned_data['ageunit']
                    edrep.position = rf.cleaned_data['position']
                    edrep.examtype = rf.cleaned_data['examtype']
                    edrep.method = rf.cleaned_data['method']
                    edrep.hospital = rf.cleaned_data['hospital']
                    edrep.indication = rf.cleaned_data['indication']
                    edrep.findings = rf.cleaned_data['findings']
                    edrep.comments = rf.cleaned_data['comments']
                    edrep.examdate = rf.cleaned_data['examdate']
                    edrep.reportdate = rf.cleaned_data['reportdate']
                    edrep.repdoctor = request.POST['repdoctor']
                    edrep.status = rf.cleaned_data['status']
                    edrep.save()
                    #return render(request, 'login/edit.html',{'nid':nid, 'rf':rf })
            except Exception as e:
                message ="Something wrong..."
        message = "Report saved."
    return redirect("/creat/")


    #else  message = "You are not allowed to edit other doctor's report!"

def print(request, nid):
    uf = UserForm()
    rfv = report.objects.get(pk = nid)
    if request.method == 'GET':
        if request.session['user_name'] == rfv.repdoctor :
            rf = ReportForm(initial={'name': rfv.name, 'examnum':rfv.examnum, 'sex':rfv.sex, 'age': rfv.age, 'ageunit':rfv.ageunit, 'position':rfv.position, 'examtype':rfv.examtype, 'method': rfv.method, 'hospital':rfv.hospital, 'indication':rfv.indication, 'findings':rfv.findings, 'comments':rfv.comments, 'examdate':rfv.examdate, 'repdoctor':rfv.repdoctor, 'reportdate':rfv.reportdate, 'status':rfv.status})
            if rfv.hospital =="2" :
                return render(request, 'login/CDHrep.htm',{ 'nid':nid, 'rf': rf ,  'uf': uf })
            elif rfv.hospital =="1" :
                return render(request, 'login/UTHrep.htm',{ 'nid':nid, 'rf': rf ,  'uf': uf })
    else: 
        return redirect("/creat/")    
