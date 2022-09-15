<h1> Link menuju ke aplikasi https://aplikasi-katalog.herokuapp.com/ </h1>
<p> 1. ![user](https://user-images.githubusercontent.com/93859147/190316618-a0868305-06ec-46aa-ad41-8ed978ee1f94.jpg)
Awalnya permintaan user masuk ke server Django akan diproses melalui urls (request HTTP) kemudian ke views. Jika perlu masuk ke database, maka views akan memanggil query ke models dan hasilnya dikembalikan ke views. Setelah itu, hasilnya akan dipetakan ke template berupa HTML yang dapat dilihat oleh user.


2. Alasan menggunakan virtual environment adalah untuk dapat mengisolasi package dan dependencies dari aplikasi yang dibuat supaya tidak mempengaruhi aplikasi lainnya dengan kata lain supaya masing-masing aplikasi memiliki modul sendiri.
Kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment hanya saja ada kemungkinan besar hasil yang dihasilkan dapat bertabrakan dengan proyek lain yang sudah pernah dibuat.

3. Untuk poin 1, saya membuat fungsi show_katalog(request) yang berfungsi untuk mengambil data dari model(CatalogItem)dan mengembalikan data tersebut ke dalam katalog.html. 
    def show_katalog(request):
        data_barang_katalog = CatalogItem.objects.all()
        context = {
        'list_barang': data_barang_katalog,
        'nama': 'Annava',
        'id':'2106635493'
        }
        return render(request, "katalog.html", context)
    Untuk poin 2, saya membuat sebuah routing untuk memetakan fungsi yang telah dibuat pada views.py dengan menambahkan urlpatterns.
    app_name = 'katalog'
    urlpatterns = [
    path('', show_katalog, name='show_katalog'), ]

    Untuk poin 3, awalnya menggunakan perintah python manage.py makemigrations dan python manage.py migrate untuk mempersiapkan migrasi dan menerapkan skema model ke dalam database Django lokal. Setelah itu, menggunakan perintah python manage.py loaddata initial_catalog_data.json untuk memasukkan data ke dalam database Django lokal.
    Berikutnya, untuk mapping data yang di-render pada views.py akan mengakses katalog.html. Pada katalog.html menggunakan sintaks {{data} untuk menggambil data dari views.py.
  
    Untuk poin 4, cara melakukan deployment ke Heroku terhadap aplikasi yang sudah saya buat adalah dengan membuat aplikasi baru terlebih dahulu pada Heroku. Setelah itu pada repositori GitHub, saya menambahkan variable repository secret baru dengan API KEY dan nama aplikasi di Heroku.

</p>
