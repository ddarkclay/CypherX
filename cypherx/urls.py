from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('intro.urls')),    
    path('courses/', include('courses.urls'))
    # path('', views.index, name="Home_Page"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
