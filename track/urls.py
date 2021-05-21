from django.urls import path , include
from .views import SendTemplateMailView , image_load , GetDataView
from django.conf.urls.static import static
from django.conf import settings




urlpatterns = [
    
    path('send/image_load/<str:uuid_val>/',image_load, name='image_load'),
    path('data/',GetDataView.as_view()),
    
    path('send/', SendTemplateMailView.as_view(), name= 'send_template'),
]

