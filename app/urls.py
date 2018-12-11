from django.urls import path

from . import views

urlpatterns = [
    path('', views.persons, name='persons'),
    path('sign_in', views.sign_in, name='sign_in'),
    path('sign_out', views.sign_out, name='sign_out'),
    path('persons/add', views.add_edit_person, name='persons_add'),
    path('persons/<int:person_id>/', views.person, name='person'),
    path('persons/<int:person_id>/edit/', views.add_edit_person, name='person_edit'),
    path('persons/<int:person_id>/update-status/', views.update_status, name='person_update_status'),
]