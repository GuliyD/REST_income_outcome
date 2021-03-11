from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('api-path/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('api/income/', include('income.urls'))
]
