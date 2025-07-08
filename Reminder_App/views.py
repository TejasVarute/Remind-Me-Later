from django.shortcuts import render, redirect, get_object_or_404
from .form import Form
from .models import Reminder, PastReminder
from login.decorators import login_required_custom
from login.models import UserData, Developer
from datetime import datetime

#Custom login required decorator
@login_required_custom
def reminder(request):
    user = get_object_or_404(UserData, id=request.session.get('user_id'))
    context = {'form' : Form, 'user' : user, 'reminders' : {}, 'developer' : Developer.objects.get()}
    
    #GET method for show reminders on webpage
    if request.method == "GET":
        reminders = Reminder.objects.filter(user=user)
        
        #Getting all reminders from database
        for reminder in reminders:
            msg, loc, date_str = str(reminder).split('@')
            date_part, time_part = date_str.strip().split()
            time = time_part[:5]
            
            date_obj = datetime.strptime(date_part, "%Y-%m-%d").strftime("%d %B %Y")
            date_time = f'{date_part} {time}'
            
            #Moving and deleting old reminders from database
            current = datetime.now().strftime("%Y-%m-%d %H:%M")
            if date_time < current:
                old_reminders = Reminder.objects.filter(date_time = date_time)
                
                for remind in old_reminders:
                    PastReminder(user=user, 
                                 date_time=remind.date_time, 
                                 location=remind.location, 
                                 message=remind.message).save()
                old_reminders.delete()

            #Storing upcomming reminders into dictionary
            try:
                if context['reminders'][str(date_obj)]: 
                    context['reminders'][str(date_obj)].append({'msg' : msg, 'loc' : loc, 'time' : time, "datetime" : date_time})
            except: 
                context['reminders'][str(date_obj)] = [{'msg' : msg, 'loc' : loc, 'time' : time, "datetime" : date_time}]
        
        #Sorting the time
        for date in context['reminders']:
            context['reminders'][date].sort(key=lambda x: datetime.strptime(x['time'], "%H:%M"))
        #Sorting the dates
        context['reminders'] = dict(sorted(context['reminders'].items(), key=lambda items : datetime.strptime(items[0], "%d %B %Y")))
        return render(request, 'my_Reminders.html', context)
    
    #POST method for get the reminder details from webpage
    elif request.method == "POST":
        form = Form(request.POST)
        if form.is_valid() and request.session.get('user_id'):
            date_time = request.POST['date_time']
            location = request.POST['location']
            message = request.POST['message']
            
            Reminder(user=user, date_time=date_time, location=location, message=message).save()
        return redirect('reminder:my_reminder')

@login_required_custom
def old_reminder(request):
    user = get_object_or_404(UserData, id=request.session.get('user_id'))
    context = {'user':user, 'reminders' : {}, 'developer' : Developer.objects.get()}
    
    #Getting all Reminders
    reminders = PastReminder.objects.filter(user=user)
    for reminder in reminders:
        msg, loc, date_str = str(reminder).split('@')
        date_part, time_part = date_str.strip().split()
        time = time_part[:5]
        
        date_obj = datetime.strptime(date_part, "%Y-%m-%d").strftime("%d %B %Y")
        date_time = f'{date_part} {time}'
        try:
            if context['reminders'][str(date_obj)]: 
                context['reminders'][str(date_obj)].append({'msg' : msg, 'loc' : loc, 'time' : time, "datetime" : date_time})
        except: 
            context['reminders'][str(date_obj)] = [{'msg' : msg, 'loc' : loc, 'time' : time, "datetime" : date_time}]

    #Sorting the time
    for date in context['reminders']:
        context['reminders'][date].sort(key=lambda x: datetime.strptime(x['time'], "%H:%M"))
    #Sorting the dates
    context['reminders'] = dict(sorted(context['reminders'].items(), key=lambda items : datetime.strptime(items[0], "%d %B %Y")))
    return render(request, 'old_Reminders.html', context)

#Handling 404 page not found error
def page_not_found(request, exception):
    return render(request, '404.html', {'developer' : Developer.objects.get()})