from django.shortcuts import render, redirect, get_object_or_404
from .models import Produk, Kategori, Status
from django import forms

#Form Validasi (Poin 7: Nama wajib isi & Harga harus angka)
class ProdukForm(forms.ModelForm):
    class Meta:
        model = Produk
        fields = ['nama_produk', 'harga', 'kategori', 'status']
        widgets = {
            'nama_produk': forms.TextInput(attrs={'class': 'form-control'}),
            'harga': forms.NumberInput(attrs={'class': 'form-control'}),
            'kategori': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

#nampilin Data (Poin 4 & 5)
def produk_list(request):
    #Mengurutkan berdasarkan ID terkecil ke terbesar (ASCENDING)
    data_produk = Produk.objects.filter(status__nama_status="bisa dijual").order_by('id_produk')
    form = ProdukForm()
    return render(request, 'produk_list.html', {
        'produk': data_produk, 
        'form': form
    })

#Fitur Tambah (Poin 6)
def produk_tambah(request):
    if request.method == "POST":
        form = ProdukForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('produk_list')
    else:
        form = ProdukForm()
    return render(request, 'produk_form.html', {'form': form, 'title': 'Tambah Produk'})

#Fitur Edit (Poin 6)
def produk_edit(request, id):
    produk = get_object_or_404(Produk, id_produk=id)
    if request.method == "POST":
        form = ProdukForm(request.POST, instance=produk)
        if form.is_valid():
            form.save()
            return redirect('produk_list')
    else:
        form = ProdukForm(instance=produk)
    return render(request, 'produk_form.html', {'form': form, 'title': 'Edit Produk'})

#Fitur Hapus (Poin 6)
def produk_hapus(request, id):
    produk = get_object_or_404(Produk, id_produk=id)
    produk.delete()
    return redirect('produk_list')