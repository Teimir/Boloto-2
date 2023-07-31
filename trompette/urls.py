from django.urls import path, include
from django.contrib import admin
from django.contrib.staticfiles import views

from .views import new_status, status, boost, reply, follow
from .views import homepage, home_tl, user_notif, user_tl, tag_tl
from .views import streaming

urlpatterns = [
    path('', homepage),
    path(r'/', homepage, name='homepage'),
    path(r'accounts/', include('django.contrib.auth.urls')),

    path(r'web/statuses/new', new_status, name="new_status"),
    path(r'web/statuses/([0-9]+)/boost', boost, name="boost"),
    path(r'web/statuses/([0-9]+)/reply', reply, name="reply"),
    path(r'web/statuses/([0-9]+)', status, name="status"),

    path(r'web/notifications', user_notif, name="user_notif"),
    path(r'web/timelines/home', home_tl, name="home_tl"),
    path(r'web/timelines/tag/(\w+)', tag_tl, name="tag_tl"),

    path(r'streaming/', streaming),
    path(r'admin/', admin.site.urls),

    path(r'static/(.+)', views.serve),

    path(r'^@([^/]+)', user_tl, name="user_tl"),
    path(r'^@([^/]+)/follow', follow, name="follow"),
]
