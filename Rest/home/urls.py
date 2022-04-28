from django.urls import path
from . import views




app_name = 'home'
urlpatterns = [
    # path('', views.home, name='home'),# Function Based Views
    path('', views.Home.as_view(), name='home'),  # Class-based Views
    path('questions/', views.QuestionListView.as_view()),
    path('question/create/', views.QuestionCreateView.as_view()),
    path('question/update/<int:pk>/', views.QuestionUpdateView.as_view()),
    path('question/delete/<int:pk>/', views.QuestionDeleteView.as_view()),
]
