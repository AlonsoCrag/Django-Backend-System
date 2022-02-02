from django.http import HttpResponse, JsonResponse
from django.views.decorators import csrf
from django.views.decorators.csrf import csrf_exempt
# Model to save data
from . import models
# Module to hash the users passwords
from Hasher.HashPass import Hash, HashWithSalt
from Serializer.serializer import SerializeData
import time

@csrf_exempt
def Register(request):
    if request.method == 'POST':
        # req = request.POST
        req = eval(request.body.decode('utf-8'))
        print("Incoming post request...", req)
        print("Request body Encoded...", request.body.decode('utf-8'))
        print("Request body Decoded...", request.body.decode('utf-8'))
        # If sending data through a post request, check if it comes from a form web app (POST) otherwise in (body) and deconde
        HashPass = Hash(req["password"])
        hashed, salt = HashPass.hash_data()
        UserModel = models.Account(Username=req["username"], Password=str(hashed), Salt=str(salt), Email=req["email"])
        UserModel.save()
    return JsonResponse(request.POST)



@csrf_exempt
def Login(request):
    if request.method == 'POST':
        print("Reques data in login", request.POST)
        req = request.POST
        QuerySet = models.Account.objects.filter(Email=req["email"])
        Data = SerializeData(QuerySet[0]).data
        print("Serialized data to login", Data)
        HashPass = HashWithSalt(req["password"], eval(Data["Salt"]))
        password = HashPass.hash_data()
        if password == eval(Data["Password"]):
            return JsonResponse(Data, status=200)
    return HttpResponse("Check if your data is right and try again please...", status=500)



def Test(request):
    time.sleep(5)
    return HttpResponse('Succesfully tested')