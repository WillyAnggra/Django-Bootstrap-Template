from django.urls import path
from. import views

urlpatterns = [
    path('', views.kategori, name = 'kategori'),
    path('tambah', views.create, name = 'tambah'),
    path('store', views.store, name = 'store'),
    path('edit/<int:id>', views.editKategori , name="editKategori"),
    path('update/<int:id>', views.updateKategori , name="updateKategori"),
    path('hapus/<int:id>', views.deleteKategori , name="hapusKategori"),
]
