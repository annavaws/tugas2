Link menuju ke aplikasi https://aplikasi-katalog.herokuapp.com/
1. 
2. Alasan menggunakan virtual environment adalah untuk dapat mengisolasi package dan dependencies dari aplikasi yang dibuat supaya tidak mempengaruhi aplikasi lainnya dengan kata lain supaya masing-masing aplikasi memiliki modul sendiri.
Kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment hanya saja ada kemungkinan besar hasil yang dihasilkan dapat bertabrakan dengan proyek lain yang sudah pernah dibuat
3. Untuk poin 1, saya membuat fungsi show_katalog(request) yang berfungsi untuk mengambil data dari model(CatalogItem) dan mengembalikan data tersebut ke dalam katalog.html. 
    def show_katalog(request):
        data_barang_katalog = CatalogItem.objects.all()
        context = {
        'list_barang': data_barang_katalog,
        'nama': 'Annava',
        'id':'2106635493'
        }
        return render(request, "katalog.html", context)
    Untuk poin 2,Membuat sebuah routing untuk memetakan fungsi yang telah kamu buat pada views.py.
    Untuk poin 3,Memetakan data yang didapatkan ke dalam HTML dengan sintaks dari Django untuk pemetaan data template.
    Untuk poin 4,Melakukan deployment ke Heroku terhadap aplikasi yang sudah kamu buat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.


