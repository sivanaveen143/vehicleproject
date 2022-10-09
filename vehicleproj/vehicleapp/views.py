import email
from django.shortcuts import render, redirect
from .models import userdetail, vmechanic
import smtplib,ssl
from email.mime.text import MIMEText
from math import sin, cos, atan2, radians,sqrt
# Create your views here.
def index(request):
    return render(request,"index.html")

def register(request):
    return render(request,"register.html")

def regvalidation(request):
    if request.method == "POST":
        username = request.POST.get('uname')
        password = request.POST.get('pswd')
        phone = request.POST.get('phn')
        email = request.POST.get('email')
        role = request.POST.get('role')
        if role == "customer":
            obj = userdetail.objects.all()
            latitude = request.POST.get('lat')
            longitude = request.POST.get('lon')
            length = len(obj)
            if latitude == "NA" or longitude == "NA":
                return render(request,"register.html",{"error":"please turnon device location"})
            for i in range(length):
                if email == obj[i].email or phone == obj[i].phone:
                    return render(request,"register.html",{"error":"email or phone number already registered..."})
            obj1 = userdetail()
            obj1.username = username
            obj1.password = password
            obj1.phone = phone
            obj1.email = email
            obj1.role = role
            obj1.latitude = latitude
            obj1.longitude = longitude
            obj1.save()
            length = len(email)
            en_email = ""
            for i in range(length):
                en_email += chr(ord(email[i])+7)
            s = smtplib.SMTP('smtp.gmail.com',587)
            msg = """\
                <html>
                    <h2>This mail from <br><br>
                    Here is yours verification link </h2>
                    <a href="http://127.0.0.1:8000/verify/{}">verify its you</a>
                </html>
            """.format(email)
            msg = MIMEText(msg,"html")
            context = ssl.create_default_context()
            s.starttls(context=context)
            s.login('backbenchers143.rgm@gmail.com','lgwnnimpsvzbblue')
            s.sendmail('backbenchers143.rgm@gmail.com',email,msg.as_string())
            s.quit()
            return render(request,"index.html",{"error":"mail was sent please verify your account"})
        else:
            obj = vmechanic.objects.all()
            latitude = request.POST.get('lat')
            longitude = request.POST.get('lon')
            length = len(obj)
            if latitude == "NA" or longitude == "NA":
                return render(request,"register.html",{"error":"please turnon device location"})
            for i in range(length):
                if email == obj[i].email or phone == obj[i].phone:
                    return render(request,"register.html",{"error":"email or phone number already registered..."})
            obj1 = vmechanic()
            obj1.username = username
            obj1.password = password
            obj1.phone = phone
            obj1.email = email
            obj1.role = role
            obj1.latitude = latitude
            obj1.longitude = longitude
            obj1.save()
            length = len(email)
            en_email = ""
            for i in range(length):
                en_email += chr(ord(email[i])+7)
            s = smtplib.SMTP('smtp.gmail.com',587)
            msg = """\
                <html>
                    <h2>This mail from <br><br>
                    Here is yours verification link </h2>
                    <a href="http://127.0.0.1:8000/mechanics/{}">verify its you</a>
                </html>
            """.format(email)
            msg = MIMEText(msg,"html")
            context = ssl.create_default_context()
            s.starttls(context=context)
            s.login('backbenchers143.rgm@gmail.com','lgwnnimpsvzbblue')
            s.sendmail('backbenchers143.rgm@gmail.com',email,msg.as_string())
            s.quit()
            return render(request,"index.html",{"error":"mail was sent please verify your account"})
    return render(request,"index.html",{"error":"Enter valid details"})
def verify(request,email):
    try:
        obj = userdetail.objects.get(email=email)
        obj.status = "active"
        obj.save()
        return render(request,"verified.html")
    except Exception as e:
        print(e)
        return render(request,"index.html",{"error":"email not registered"})
def mechanics(request,email):
    print(email)
    try:
        obj1 = vmechanic.objects.get(email=email)
        obj1.status = "active"
        obj1.save()
        return render(request,"verified.html")
    except Exception as e:
        print(e)
        return render(request,"index.html",{"error":"email not registered"})

def validate(request):
    if request.POST.get('role') == "customer":
        try:
            email = request.POST.get('email')
            password = request.POST.get('pswd')
            obj = userdetail.objects.get(email=email)
            print(obj.password, password)
            if obj.password == password and obj.status == "active":
                request.session['email']  = email
                return render(request,"customer.html")
            else:
                return render(request,"index.html",{"error":"password invalid"})
        except Exception as e:
            print(e)
            return render(request,'index.html',{"error":"email not registered.."})
    else:
        try:
            email = request.POST.get('email')
            password = request.POST.get('pswd')
            obj = vmechanic.objects.get(email=email)
            print(obj.password, password)
            if obj.password == password and obj.status == "active":
                request.session['email']  = email
                return render(request,"mechanic.html")
            else:
                return render(request,"index.html",{"error":"password invalid or account not activated check email to activate account"})
        except Exception as e:
            print(e)
            return render(request,'index.html',{"error":"email not registered.."})
def sendrequest(request):
    latitude = request.POST.get('latitude')
    longitude = request.POST.get('longitude')
    
    if latitude == "NA" or longitude == "NA":
        return redirect("customer",{"error":"turon device location"})
    email = request.session['email']
    obj = userdetail.objects.get(email = email)
    if obj.requested == "none":
        obj.requested = "requested"
        obj.save()
        latitude = obj.latitude
        longitude = obj.longitude
        print("requested : ",latitude,longitude)
        R = 6373.0
        lat1 = radians(float(latitude))
        lon1 = radians(float(longitude))
        min_distance = 100000
        j=0
        mech_obj = vmechanic.objects.all()
        length = len(mech_obj)
        for i in range(length):
            lat2 = radians(float(mech_obj[i].latitude))
            lon2 = radians(float(mech_obj[i].longitude))
            dlon = lon2 - lon1
            dlat = lat2 - lat1

            a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
            c = 2 * atan2(sqrt(a), sqrt(1 - a))
            distance = R * c
            print("distance :",distance)
            if distance < min_distance:
                min_distance = distance
                mech = mech_obj[i].email
                j = i
        mech_obj[j].response = "work alloted"
        msg = """\
        <h2>customer details</h2><br>
        Email : {}<br>
        Phone : {}<br>
        latitude : {}<br>
        longitude : {}<br>
        """.format(email,obj.phone,obj.latitude,obj.longitude)
        msg = MIMEText(msg,'html')
        s = smtplib.SMTP('smtp.gmail.com',587)
        context = ssl.create_default_context()
        s.starttls(context = context)
        s.login('backbenchers143.rgm@gmail.com','lgwnnimpsvzbblue')
        s.sendmail('backbenchers143.rgm@gmail.com',mech,msg.as_string())
        msg = """\
        <h2>mechanic details</h2><br>
        Email : {}<br>
        Phone : {}<br>
        latitude : {}<br>
        longitude : {}<br>
        """.format(mech,mech_obj[j].phone,mech_obj[j].latitude,mech_obj[j].longitude)
        msg = MIMEText(msg,'html')
        s.sendmail('backbenchers143.rgm@gmail.com',email,msg.as_string())
        s.quit()
        return render(request,"customer.html",{"error":"mechanic details sent to your mail account"})
    else:
        return render(request,"customer.html",{"error":"request already sent"})
    