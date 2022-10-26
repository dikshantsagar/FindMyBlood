
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime

import pickle
import numpy as np



from .utils import distance

import matplotlib.pyplot as plt

import cv2
import os.path


import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

firebase_creds = os.environ['firebase_creds']
# with open("firebase_credentials.json", "w") as write_file:
#     json.dump(firebase_creds, write_file)

cred = credentials.Certificate(json.loads(firebase_creds))

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://blood-ed205-default-rtdb.firebaseio.com',
    'storageBucket': 'blood-ed205.appspot.com'
})


def loader(request):
    return render(request,'loader.html')


def index(request):
    

    # ref = db.reference('/users/')
    # users = ref.get()
    # print(users)
    # #print(type(ref.get()))
    # # ref.update({'user2':{'bloodgroup': 'A+', 'location': '(230,430)', 'name': 'kumar', 'password': 'pass123'}})
    # ref.update({'user1':{'bloodgroup': 'A+', 'location': '(230,430)', 'email': 'rahul@gmail.com', 'password': 'pass123'}})
    
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
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        utype = request.POST.get('type')

        dic = {'bloodgroup' : group, 'location':'('+lat+','+longi+')', 'name':name, 'email':email, 'password':password, 'phone':phone, 'gender':gender,'age':age,'type':utype}

        ref = db.reference('/users/')
        userind = int(list(sorted(list(ref.get()))[-1])[-1]) + 1
        dic['id'] = userind
        if request.POST.get('radio1'):
            r1 = request.POST.get('radio1')
            r2 = request.POST.get('radio2')
            r3 = request.POST.get('radio3')
            r4 = request.POST.get('radio4')

            if(r1=='1' and r2=='0' and r3=='0' and r4=='0'):
                dic['lastdonated'] = 'NA'
                dic['requests'] = {"request1":"something about request1"}
                
                
                ref.update({'user'+str(userind): dic})
                return render(request,'index.html',{'signuptoken': 1})
            else:
                return render(request,'index.html',{'signupfailure': 1})
        else:
            
            dic['history'] = {"history1":"something"}
            
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
        # print(users)
        # print("######",email,password)

        for i in users:
            if(users[i]['email'] == email and users[i]['password'] == password):
                return home(request,users[i])
                #return redirect('home',users[i])
        
        return render(request,'index.html',{'error':1})
        




@csrf_exempt
def donorlist(request):

    if request.method == 'POST':
        group = request.POST.get('group')
        print("session user")
        print(request.session['user'])
        uloc = np.array(list(map(float, request.session['user']['location'].strip('()').split(','))))
        ref = db.reference('/users/')
        donors = ref.get()
        dist = []
        reqdoner = []
        for i in donors:
            if donors[i]['bloodgroup'] == group and donors[i]['type']=='Donor':
                print('found')
                dloc = np.array(list(map(float, donors[i]['location'].strip('()').split(','))))
                dist.append(distance(uloc[0],dloc[0],uloc[1],dloc[1]))
                reqdoner.append(donors[i])


        donordist = zip(dist,reqdoner)
        donordist = sorted(donordist, key=lambda x: x[0])
        print(donordist)
        

        return render(request,'donorlist.html',{'donorlist':donordist,'user':request.session['user']})


def home(request,user):
    
    utype = user['type']
    if utype=="Reciever":
        history = [user['history'][i] for i in user['history']]
    else:
        history = [user['requests'][i] for i in user['requests']]
    request.session['user'] = user
    print(history)
    #add image

    if os.path.exists('static/uploads/'+str(request.session['user']['id'])+'.png'):
        return render(request,'home.html',{'user':user,'history':history,'pic':1})
    else:
        return render(request,'home.html',{'user':user,'history':history})

    


@csrf_exempt
def sendrequest(request):

    if request.method == 'POST':

        recid = request.POST.get('requesterid')
        recname = request.POST.get('requestername')
        donid = request.POST.get('donorid')
        print(recid,donid)
        date = datetime.today().strftime('%m/%d/%Y')

        ref = db.reference('/users/user'+str(donid)+"/requests/")
        dbref = ref.get()
        exists = 0
        for i in dbref:
            print(dbref[i])
            if dbref[i]['from'] == recname:
                exists = 1
        if exists == 0:
            reqind = int(list(sorted(list(ref.get()))[-1])[-1]) + 1
            dic = {'date':date,'from':recname,'recid':recid,'id':reqind}
            ref.update({'request'+str(reqind): dic})
        # print(ref.get(),histind)
        

    return HttpResponse()



@csrf_exempt
def handle_uploaded_file(f):
    
    print(f)


@csrf_exempt
def upload(request):


    if request.method == 'POST':

        img = cv2.imdecode(np.fromstring(request.FILES['files[]'].read(), np.uint8), cv2.IMREAD_UNCHANGED)
        cv2.imwrite('static/uploads/'+str(request.session['user']['id'])+'.png',img)
       
        
        
            

    return home(request,request.session['user'])
