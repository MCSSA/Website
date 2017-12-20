"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from News import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('about.html', views.about),
    path('404.html', views.not_found),
    path('blog-fullwidth.html', views.blog_full),
    path('blog-left-sidebar.html', views.blog_left),
    path('blog-right-sidebar.html', views.blog_right),
    path('contact.html', views.contact),
    path('gallery.html', views.gallery),
    path('service.html', views.service),
    path('single-portfolio.html', views.single_port),
    path('single-post.html', views.single_post),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
