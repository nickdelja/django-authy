# -*- coding: utf-8 -*-
from django.conf.urls import url

from .views import HoldingPageView, ProfileView

urlpatterns = [
    url(r'^holding/$', HoldingPageView.as_view(), name='holding'),
    url(r'^profile/$', ProfileView.as_view(), name='profile'),
]

