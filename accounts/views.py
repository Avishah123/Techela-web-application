from django.shortcuts import render, redirect
from .forms import StudentSignUpForm, HotelForm
from .models import Student, User, EventRegistration
from django.views.generic import CreateView
from django.contrib.auth import login
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail
import csv
from django.http import HttpResponse
from django.contrib import auth
from .decorators import *
from .models import *
from django.template.loader import render_to_string


# Validations to be added
# 1. No user can have a tour without logging in
# 2  No user can fill the events form without logging in
# 3. Bulk Emailer to only registered user


def home(request):
    return render(request, 'home.html')


def valo_register(request):
    return render(request, 'forms/valo_form.html')


def cod_register(request):
    return render(request, 'forms/cod_form.html')


def amoungus_register(request):
    return render(request, 'forms/amongus_form.html')


def clash_register(request):
    return render(request, 'forms/clash_form.html')


def scrib_register(request):
    return render(request, 'forms/scrib_form.html')


def bolly_register(request):
    return render(request, 'forms/bolly_form.html')


def meme_register(request):
    return render(request, 'forms/meme_form.html')


def chess_register(request):
    return render(request, 'forms/chess_form.html')


def openmic_register(request):
    return render(request, 'forms/openmic_form.html')


def csgo_register(request):
    return render(request, 'forms/csgo_form.html')


def events_list(request):
    return render(request, 'events_list.html')


def pevents_list(request):
    return render(request, 'pevents.html')


def treasure_register(request):
    return render(request, 'forms/treasurehunt.html')


def form1(request):
    return render(request, 'forms/test1.html')


def reg_list(request):
    return render(request, 'reg_list.html')


def preg_list(request):
    return render(request, 'preg_list.html')


@login_required
def events1(request):
    if (EventRegistration.objects.count() < 10):
        return render(request, 'forms/eventregister.html')
    else:
        return HttpResponse('Registration closed')


def success(request):
    return render(request, 'success1.html')


class StudentSignUpView(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user-type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


def eventRegistration(request):
    if request.method == 'POST':
        if (EventRegistration.objects.count() < 10):
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            mobile_number = request.POST['mobile_number']
            event_name = request.POST['event_name']
            college_name = request.POST['college_name']

            events = EventRegistration(first_name=first_name, last_name=last_name, email=email,
                                       mobile_number=mobile_number, event_name=event_name, college_name=college_name)

            events.save()
            print('Event Registration Done Succesfully')
            subject = 'Techela 6.0 Registration'
            from_email = settings.DEFAULT_FROM_EMAIL
            message = 'Registered for the event xyz'

            html_message = '<h1>You have been registered </h1>'

            send_mail(subject, message, from_email, [email],
                      fail_silently=False, html_message=html_message)

            return redirect('home')
        else:
            print('Limit exceeded , regisatrations are closed')
            return HttpResponse('Closed')

        print(request.user.get_username())
        # form.instance.user = self.request.user
        # print(form.instance.user)

    else:
        print('Not there events')
        return redirect('warning.html2')


@login_required
@head_required
def mass_emailer(request):
    # Emails = User.objects.values_list('email', flat=True)
    Emails = User.objects.values_list('email', flat=True).distinct()
    linked_content = []
    for i in Emails:
        linked_content.append(i)

    print(linked_content)

    subject = 'Some subject'
    from_email = settings.DEFAULT_FROM_EMAIL
    message = 'This is my test message'
    recipient_list = linked_content
    html_message = '<h1>This is my HTML test</h1>'

    send_mail(subject, message, from_email, recipient_list,
              fail_silently=False, html_message=html_message)

    return redirect('success')

#  Emails = EventRegistration.objects.values_list('email', flat=True).distinct()


class DetailEvent(generic.ListView):
    template_name = 'details.html'
    queryset = EventRegistration.objects.all().order_by('id')


@login_required
@head_required
def report(request):
    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(['First Name', 'Last Name', 'Email',
                     'Mobile Number', 'Name of the College', 'Name of the Event'])

    for member in EventRegistration.objects.all().values_list('first_name', 'last_name', 'email', 'mobile_number', 'college_name', 'event_name'):
        writer.writerow(member)

    response['Content-Disposition'] = 'attachment; filename="registration.csv"'

    return response


@login_required
def logout(request):

    auth.logout(request)
    return redirect('logout3')


def warning(request):
    return render(request, 'warning.html')


def logout3(request):
    return render(request, 'logout1.html')


def hotel_image_view(request):

    if request.method == 'POST':
        form = HotelForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = HotelForm()

    return render(request, 'images.html', {'form': form})


######################### Event Views ######################################

def valorant_view(request):
    if (valorant_registration.objects.count() <= 160):
        if request.method == 'POST':
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            mobile_number = request.POST['mobile_number']
            branch = request.POST['mobile_number']
            dicord_id = request.POST['dicord_id']
            valorant_id = request.POST['valorant_id']
            college_name = request.POST['college_name']
            student_id = request.FILES['student_id']

            valorant = valorant_registration(first_name=first_name, last_name=last_name, email=email,
                                             mobile_number=mobile_number, branch=branch, dicord_id=dicord_id, valorant_id=valorant_id, college_name=college_name, student_id=student_id)

            valorant.save()
            print('Event Registration Done Succesfully')
            subject = 'Techela 6.0 Registration'
            from_email = settings.DEFAULT_FROM_EMAIL
            template = render_to_string(
                'thank-you.html', {'name': first_name + ' ' + last_name, 'event': 'Valorant'})
            message = 'Test'
            html_message = template

            send_mail(subject, message, from_email, [email],
                      fail_silently=False, html_message=html_message)
            return HttpResponse('Done')

        else:
            print('Not there events')
            return redirect('warning.html2')

    else:
        return HttpResponse('Registration closed')


def csgo_view(request):
    if (csgo_registration.objects.count() <= 160):
        if request.method == 'POST':
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            mobile_number = request.POST['mobile_number']
            branch = request.POST['mobile_number']
            dicord_id = request.POST['dicord_id']
            csgo_id = request.POST['csgo_id']
            college_name = request.POST['college_name']
            student_id = request.FILES['student_id']

            csgo = csgo_registration(first_name=first_name, last_name=last_name, email=email,
                                     mobile_number=mobile_number, branch=branch, dicord_id=dicord_id, csgo_id=csgo_id, college_name=college_name, student_id=student_id)

            csgo.save()
            print('Event Registration Done Succesfully')
            subject = 'Techela 6.0 Registration'
            from_email = settings.DEFAULT_FROM_EMAIL
            template = render_to_string(
                'thank-you.html', {'name': first_name + ' ' + last_name, 'event': 'CS-GO'})
            message = 'Test'
            html_message = template

            send_mail(subject, message, from_email, [email],
                      fail_silently=False, html_message=html_message)
            return HttpResponse('Done')

        else:
            print('Not there events')
            return redirect('warning.html2')

    else:
        return HttpResponse('Registration closed')


def clash_view(request):
    if (clash_registration.objects.count() <= 160):
        if request.method == 'POST':
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            mobile_number = request.POST['mobile_number']
            branch = request.POST['mobile_number']
            dicord_id = request.POST['dicord_id']
            player_id = request.POST['player_id']
            college_name = request.POST['college_name']
            student_id = request.FILES['student_id']

            clash = clash_registration(first_name=first_name, last_name=last_name, email=email,
                                       mobile_number=mobile_number, branch=branch, dicord_id=dicord_id, player_id=player_id, college_name=college_name, student_id=student_id)

            clash.save()
            print('Event Registration Done Succesfully')
            subject = 'Techela 6.0 Registration'
            from_email = settings.DEFAULT_FROM_EMAIL
            template = render_to_string(
                'thank-you.html', {'name': first_name + ' ' + last_name, 'event': 'Clash Royale'})
            message = 'Test'
            html_message = template

            send_mail(subject, message, from_email, [email],
                      fail_silently=False, html_message=html_message)

            return HttpResponse('Done')

        else:
            print('Not there events')
            return redirect('warning.html2')
    else:
        return HttpResponse('Registration closed for Clash')


def cod_view(request):
    if (callofduty_registration.objects.count() <= 400):
        if request.method == 'POST':
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            mobile_number = request.POST['mobile_number']
            branch = request.POST['mobile_number']
            dicord_id = request.POST['dicord_id']
            player_id = request.POST['player_id']
            college_name = request.POST['college_name']
            student_id = request.FILES['student_id']

            cod = callofduty_registration(first_name=first_name, last_name=last_name, email=email,
                                          mobile_number=mobile_number, branch=branch, dicord_id=dicord_id, player_id=player_id, college_name=college_name, student_id=student_id)

            cod.save()
            print('Event Registration Done Succesfully')
            subject = 'Techela 6.0 Registration'
            from_email = settings.DEFAULT_FROM_EMAIL
            template = render_to_string(
                'thank-you.html', {'name': first_name + ' ' + last_name, 'event': 'Call of Duty'})
            message = 'Test'
            html_message = template

            send_mail(subject, message, from_email, [email],
                      fail_silently=False, html_message=html_message)

            return HttpResponse('Done')

        else:
            print('Not there events')
            return redirect('warning.html2')
    else:
        return HttpResponse('Registration closed for Call Of Duty')


def amongus_view(request):
    if (amongus_registration.objects.count() <= 200):
        if request.method == 'POST':
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            mobile_number = request.POST['mobile_number']
            branch = request.POST['mobile_number']
            dicord_id = request.POST['dicord_id']
            player_id = request.POST['player_id']
            college_name = request.POST['college_name']
            student_id = request.FILES['student_id']

            amongus = amongus_registration(first_name=first_name, last_name=last_name, email=email,
                                           mobile_number=mobile_number, branch=branch, dicord_id=dicord_id, player_id=player_id, college_name=college_name, student_id=student_id)

            amongus.save()
            print('Event Registration Done Succesfully')
            subject = 'Techela 6.0 Registration'
            from_email = settings.DEFAULT_FROM_EMAIL
            template = render_to_string(
                'thank-you.html', {'name': first_name + ' ' + last_name, 'event': 'Among Us'})
            message = 'Test'
            html_message = template

            send_mail(subject, message, from_email, [email],
                      fail_silently=False, html_message=html_message)

            return HttpResponse('Done')

        else:
            print('Not there events')
            return redirect('warning.html2')

    else:
        return HttpResponse('Registration closed for Among Us')


def tre_view(request):
    if (amongus_registration.objects.count() <= 200):
        if request.method == 'POST':
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            mobile_number = request.POST['mobile_number']
            branch = request.POST['mobile_number']
            dicord_id = request.POST['dicord_id']
            insta_id = request.POST['insta_id']
            college_name = request.POST['college_name']
            student_id = request.FILES['student_id']

            treasure = treasurehunt_registration(first_name=first_name, last_name=last_name, email=email,
                                                 mobile_number=mobile_number, branch=branch, dicord_id=dicord_id, insta_id=insta_id, college_name=college_name, student_id=student_id)

            treasure.save()
            print('Event Registration Done Succesfully')
            subject = 'Techela 6.0 Registration'
            from_email = settings.DEFAULT_FROM_EMAIL
            template = render_to_string(
                'thank-you.html', {'name': first_name + ' ' + last_name, 'event': 'Treasure Hunt'})
            message = 'Test'
            html_message = template

            send_mail(subject, message, from_email, [email],
                      fail_silently=False, html_message=html_message)

            return HttpResponse('Done')

        else:
            print('Not there events')
            return redirect('warning.html2')

    else:
        return HttpResponse('Registration closed for Treasure Hunt')


def scrib_view(request):
    if (scrib_registration.objects.count() <= 250):
        if request.method == 'POST':
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            mobile_number = request.POST['mobile_number']
            dicord_id = request.POST['dicord_id']
            college_name = request.POST['college_name']
            student_id = request.FILES['student_id']

            scrib = scrib_registration(first_name=first_name, last_name=last_name, email=email,
                                       mobile_number=mobile_number, dicord_id=dicord_id,  college_name=college_name, student_id=student_id)

            scrib.save()
            print('Event Registration Done Succesfully')
            subject = 'Techela 6.0 Registration'
            from_email = settings.DEFAULT_FROM_EMAIL
            template = render_to_string(
                'thank-you.html', {'name': first_name + ' ' + last_name, 'event': 'Scribble'})
            message = 'Test'
            html_message = template

            send_mail(subject, message, from_email, [email],
                      fail_silently=False, html_message=html_message)

            return HttpResponse('Done')

        else:
            print('Not there events')
            return redirect('warning.html2')

    else:
        return HttpResponse('Registration closed for Scribble')


def bolly_view(request):
    if (bolly_registration.objects.count() <= 1000):
        if request.method == 'POST':
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            mobile_number = request.POST['mobile_number']
            dicord_id = request.POST['dicord_id']
            college_name = request.POST['college_name']
            student_id = request.FILES['student_id']

            bolly = bolly_registration(first_name=first_name, last_name=last_name, email=email,
                                       mobile_number=mobile_number, dicord_id=dicord_id,  college_name=college_name, student_id=student_id)

            bolly.save()
            print('Event Registration Done Succesfully')
            subject = 'Techela 6.0 Registration'
            from_email = settings.DEFAULT_FROM_EMAIL
            template = render_to_string(
                'thank-you.html', {'name': first_name + ' ' + last_name, 'event': 'Bollywood Quiz'})
            message = 'Test'
            html_message = template

            send_mail(subject, message, from_email, [email],
                      fail_silently=False, html_message=html_message)

            return HttpResponse('Done')

        else:
            print('Not there events')
            return redirect('warning.html2')

    else:
        return HttpResponse('Registration closed for Bollywood Quiz')


def chess_view(request):
    if (chess_registration.objects.count() <= 100):
        if request.method == 'POST':
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            mobile_number = request.POST['mobile_number']
            dicord_id = request.POST['dicord_id']
            college_name = request.POST['college_name']
            student_id = request.FILES['student_id']

            chess = chess_registration(first_name=first_name, last_name=last_name, email=email,
                                       mobile_number=mobile_number, dicord_id=dicord_id,  college_name=college_name, student_id=student_id)

            chess.save()
            print('Event Registration Done Succesfully')
            subject = 'Techela 6.0 Registration'
            from_email = settings.DEFAULT_FROM_EMAIL
            template = render_to_string(
                'thank-you.html', {'name': first_name + ' ' + last_name, 'event': 'Chess Event'})
            message = 'Test'
            html_message = template

            send_mail(subject, message, from_email, [email],
                      fail_silently=False, html_message=html_message)

            return HttpResponse('Done')

        else:
            print('Not there events')
            return redirect('warning.html2')

    else:
        return HttpResponse('Registration closed for Chess')


def openmic_view(request):
    if (openmic_registration.objects.count() <= 1000):
        if request.method == 'POST':
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            mobile_number = request.POST['mobile_number']
            dicord_id = request.POST['dicord_id']
            college_name = request.POST['college_name']
            student_id = request.FILES['student_id']

            openmic = openmic_registration(first_name=first_name, last_name=last_name, email=email,
                                           mobile_number=mobile_number, dicord_id=dicord_id,  college_name=college_name, student_id=student_id)

            openmic.save()
            print('Event Registration Done Succesfully')
            subject = 'Techela 6.0 Registration'
            from_email = settings.DEFAULT_FROM_EMAIL
            template = render_to_string(
                'thank-you.html', {'name': first_name + ' ' + last_name, 'event': 'Open Mic Event'})
            message = 'Test'
            html_message = template

            send_mail(subject, message, from_email, [email],
                      fail_silently=False, html_message=html_message)

            return HttpResponse('Done')

        else:
            print('Not there events')
            return redirect('warning.html2')

    else:
        return HttpResponse('Registration closed for Open Mic')


def meme_view(request):
    if (meme_registration.objects.count() <= 2000):
        if request.method == 'POST':
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            mobile_number = request.POST['mobile_number']
            dicord_id = request.POST['dicord_id']
            insta_id = request.POST['insta_id']
            college_name = request.POST['college_name']
            student_id = request.FILES['student_id']
            meme_upload = request.FILES['meme_upload']

            meme = meme_registration(first_name=first_name, last_name=last_name, email=email,
                                     mobile_number=mobile_number,  dicord_id=dicord_id, insta_id=insta_id, college_name=college_name, student_id=student_id, meme_upload=meme_upload)

            meme.save()
            print('Event Registration Done Succesfully')
            subject = 'Techela 6.0 Registration'
            from_email = settings.DEFAULT_FROM_EMAIL
            template = render_to_string(
                'thank-you.html', {'name': first_name + ' ' + last_name, 'event': 'Meme War'})
            message = 'Test'
            html_message = template

            send_mail(subject, message, from_email, [email],
                      fail_silently=False, html_message=html_message)

            return HttpResponse('Done')

        else:
            print('Not there events')
            return redirect('warning.html2')

    else:
        return HttpResponse('Registration closed for Meme War')

################## REPORT GENERATION ######################################


def valo_report(request):
    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(['First Name', 'Last Name', 'Email',
                     'Mobile Number',  'Discord ID', 'Valorant ID', 'Name of the College', 'Student ID'])

    for member in valorant_registration.objects.all().values_list('first_name', 'last_name', 'email', 'mobile_number', 'dicord_id', 'valorant_id', 'college_name', 'student_id'):
        writer.writerow(member)

    response['Content-Disposition'] = 'attachment; filename="valorant_registration.csv"'

    return response


def csgo_report(request):
    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(['First Name', 'Last Name', 'Email',
                     'Mobile Number',  'Discord ID', 'CS-GO ID', 'Name of the College', 'Student ID'])

    for member in csgo_registration.objects.all().values_list('first_name', 'last_name', 'email', 'mobile_number', 'dicord_id', 'csgo_id', 'college_name', 'student_id'):
        writer.writerow(member)

    response['Content-Disposition'] = 'attachment; filename="csgo_registration.csv"'

    return response


def clash_report(request):
    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(['First Name', 'Last Name', 'Email',
                     'Mobile Number',  'Discord ID', 'Clash Royale ID', 'Name of the College', 'Student ID'])

    for member in clash_registration.objects.all().values_list('first_name', 'last_name', 'email', 'mobile_number', 'dicord_id', 'player_id', 'college_name', 'student_id'):
        writer.writerow(member)

    response['Content-Disposition'] = 'attachment; filename="clash_registration.csv"'

    return response


def cod_report(request):
    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(['First Name', 'Last Name', 'Email',
                     'Mobile Number',  'Discord ID', 'Call of Duty ID', 'Name of the College', 'Student ID'])

    for member in callofduty_registration.objects.all().values_list('first_name', 'last_name', 'email', 'mobile_number', 'dicord_id', 'player_id', 'college_name', 'student_id'):
        writer.writerow(member)

    response['Content-Disposition'] = 'attachment; filename="cod_registration.csv"'

    return response


def amongus_report(request):
    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(['First Name', 'Last Name', 'Email',
                     'Mobile Number',  'Discord ID', 'In-game Name', 'Name of the College', 'Student ID'])

    for member in amongus_registration.objects.all().values_list('first_name', 'last_name', 'email', 'mobile_number', 'dicord_id', 'player_id', 'college_name', 'student_id'):
        writer.writerow(member)

    response['Content-Disposition'] = 'attachment; filename="amongus_registration.csv"'

    return response


def tre_report(request):
    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(['First Name', 'Last Name', 'Email',
                     'Mobile Number',  'Discord ID', 'Instagram ID', 'Name of the College', 'Student ID'])

    for member in treasurehunt_registration.objects.all().values_list('first_name', 'last_name', 'email', 'mobile_number', 'dicord_id', 'insta_id', 'college_name', 'student_id'):
        writer.writerow(member)

    response['Content-Disposition'] = 'attachment; filename="treasurehunt_registration.csv"'

    return response


def scrib_report(request):
    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(['First Name', 'Last Name', 'Email',
                     'Mobile Number',  'Discord ID', 'Name of the College', 'Student ID'])

    for member in scrib_registration.objects.all().values_list('first_name', 'last_name', 'email', 'mobile_number', 'dicord_id',  'college_name', 'student_id'):
        writer.writerow(member)

    response['Content-Disposition'] = 'attachment; filename="scribble_registration.csv"'

    return response


def bolly_report(request):
    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(['First Name', 'Last Name', 'Email',
                     'Mobile Number',  'Discord ID', 'Name of the College', 'Student ID'])

    for member in bolly_registration.objects.all().values_list('first_name', 'last_name', 'email', 'mobile_number', 'dicord_id',  'college_name', 'student_id'):
        writer.writerow(member)

    response['Content-Disposition'] = 'attachment; filename="bollywood_registration.csv"'

    return response


def openmic_report(request):
    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(['First Name', 'Last Name', 'Email',
                     'Mobile Number',  'Discord ID', 'Name of the College', 'Student ID'])

    for member in openmic_registration.objects.all().values_list('first_name', 'last_name', 'email', 'mobile_number', 'dicord_id',  'college_name', 'student_id'):
        writer.writerow(member)

    response['Content-Disposition'] = 'attachment; filename="Openmic_registration.csv"'

    return response


def chess_report(request):
    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(['First Name', 'Last Name', 'Email',
                     'Mobile Number',  'Discord ID', 'Name of the College', 'Student ID'])

    for member in chess_registration.objects.all().values_list('first_name', 'last_name', 'email', 'mobile_number', 'dicord_id',  'college_name', 'student_id'):
        writer.writerow(member)

    response['Content-Disposition'] = 'attachment; filename="chess_registration.csv"'

    return response


def meme_report(request):
    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(['First Name', 'Last Name', 'Email',
                     'Mobile Number',  'Discord ID', 'Instagram ID', 'Name of the College', 'Student ID'])

    for member in meme_registration.objects.all().values_list('first_name', 'last_name', 'email', 'mobile_number', 'dicord_id', 'insta_id', 'college_name', 'student_id'):
        writer.writerow(member)

    response['Content-Disposition'] = 'attachment; filename="memewar_registration.csv"'

    return response
