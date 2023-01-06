from .views import HomePage,resourcesPage,detialPage,aboutPage,aboutDetailPage,signUpPage
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',HomePage.as_view(),name="home"),
    path('resources/',resourcesPage,name="Resources"),
    path('resources/<str:id>',detialPage,name="resource_detail"),
    path('about/',aboutPage,name="about"),
    path('about/<str:id>',aboutDetailPage,name="about_detail"),
    path('login/',auth_views.LoginView.as_view(),name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('signup/',signUpPage,name="register")
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
