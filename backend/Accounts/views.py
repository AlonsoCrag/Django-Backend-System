from django.http import HttpResponse, JsonResponse
from django.views.decorators import csrf
from django.views.decorators.csrf import csrf_exempt
# Model to save data
from . import models
# Module to hash the users passwords
from Hasher.HashPass import Hash, HashWithSalt
from Serializer.serializer import SerializeData
import time
from PIL import Image
from django.core.files.base import ContentFile
from django.core.files import File
from io import BytesIO
from django.core.files.base import ContentFile
from django.core.files import File
from io import BytesIO
#
import logging

logger = logging.getLogger(__name__)

@csrf_exempt
def Register(request):
    logger.debug(f"Request POST  data: {request.POST}, {request.FILES}")
    if request.method == 'POST':
        # req = request.POST
        print(request.POST, request.FILES)
        # req = eval(request.body.decode('utf-8'))
        req = request.POST
        # print("Incoming post request...", req)
        # print("Request body Encoded...", request.body.decode('utf-8'))
        # print("Request body Decoded...", request.body.decode('utf-8'))
        # If sending data through a post request, check if it comes from a form web app (POST) otherwise in (body) and deconde
        HashPass = Hash(req["password"])
        hashed, salt = HashPass.hash_data()
        print("Picture ->", request.FILES["picture"])
        print("Picture.FILE->", request.FILES["picture"].file)
        print("Picture.BUFFER ->", request.FILES["picture"].file.getbuffer())
        # print("Picture ->", request.FILES["picture"].file.read())
        # DATA = request.FILES["picture"].file.read()
        # DATA.seek(0)
        output = BytesIO(request.FILES["picture"].file.getbuffer())
        output.seek(0)
        content = ContentFile(output.read())
        _file = File(content)
        request.FILES["picture"].file = _file
        UserModel = models.Account(Username=req["username"], Password=str(hashed), Salt=str(salt), Email=req["email"], Picture=request.FILES["picture"])
        UserModel.save()
        return HttpResponse("TESTING THE REGISTER ROUTE")
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
    # time.sleep(5)
    logger.debug("---------------- > Logger is working in a django route < --------------")
    logging.info("This is a message to test")
    return HttpResponse('REST API - Mobile Application - 2022')


