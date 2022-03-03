from django.shortcuts import render
from django.http import HttpResponse
from Accounts.models import Account

import logging

logger = logging.getLogger(__name__)

# Create your views here.
def DeleteClient(request, email):
    User = None
    try:
        User = Account.objects.get(Email=email)
    except:
        logger.info("User not found or doesnt exists, try again...")
        return HttpResponse("User not found or doesnt exists, try again...")
    logger.info(f"User found {User}")
    User.delete()
    return HttpResponse(f'User with email: {email} was found as {User}')