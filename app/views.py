from django.shortcuts import render
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from app.models import student
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
class studentlist(View):
    def get(self, request):
        # data=[
        #     {"Name": "Arun", "Age": 23,"Course":"Python","Marks":50},
        #     {"Name": "Amal", "Age": 24, "Course": "Java", "Marks":45},
        #     {"Name": "Anu", "Age": 24, "Course": "Java", "Marks":48}
        # ]

        s=list(student.objects.all().values()) #read all data records from student table
        print(s)
        print(type(s)) #Querysert of objects not python native


        return JsonResponse(s,safe=False)

#queryset ---> python native ---> Json
#Api creating a new student record
from json import loads

@method_decorator(csrf_exempt,name='dispatch')
class studentCreate(View):
    def post(self,request):
        # fetches data from client body
        form_data=request.body #json data

        #converts json data to python native type(dictionary)
        data = loads(form_data)
        # print(data)
        # creates a new record in db table
        n=data['name']
        a=data['age']
        c=data['course']
        m=data['marks']
        s=student.objects.create(Name=n,Age=a,Course=c,Marks=m)
        s.save()

        # returns jsonrespone
        return JsonResponse({"message":"Created"})
@method_decorator(csrf_exempt,name='dispatch')
class studentdetail(View):
    def get(self, request,i):
        # data={"Name": "Arun", "Age": 23,"Course":"Python","Marks":50}
        #reads data from student table matching with id i(modelobject)
        s=student.objects.filter(id=i)
        print(s)
        print(type(s))
        #converts the data into python native type
        data=list(s.values())
        print(data)
        print(type(data))
        #returns response
        return JsonResponse(data,safe=False)

#api view for deleting existing student records
@method_decorator(csrf_exempt,name='dispatch')
class studentdelete(View):
    def delete(self,request,i):
        #fetch the data from student table matching with id i
        s=student.objects.get(id=i)


        #delete the record
        s.delete()

        #returns response back to client
        return JsonResponse({"message":"Deleted"})
