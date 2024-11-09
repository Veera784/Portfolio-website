from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def experience (request):
    experience=[
        {"company":"COGNIZANT TECHNOLOGY SOLUTIONS",
         "position":"Senior Process Executive",
         "period":"Five years"},
        {"company":"SAVIC TECHNOLOGIES",
         "position":"Associate Consultant",
         "period":"One year"}
    ]
    return render (request,'experience.html',{'experience':experience})

def Projects  (request):
    Projects_show=[
        {
            "title": "Giftshop",
            "path": "images/Project-1.png",
        },
        {
            "title": "Portfolio_website",
            "path": "images/Project-2.png",
        },
        {
            "title": "Blood_Bank",
            "path": "images/Project-3.png",
        },
        {
            "title": "Django_REST API",
            "path": "images/Project-4.png",
        },
        {
            "title": "Employee Management System",
            "path": "images/Project-5.png",
        }
    ]
    return render(request,'Projects.html',{'Projects_show':Projects_show})

    
def certification (request):
    certification=[
        {"Cname":"PYTHON FULL STACK DEVELOPMENT",
         "institute":"Xplore IT corp"},
        {"Cname":"GAME CHANGER",
         "institute":"Cognizant"},
         {"Cname":"NETWORKING",
         "institute":"Kgcas"},
         {"Cname":"MS-OFFICE",
         "institute":"Kgcas"},
         {"Cname":"UNICORN",
         "institute":"Cognizant"},
         {"Cname":"KINAXIS",
         "institute":"Savic Technologies"}
    ]
    return render(request,'certification.html',{'certification':certification})
    
    
def contact (request):
    return render (request,'contact.html')