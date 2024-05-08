from django.contrib import admin
from django.urls import path, include, re_path
from . import views

urlpatterns = [
    re_path(r'^$',  views.main, name="main"),
    re_path(r'^users_realty/$',views.users_realty, name='users_realty'),
    re_path(r'^users_realty/category/(?P<category_slug>[-\w]+)/$',views.user_category_realties, name="user_category"),
    re_path(r'^agency_realty/$', views.agency_realty,  name='agency_realty'),
    re_path(r'^agency_realty/category/(?P<category_slug>[-\w]+)/$',views.agency_category_realties, name="agency_category"),
    re_path(r'^realty/(?P<realty_slug>[-\w]+)/$',views.realty, name="realty"),
    re_path(r'^login/$',views.LoginUser.as_view(), name="login"),
    re_path(r'^register/$',views.RegisterUser.as_view(), name="register"),
    re_path(r'^logout/$', views.logout_user, name="logout"),
    re_path(r'^owner_realties/$', views.owner_realties, name="owner_realties"),
    re_path(r'^query/$', views.query, name="query"),
    re_path(r'^new_query/(?P<realty_slug>[-\w]+)/$', views.create_query, name="create_quary"),
    re_path(r'^accept_query/(?P<query_id>\d+)/$', views.accept_query, name="accept_query"),
    re_path(r'^add_realty/$', views.AddRealtyView.as_view(), name="add_realty"),
    re_path(r'^delete_realty/(?P<realty_slug>[-\w]+)/$', views.delete_realty, name="delete_realty"),
    re_path(r'^update_realty/(?P<slug>[-\w]+)/$', views.UpdateRealtyView.as_view(), name="update_realty"),
    re_path(r'^delete_query/(?P<query_id>\d+)/$', views.delete_query, name="delete_query"),
    re_path(r'^admin_info/$', views.admin_info, name="admin_info"),
    re_path(r'^profile/(?P<user_id>\d+)/$', views.profile_user, name="profile_user"),
    re_path(r'^update_user_data/(?P<pk>\d+)/$', views.UpdateUserView.as_view(), name='update_user_data'),
    re_path(r'^buy_realty/(?P<realty_slug>[-\w]+)/$', views.buy_realty, name="buy_realty"),
    re_path(r'^create-checkout-session/(?P<realty_slug>[-\w]+)/(?P<landlord_id>\d+)/$', views.CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
    re_path(r'^success/(?P<realty_slug>[-\w]+)/(?P<landlord_id>\d+)/$', views.success, name='success'),
    re_path(r'^cancel/$', views.cancel, name='cancel'),
    re_path(r'^owner/all_realties/$', views.all_realties, name='all_realties'),
    re_path(r'^owner/all_employees/$', views.view_all_employees, name='all_employees'),
    re_path(r'^owner/all_clients/$', views.view_all_clients, name='all_clients'),
    re_path(r'^owner/add_employee/$', views.RegisterUser.as_view(), name='add_employee'),
    re_path(r'^owner/delete_employee/(?P<user_id>\d+)/$', views.delete_employee, name='delete_employee'),
    re_path(r'^employee_clients/(?P<employee_id>\d+)/$', views.employee_clients, name='employee_clients'),
    re_path(r'^company/$', views.view_info_company, name='info_company'),
    re_path(r'^news/$', views.view_news, name='news'),
    re_path(r'^article/(?P<article_id>\d+)/$', views.view_article, name='article'),
    re_path(r'^FAQ/$', views.view_FAQ, name='FAQ'),
    re_path(r'^vacancies/$', views.view_vacancies, name='vacancies')
]