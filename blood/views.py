from inspect import indentsize
from uuid import RFC_4122
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

import pickle
import numpy as np
import pandas as pd


import math

import matplotlib.pyplot as plt


import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("static/data/blood-ed205-firebase-adminsdk-eqmtk-2bffc253fb.json")

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://blood-ed205-default-rtdb.firebaseio.com'
})
def index(request):
    

    ref = db.reference('/users/')
    users = ref.get()
    print(users)
    #print(type(ref.get()))
    # ref.update({'user2':{'bloodgroup': 'A+', 'location': '(230,430)', 'name': 'kumar', 'password': 'pass123'}})
    ref.set({'user1':{'bloodgroup': 'A+', 'location': '(230,430)', 'email': 'rahul@gmail.com', 'password': 'pass123'}})
    
    return render(request,'index.html')


@csrf_exempt
def signup(request):

    if request.method == 'POST':
        typeval = request.POST.get('type')

        if(typeval == 'donor'):
            return render(request, 'signup.html',{'n' : range(18,99),'donor':1 })
        else:
            return render(request, 'signup.html',{'n' : range(18,99), 'rec':1 })
    
    # return render(request, 'signup.html',{'n' : range(18,99) })



@csrf_exempt
def signupworker(request):

    if request.method == 'POST':


        email = request.POST.get('email')
        password = request.POST.get('password')
        name = request.POST.get('name')
        lat = request.POST.get('lat')
        longi = request.POST.get('long')
        group = request.POST.get('group')
        phone = request.POST.get('phone')

        dic = {'bloodgroup' : group, 'location':'('+lat+','+longi+')', 'name':name, 'email':email, 'password':password, 'phone':phone}
        
        if request.POST.get('radio1'):
            r1 = request.POST.get('radio1')
            r2 = request.POST.get('radio2')
            r3 = request.POST.get('radio3')
            r4 = request.POST.get('radio4')

            if(r1=='1' and r2=='0' and r3=='0' and r4=='0'):
                ref = db.reference('/donors/')
                userind = int(list(sorted(list(ref.get()))[-1])[-1]) + 1
                ref.update({'donor'+str(userind): dic})
                return render(request,'index.html',{'signuptoken': 1})
            else:
                return render(request,'index.html',{'signupfailure': 1})
        else:
            ref = db.reference('/users/')
            userind = int(list(sorted(list(ref.get()))[-1])[-1]) + 1
            print(email, password, name, lat, longi, group)
            ref.update({'user'+str(userind): dic})
            #ref.update({str(email): dic})
            return render(request,'index.html',{'signuptoken': 1})


        

        
        
        


        
        
        

@csrf_exempt
def signin(request):   

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        ref = db.reference('/users/')
        users = ref.get()
        print(users)

        for i in users:
            if(users[i]['email'] == email and users[i]['password'] == password):
                return redirect('/home')
            else:
                return render(request,'index.html',{'error':1})
        





def donorlist(request):

    return render(request,'donorlist.html')


def home(request):

    return render(request,'home.html')