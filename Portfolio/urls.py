from django.urls import path
from . import views


urlpatterns = [
    path('portfolio/', views.PortfolioView, name='portfolio'),
    path('send-msg/', views.SendMsgView, name='sendmsg'),



]