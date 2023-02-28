from django.shortcuts import render
from django.http import HttpResponse
from .models import customer,mobilelist,brand,contac,feed
from django.contrib import messages
from autoscraper import AutoScraper
from .models import PredResults
import pickle
# Create your views here.


def home(request):
    mob_dict = {'mob':mobilelist.objects.all()}
    return render(request,'index.html', mob_dict)

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method=='POST':
        Name=request.POST['Name']
        Email=request.POST['Email']
        Phone = request.POST['Phone']   
        Message=request.POST['Message']
        

        contac(Name=Name, Email=Email,Phone = Phone, Message=Message).save()
        messages.success(request,'The New Message is saved Successfully...!')
        return render(request,'contact.html')
    
    else:
        return render(request, 'contact.html')

    

def mobile(request):
    mob_dict = {'mob':mobilelist.objects.all()}
    return render(request,'mobile.html',mob_dict)

def laptop(request):
    return render(request,'laptop.html')

def product(request):
    logo = {'b':brand.objects.all()}
    return render(request,'product.html',logo)

def register(request):
    if request.method=='POST':
        name=request.POST['name']
        phone = request.POST['phoneno']   
        email=request.POST['email']
        password=request.POST['password']

        emailExist = customer.objects.filter(email = email)
        phoneExist = customer.objects.filter(phone = phone)

        if(emailExist):
            messages.success(request,"E-mail Id already exist...!")
            return render(request,'register.html')
        elif(phoneExist):
            messages.success(request,"Phone number already exist...!")
            return render(request,'register.html')
        else:
            customer(name=name, phone = phone, email=email,password=password).save()
            messages.success(request,'The New customer '+request.POST['name']+" is saved Successfully...!")
            return render(request,'login.html')
    
    else:
        return render(request,'register.html') 

def fb(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']

        feed(name=name,email=email,message=message).save()
        messages.success(request,"Feedback sended Successfully...!")
        return render(request,'fb.html')
    
    else:
        return render(request,'fb.html') 


def login(request):
    if request.method=="POST":
       
        try:
            Userdetails=customer.objects.get(email=request.POST['email'],password=request.POST['password'])
            print("Username=",Userdetails)
            request.session['email']=Userdetails.email
            return render(request,'prediction.html')
        except customer.DoesNotExist as e:
            messages.success(request,'Username/Password Invalid...!')
    return render (request,'login.html')  

def logout(request):
    try:
        del request.session['email'] 
    except: 
        return render(request,'index.html')
    return render(request,'index.html')

def prediction(request):
    return render(request, 'prediction.html')




def aggreslt(result):
    final_result = []
    print(list(result.values())[0])
    for i in range(len(list(result.values())[0])):
        try:
            
            final_result.append({alias: result[alias][i] for alias in result})
        except:
            pass
    return (final_result)


def amzsearch(request):
    amazon_scraper = AutoScraper( )
    amazon_scraper.load('C:/Users/Atees/Desktop/amazon/static/amazonsearch')
    url = 'https://www.amazon.in/s?k=/?q=' + request.POST['query']
    result = amazon_scraper.get_result_similar(url, group_by_alias=True)
    r = aggreslt(result)
    print(r)
    return render(request, 'res.html',{'result':r})



def getPrediction(battery_power,blue,clock_speed, dual_sim,fc,four_g,int_memory,m_dep,mobile_wt,n_cores, pc,px_height,px_width,ram, sc_h,sc_w,talk_time,three_g,touch_screen,wifi):
    model=pickle.load(open("C:/Users/Atees/Desktop/amazon/product/Amazon_model.sav",'rb'))
    scaled=pickle.load(open("C:/Users/Atees/Desktop/amazon/product/scaler_Amazon.sav","rb"))
    prediction=model.predict(scaled.transform([[battery_power,blue,clock_speed, dual_sim,fc,four_g,int_memory,m_dep,mobile_wt,n_cores, pc,px_height,px_width,ram, sc_h,sc_w,talk_time,three_g,touch_screen,wifi]]))
    if prediction==0:
        return "5000"
    elif prediction==1:
        return "10000"
    elif prediction==2:
        return "50000"
    elif prediction==3:
        return "100000"


    else:
        return "error"      

    return prediction
    print("$$$$")
    print("hello",prediction)
def result(request):
    battery_power = float(request.GET['battery_power'])
    blue = float(request.GET['blue'])
    clock_speed = float(request.GET['clock_speed'])
    dual_sim = float(request.GET['dual_sim'])
    fc = float(request.GET['fc'])
    four_g = float(request.GET['four_g'])
    int_memory = float(request.GET['int_memory'])
    m_dep = float(request.GET['m_dep'])
    mobile_wt= float(request.GET['mobile_wt'])
    n_cores=float(request.GET['n_cores'])
    pc=float(request.GET['pc'])
    px_height=float(request.GET['px_height'])
    px_width=float(request.GET['px_width'])
    ram=float(request.GET['ram'])
    sc_h=float(request.GET['sc_h'])
    sc_w=float(request.GET['sc_w'])
    talk_time=float(request.GET['talk_time'])
    three_g=float(request.GET['three_g'])
    touch_screen=float(request.GET['touch_screen'])

    wifi=float(request.GET['wifi'])




    result=getPrediction(battery_power,blue,clock_speed, dual_sim,fc,four_g,int_memory,m_dep,mobile_wt,n_cores, pc,px_height,px_width,ram, sc_h,sc_w,talk_time,three_g,touch_screen,wifi)
    return render(request,'result.html',{'res':result})



def forgotPassword(request):
    return render (request,'forgot-password.html')

def updatePassword(request):
    email = request.POST['email']
    password = request.POST['password']
    
    checkAccountExistOrNot = customer.objects.filter(email = email)
    if checkAccountExistOrNot:
        customer.objects.filter(email = email).update(password = password)
        messages.success(request,"Password updated Successfully...!")
        return render(request,'login.html')
    else:
        messages.success(request,"No account found on this E-mail Id...!")
        return render (request,'forgot-password.html')



