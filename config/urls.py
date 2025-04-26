# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django.views import defaults as default_views

from mainapp.views import LoadUserLikes, HomeView, TestView, LoadQuestions, ResultView

app_name = 'users'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('load/', LoadUserLikes.as_view(), name='load'),
    path('test/', TestView.as_view(), name='test'),
    re_path(r'^result/(?P<testid>[0-9]+)/$', ResultView.as_view(), name='result'),
    path('loadquestions/', LoadQuestions.as_view(), name='loadquestions'),
    
    # Admin panel
    path(settings.ADMIN_URL.lstrip('/'), admin.site.urls),
    
    # User management
    path('users/', include('fbstats.users.urls', namespace='users')),
    path('accounts/', include('allauth.urls')),
    
    # REST Framework
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += [
        path('400/', default_views.bad_request, kwargs={'exception': Exception('Bad Request!')}),
        path('403/', default_views.permission_denied, kwargs={'exception': Exception('Permission Denied')}),
        path('404/', default_views.page_not_found, kwargs={'exception': Exception('Page not Found')}),
        path('500/', default_views.server_error),
    ]
    
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar
        urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]