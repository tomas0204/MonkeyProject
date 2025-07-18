"""vercel_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from index.views import hello, rules, game, submit_word, monkey_learn, definition, final

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hello, name='index'),
    path("hello/rules/", rules, name="rules"),
    path("hello/game/", game, name="game"),
    path('submit_word/', submit_word, name='submit_word'),
    path('simulate/<str:word>/', monkey_learn, name='simulate'),
    path('definition/<str:word>/', definition, name='definition'),
    path('final/', final, name='final'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
