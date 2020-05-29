from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

admin.site.site_header = "Online test paper and solution sharing system"
admin.site.site_title = "Online test paper and solution sharing system"
urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('accountprofile.urls')),
                  path('core/', include('core.urls')),
                  path('jet_api/', include('jet_django.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
