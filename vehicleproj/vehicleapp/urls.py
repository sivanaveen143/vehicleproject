from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('register',views.register,name="register"),
    path('registrationvalidation',views.regvalidation,name="regvalidation"),
    path('mechanics/<str:email>',views.mechanics,name="mechanics"),
    path('verify/<str:email>',views.verify,name="verify"),
    path('validate',views.validate,name="validate"),
    path('sendrequest',views.sendrequest,name="sendrequest"),
]
