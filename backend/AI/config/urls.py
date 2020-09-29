from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('community/', include('community.urls')),
    path('english/', include('english.urls')),

    # 로그인 & 로그아웃
    path('rest-auth/', include('rest_auth.urls')),
    # 회원가입
    path('rest-auth/signup/', include('rest_auth.registration.urls'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
