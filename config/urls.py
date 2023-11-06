from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('bookmark/', include('bookmark.urls')),
    path('admin/', admin.site.urls),
    path('tour/', include('tour.urls')),
    path('markdownx/', include('markdownx.urls')),
    path('crm/', include('website.urls')),
    path('tinymce/', include('tinymce.urls')),
]

# static() 정적 파일들의 url을 관리. 접근한 url을 리턴.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)