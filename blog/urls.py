from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('contact.html', views.contact, name='contact'),
    path('about.html', views.about, name='about'),
    path('team.html', views.team, name='team'),
    path('school_list.html', views.school_list, name='school_list'),
    #path('school_detail.html', views.school_detail, name=' school_detail'),
    path('school<int:pk>', views.school_detail, name='school_detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)