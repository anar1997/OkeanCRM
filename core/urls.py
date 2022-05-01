from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static

urlpatterns = [
    path('admin/clearcache/', include('clearcache.urls')),
    path('admin/', admin.site.urls),
    path('api/v1/', include("api.v1.urls")),
    path('api-auth', include("rest_framework.urls")),
    path('api/v1/rest_auth/', include("rest_auth.urls"))
]

urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)