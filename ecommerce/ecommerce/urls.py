from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('indic_auth.urls'), name='indic_auth'),
    path('', include('ecom_app.urls'), name='ecom_app'),
]
