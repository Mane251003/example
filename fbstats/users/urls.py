from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path(
        '',
        views.UserListView.as_view(),
        name='list'
    ),
    path(
        'redirect/',
        views.UserRedirectView.as_view(),
        name='redirect'
    ),
    path(
        '<str:username>/',  # Փոխարինել regex-ը path converter-ով
        views.UserDetailView.as_view(),
        name='detail'
    ),
    path(
        'update/',  # Հեռացնել ~ նշանը և regex սինտաքսը
        views.UserUpdateView.as_view(),
        name='update'
    ),
]