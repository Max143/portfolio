from django.shortcuts import render, redirect
from .forms import SendMsgForm
import smtplib
import os
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

# Create your views here.


def SendMsgView(request):
    if request.method == 'GET':
        form = SendMsgForm()
        context = {'form':form}
        return render(request, 'portfolio/sendmsg.html', context)
    else:
        if request.method == 'POST':
            form = SendMsgForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['name']
                email = form.cleaned_data['email']
                person = form.cleaned_data['person']
                subject = form.cleaned_data['subject']
                msg = form.cleaned_data['msg']
            
                # here not working ------ message is appending to  send_mail()
                # Prepare actual message
                message = "Name: {0}, Email:{1}, Person Type:{2}, Subject:{3}, Message:{4}".format(name,email,person,subject,msg) 
                print(message)


                # Sending Mail Now # message 
                server = smtplib.SMTP("SMTP.gmail.com", 587)
                server.ehlo()
                server.starttls()
                server.ehlo()
                server.login('aoen143@gmail.com', '@emmawatson143@')
                server.sendmail('aoen143@gmail.com', ["manishgupta3950@gmail.com"], message)
                server.close()
                # message 
                messages.success(request, f"Thank you for sending msg. I'll get in touch with you ASAP.")
                return redirect('/portfolio')
            else:
                form = SendMsgForm()
                context = {'form':form}
                return render(request, 'portfolio/sendmsg.html')



def PortfolioView(request):
    return render(request, 'portfolio/portfolio.html')

    