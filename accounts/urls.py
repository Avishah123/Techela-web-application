from django.contrib import admin
from django.urls import path, include
from .views import StudentSignUpView, hotel_image_view
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from .decorators import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', views.home, name='home'),
    path('register', views.eventRegistration, name='eventreg'),
    path('events', views.events1, name='events1'),
    path('students', StudentSignUpView.as_view(), name='student1'),
    path('login', auth_views.LoginView.as_view(
        template_name='forms/login.html'), name='login'),
    path('mass_emailer', views.mass_emailer, name='mass_emailer'),
    path('success', views.success, name='success'),
    path('user/detail',
         login_required(head_required(views.DetailEvent.as_view())), name='detail'),
    path('user_report', views.report, name='report'),
    path('logout', views.logout, name='logout'),
    path('warning', views.warning, name='warning'),
    path('logout_confirm', views.logout3, name='logout3'),
    path('image_upload', hotel_image_view, name='image_upload'),

    #  Techfest Events Forms
    path('valo_form', views.valo_register, name='valo_form'),
    path('amongus_form', views.amoungus_register, name='amongus_form'),
    path('cod_form', views.cod_register, name='cod_form'),
    path('csgo_form', views.csgo_register, name='csgo_form'),
    path('clash_form', views.clash_register, name='clash_form'),


    #  Techfest Events Views
    path('valorant_reg', views.valorant_view, name='valorant_reg'),
    path('csgo_reg', views.csgo_view, name='csgo_reg'),
    path('clash_reg', views.clash_view, name='clash_reg'),
    path('cod_reg', views.cod_view, name='cod_reg'),
    path('amongus_reg', views.amongus_view, name='amongus_reg'),
    path('tre_reg', views.tre_view, name='tre_reg'),

    #  Testing Views
    path('tre_form', views.treasure_register, name='tre_form'),
    path('test11', views.form1, name='test11'),


    #  Display views
    path('reg_list', views.reg_list, name='reg_list'),
    path('events_list', views.events_list, name='event_list'),
    path('pevents_list', views.pevents_list, name='pevents_list'),
    path('preg_list', views.preg_list, name='preg_list'),


    # Techfest Registrations
    path('valo_report', views.valo_report, name='valo_report'),
    path('csgo_report', views.csgo_report, name='csgo_report'),
    path('clash_report', views.clash_report, name='clash_report'),
    path('cod_report', views.cod_report, name='cod_report'),
    path('amongus_report', views.amongus_report, name='amongus_report'),
    path('tre_report', views.tre_report, name='tre_report'),
    path('scrib_report', views.scrib_report, name='scrib_report'),
    path('meme_report', views.meme_report, name='meme_report'),
    path('bolly_report', views.bolly_report, name='bolly_report'),
    path('chess_report', views.chess_report, name='chess_report'),
    path('openmic_report', views.openmic_report, name='openmic_report'),

    #  Pre Techfest Forms
    path('scrib_form', views.scrib_register, name='scrib_form'),
    path('chess_form', views.chess_register, name='chess_form'),
    path('bolly_form', views.bolly_register, name='bolly_form'),
    path('openmic_form', views.openmic_register, name='openmic_form'),
    path('meme_form', views.meme_register, name='meme_form'),

    # Pre techfest Views
    path('scrib_reg', views.scrib_view, name='scrib_reg'),
    path('chess_reg', views.chess_view, name='chess_reg'),
    path('openmic_reg', views.openmic_view, name='openmic_reg'),
    path('meme_reg', views.meme_view, name='meme_reg'),
    path('bolly_reg', views.bolly_view, name='bolly_reg'),





] + static(settings.MEDIA_URL,
           document_root=settings.MEDIA_ROOT)
