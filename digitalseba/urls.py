
from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static

app_name=(
'home',
'girls',
'panjabi',
'pant',
'shirt',
't_shirt'
'gift'
)
urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('home/',include('home.urls')),
    path('girls/',include('girls.urls')),
    path('panjabi/',include('panjabi.urls')),
    path('pant/',include('pant.urls')),
    path('shirt/',include('shirt.urls')),
    path('t_shirt/',include('t_shirt.urls')),
    path('gift/',include('gift.urls')),

    path('api/',include('api.urls'))
]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
