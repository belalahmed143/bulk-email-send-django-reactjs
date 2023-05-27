from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from django.conf import settings
from django.core.mail import send_mass_mail
from .serializers import *
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST



class BulkEmailSendAPI(APIView):
    def post(self,request, *args, **kwargs):
        try:
            email = UserEmail.objects.all()
            my_email = []
            for i in email:
                my_email.append(i.email)

            subject = request.data.get('subject') 
            message = request.data.get('message')

            sendmail =  [(subject, message, f"<{settings.EMAIL_HOST_USER}>",[email]) for email in my_email]
            send_mass_mail(sendmail)
            return Response("successful send" ,status=HTTP_200_OK)
        except:
            return Response("somthing is wrong" ,status=HTTP_400_BAD_REQUEST)


