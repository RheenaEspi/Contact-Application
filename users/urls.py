from django.urls import path
from users import views as user_views
from django.contrib.auth import views as auth_views
from users import views as user_views

urlpatterns = [
    path('register/', user_views.register, name='register'),

    path('check_the_otp/', user_views.check_the_otp, name='check_the_otp'),
    path('save_the_user_info/', user_views.save_the_user_info, name='save_the_user_info'),

    path('check_login_info/', user_views.check_login_info, name='check_login_info'),
    path('logout/', user_views.logout, name='logout'),
    path('retrive_pass/', user_views.retrive_pass, name='retrive_pass'),
    path('reset_pass/', user_views.reset_pass, name='reset_pass'),
    path('type_reset_pass/', user_views.type_reset_pass, name='type_reset_pass'),
    path('savereset_pass/', user_views.savereset_pass, name='savereset_pass'),

    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', user_views.profile, name='profile'),

    path('go_for_poll/', user_views.go_for_poll, name='go_for_poll'),
    path('Vice_President_vote/', user_views.Vice_President_vote, name='Vice_President_vote'),
    path('Vice_President_result/', user_views.Vice_President_result, name='Vice_President_result'),
    path('President_vote/', user_views.President_vote, name='President_vote'),
    path('President_result/', user_views.President_result, name='President_result'),
    path('Senator_vote/', user_views.Senator_vote, name='Senator_vote'),
    path('Senator_result/', user_views.Senator_result, name='Senator_result'),

    path('save_the_v_p_v/', user_views.save_the_v_p_v, name='save_the_v_p_v'),
    path('save_the_president_v/', user_views.save_the_president_v, name='save_the_president_v'),
    path('save_the_sanetor_v/', user_views.save_the_sanetor_v, name='save_the_sanetor_v'),

]