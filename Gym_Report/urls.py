from django.urls import path
from Gym import views
from django.conf import settings
from django.conf.urls.static import static

"""
URL configuration for Gym_Report project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app  import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login, name="login"),
    path('signup/', views.signup, name="signup"), 

    path('index/', views.home, name="home"),
    path('exercises/', views.exercises, name="exercises"),
    path('profile/', views.profile, name="profile"),
    path('history/', views.history, name="history"),
    
    path('workout/', views.workout, name="workout"),

    path('Biceps/', views.Biceps_, name="Biceps"),
    path('Triceps/', views.Triceps_, name="Triceps"),
    path('Forearms/', views.Forearms_, name="Forearms"),
    path('Leg/', views.Leg_, name="Leg"),
    path('Back/', views.Back_, name="Back"),
    path('Chest/', views.Chest_, name="Chest"),
    path('Shoulder/', views.Shoulder_, name="Shoulder"),
    path('Abs/', views.Abs_, name="Abs"),    
    path('404/', views.error_404_view, name="error_404_view"),    

]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )