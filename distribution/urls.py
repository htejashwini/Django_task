from django.urls import path
from . import views

urlpatterns = [
    path('', views.subject_student_view, name='subject-student'),
    path('edit/<int:distribution_id>/', views.edit_result, name='edit-result'),
    path('delete/<int:distribution_id>/', views.delete_result, name='delete-result'),
    path('delete/<int:distribution_id>/', views.delete_result, name='delete-result'),

    path('delete/<int:distribution_id>/', views.delete_result, name='delete-confirmation'),
]
