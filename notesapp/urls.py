from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('new_note', views.new_note, name = 'new_note'),
    path('update/<id>',views.update,name='update'),
    path('delete/<id>', views.delete, name = 'delete'),
    path('note_dtl/<id>',views.note_dtl, name="note_dtl"),
    path('search_text',views.search_text, name = 'search_text')

]