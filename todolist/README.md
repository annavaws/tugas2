<h1> Link menuju ke aplikasi https://aplikasi-katalog.herokuapp.com/todolist/ </h1>
<h2>1. Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?</h2>
<p>
csrf adalah Cross-Site Request Forgery gunanya untuk security, yaitu mencegah penyerang menggunakan script memanipulasi dokumen htmlnya
Yang akan terjadi jika tidak memiliki {% csrf_token %} pada elemen <form> adalah akan muncul page berisi pesan 
'Forbidden (403)
CSRF verification failed. Request aborted.'
</p>


<h2>2. Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})
Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual. </h2>
<p>
Kita dapat membuat elemen <form> secara manual. Misalnya seperti dibawah ini 
    `<label for="id_title">Title:</label>
    <input type="text" name="title" required="" id="id_title">
    <label for="id_description">Description:</label>
    <textarea name="description" cols="40" rows="10" required="" id="id_description"></textarea>`
Kita perlu mendefisini idnya dan id untuk labelnya harus sama.
</p>


<h2>3. Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.</h2>
<p>
Ketika user menekan button `Tambah Task Baru` pada halaman todolist atau langsung mengakses url `../create-task`, django akan memanggil fungsi create_task pada views.py dan melempar HTML yang berisi form. Setelah itu, user dapat mengisi data pada field tersebut
Setelah user mengisi data pada form, user dapat menekan tombol submit yang akan mengirim request POST. Lalu datanya akan diterima dalam bentuk form dan disimpan pada database.
</p>


<h2>4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.</h2>
<p>
Awalnya menggunakan command python manage.py startapp todolist untuk membuat aplikasi baru pada repositori. 
Setelah itu di project_django menambahkan path todolist pada urls.py dan pada variabel INSTALLED_APPS di settings.py menambahkan todolist. Setelah itu membuat model Task pada models.py dengan atribut user, date, title, description, dan is_finished. Lalu mengimplementasikan form registrasi, login, dan logout dengan mengikuti tutorial sebelumnya pada file
views.py dan menambahkannya pada urls.py untuk routing. Tidak lupa juga membuat tampilannya pada folder templates. Membuat tampilan utama todolist pada views.py show_todolist yang ditampilkan pada todolist.html beserta button-buttonnya. Tombol `Tambah Task Baru` akan melempar halaman ke link `../create-task/'. Fungsi create_task pada views.py untuk menampilkan form yaitu todolist_form.html. Setelah itu mendeploy ke Heroku dengan git add, commit, dan push ke repositori.