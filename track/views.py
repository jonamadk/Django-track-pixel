from django.shortcuts import render

# Create your views here.




from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser , FormParser 
from rest_framework.response import Response
from rest_framework import status
from .models import *
import datetime
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication , TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse
from PIL import Image
from rest_framework.decorators import api_view

from django.template import Context
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMessage
import uuid
from django.http import HttpResponse ,HttpRequest
from PIL import Image
from django.urls import reverse





class SendTemplateMailView(APIView):



    def post(self, request, *args, **kwargs):

        email_list = ['manoj.adhikari@digiconnect.com.np', 'manoj@manojadhikary.com.np']

        for target_user_email in email_list:
            user = UserModel.objects.get(email = target_user_email)
            user.unique_code = uuid.uuid4()
            user.save()
            template = get_template("mail_template.html")
            context_data = dict()
            context_data["image_url"] = request.build_absolute_uri(("image_load"))
            print(context_data['image_url'])
            context_data['user']="Manoj"
            url_is = context_data["image_url"]+"/"+str(user.unique_code)+"/"
            context_data['url_is']= url_is
            html_text = template.render(context_data)
            email = user.email
            subject, from_email, to = "pixel" , 'postmaster@manojadhikary.com.np',  [target_user_email]

            msg = EmailMultiAlternatives(subject, html_text, from_email, to)
            msg.attach_alternative(html_text, "text/html")
            msg.content_subtype='html'
            msg.send()
            print("done", email)
            
        return Response({"success":True})


from .serializer import GetDataSerializer



class GetDataView(APIView):
    def get(self, request, *args, **kwargs):
        
        user = UserModel.objects.get(id = request.data.get('id'))
        serializer = GetDataSerializer(user)

        return Response({"Data":serializer.data})

        




@api_view()
def image_load(request, uuid_val):
   
    if request.method =='GET':
        print("\nImage Loaded\n")
        red = Image.new('RGB', (20, 20))
        response = HttpResponse(content_type="image/png" , status = status.HTTP_200_OK)
        user = UserModel.objects.get(unique_code= uuid_val)
        user.counter_is = "api_hit"
        user.save()
        red.save(response, "PNG")
        print("hit")
        return response
       

