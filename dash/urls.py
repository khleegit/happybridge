
from django.conf.urls import url, include
from . import views

app_name = 'dash' # url에서 name을 사용하려면 추가 필요
urlpatterns = [
	url(r'^$', views.index, name = 'index'),
	url(r'^flot/', views.flot, name = 'flot'),
	url(r'^morris/', views.morris, name = 'morris'),
	url(r'^delivery/', views.delivery, name = 'delivery'),
	url(r'^affiliated/', views.affiliated, name = 'affiliated'),
	url(r'^consumer/', views.consumer, name = 'consumer'),
	url(r'^table/', views.tables, name = 'tables'),
	url(r'^forms/', views.forms, name = 'forms'), 
	url(r'^panels_wells/', views.panels_wells, name = 'panels_wells'),
	url(r'^buttons/', views.buttons, name = 'buttons'), 
	url(r'^notifications/', views.notifications, name = 'notifications'),
	url(r'^typography/', views.typography, name = 'typography'),
	url(r'^icons/', views.icons, name = 'icons'),
	url(r'^grid/', views.grid, name = 'grid'),
	url(r'^blank/', views.blank, name = 'blank'),
	url(r'^login/', views.login, name = 'login'),
]