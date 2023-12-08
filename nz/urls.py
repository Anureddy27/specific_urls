from nz.views import*
from django.urls import path
app_name='kl'
urlpatterns=[
    path('williamson/',williamson,name='williamson'),
    path('ravindra/',ravindra,name='ravindra'),
]