from django.urls import path
from .views import EventListView, EventDetailView, UserLoginView, UserRegisterView

app_name = 'event'

urlpatterns = [
    path('login/', UserLoginView.as_view()),
    path('register/', UserRegisterView.as_view()),
    path('list/', EventListView.as_view()),
    path('listview/<int:id>', EventDetailView.as_view())
]
