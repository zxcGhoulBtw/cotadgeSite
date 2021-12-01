from django.contrib import admin
from django.urls import path, include


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('main.urls')),
    path('main/', include('main.urls')),
    path('admin/', admin.site.urls),
    path('about_us/', include('about_us.urls')),
    path('contact/', include('contact.urls')),
    path('faq/', include('faq.urls')),
    path('more1/', include('more1.urls')),
    path('more2/', include('more2.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
