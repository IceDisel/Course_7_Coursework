from django.urls import path
from habit_tracker.apps import HabitTrackerConfig
from habit_tracker.views import CreateHabitsAPIView, DetailHabitsAPIView, UserListHabitsAPIView, DeleteHabitsAPIView, \
    UpdateHabitsAPIView, PublicListHabitsAPIView

app_name = HabitTrackerConfig.name

urlpatterns = [
    path('habits/create/', CreateHabitsAPIView.as_view(), name='create'),
    path('habits/detail/<int:pk>/', DetailHabitsAPIView.as_view(), name='detail'),
    path('habits/update/<int:pk>/', UpdateHabitsAPIView.as_view(), name='update'),
    path('habits/delete/<int:pk>/', DeleteHabitsAPIView.as_view(), name='delete'),
    path('habits/user_list/', UserListHabitsAPIView.as_view(), name='user_list'),
    path('habits/public_list/', PublicListHabitsAPIView.as_view(), name='public_list'),
]
