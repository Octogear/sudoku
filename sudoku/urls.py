"""sudoku URL Configuration.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from django.urls import path
from django.conf.urls import include
from django.contrib import admin
# from django.contrib.auth import views as auth_views

from sudoku_app import views as sudoku_app_views

# from django.conf.urls.static import static
# from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', sudoku_app_views.IndexView.as_view(), name='home'),
    path('health/', sudoku_app_views.HealthView.as_view(), name='health'),
    path('sudoku_app_template/', sudoku_app_views.sudoku_appIndexView.as_view(), name='sudoku_app_template'),

    # logging users in/out
    path('accounts/login', include('django.contrib.auth.urls'), name='login'),
    path('accounts/logout', include('django.contrib.auth.urls'), name='logout'),

    # signup users
    path('signup/', sudoku_app_views.SignUpView.as_view(), name='signup'),

    # app url
    path('sudoku_app/', include('sudoku_app.urls')),


]  # + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
