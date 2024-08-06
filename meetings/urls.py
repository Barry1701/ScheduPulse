from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.detail, name="detail"),
    path('rooms', views.rooms_list, name='rooms'),
    path('new', views.new, name="new"),
    path('edit/<int:id>', views.edit_meeting, name='edit_meeting'),
    path('delete/<int:id>', views.delete_meeting, name='delete_meeting'),
    path('', views.meetings_list, name='meetings_list'),
    
]
