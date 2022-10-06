<h1> Link menuju ke aplikasi https://aplikasi-katalog.herokuapp.com/todolist/ </h1>

<h2>
Akun: akunPertama
Pass: akundummy1
Akun: akunKedua
Pass: akundummy2

</h2>

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
</p>

<h2>Tugas 5</h2>

<h2>Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?</h2>
<p>
Inline CSS artinya stylenya langsung ditulis pada suatu tag. Misalnya < h3 style = "color: blue">Hello</h3 >
Internal CSS artinya stylenya berada pada <head> document tersebut dan bisa menggunakan class selector atau id selector.
External CSS artinya stylenya berada pada folder static dengan file .css, cara menghubungakan html dan .css
adalah dengan menyisipkan link pada file html. Dan harus menambahkan tag {% load staticfiles %}.
Kelebihan Inline adalah akan berguna jika ingin melihat perubahan pada satu elemen sehingga mudah untuk memperbaiki kode dan proses load website juga akan lebih cepat.
Kekurangan Inline adalah tidak efisien jika terdapat banyak elemen.
Kelebihan Internal adalah bisa menggunakan class dan id selector pada <style>
Kekurangan Internal adalah performa web bisa melambat karena setiap halaman perlu load css beda.
Kelebihan External adalah ukuran file html menjadi lebih kecil dan file css dapat digunakan beberapa halaman website sekaligus sehingga load website juga akan cepat.
Kekurangan External adalah halaman berpotensi berantakan jika file css tidak berhasil dipanggil oleh html
karena koneksi internet tidak bagus.
</p>

<h2>Jelaskan tag HTML5 yang kamu ketahui.</h2>
<p> 
< a > mendefinisikan hyperlink<br>
< b > mendefinisikan bold style pada text<br>
< body > mendefinisikan body dari dokumen<br>
< br > membuat new line <br>
< button > membuat button yang dapat diklik<br>
< div > menspesifikasikan sebuah section pada dokumen<br>
< form > mendefinisikan form html <br>
< head > mendefinisikan porsi head dari dokumen yang berisi informasi tentang dokumen misalnya title<br>
< img > merepresentasikan gambar<br>
< input > mendefinisikan tempat input<br>
< label > mendefinisikan sebuah label untuk kontrol < input > <br>
< meta > mendefinisikan memberi metadata terstruktur mengenai isi dokumen<br>
< style > untuk mengisi informasi style seperti CSS pada head<br>
< table > mendefinisikan table<br>
< td > mendefinisikan cell pada table<br>
< th > mendefinisikan header cell pada table<br>
< tr > mendefinisikan row dari cells pada table<br>
</p>


<h2>Jelaskan tipe-tipe CSS selector yang kamu ketahui.</h2>
<p>
1. Element Selector
Element selector menggunakan tag HTML sebagai selector untuk mengubah properti yang terdapat dalam tag tersebut.

2. ID Selector(#id)
ID selector menggunakan ID pada tag sebagai selector-nya. Menggunakan karakter # diikuti dengan id.

3. Class Selector(.class)
Class selector digunakan untuk memperindah tampilan template HTML dengan menambahkan class pada tag HTML,
lalu menambahkan class selector pada file css. Menggunakan karakter . diikuti dengan nama class.

4. Hover (:hover)
Memilih link dengan mouse 

dan masih banyak lagi yang bisa dibaca dari link berikut <a href="https://www.w3schools.com/cssref/css_selectors.asp">ini</a>
</p>

<h2>Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.</h2>
<p>
Menganti isi file html login, register, todolist_form, dan todolist dengan menambahkan framework bootstrap dan menggunakan internal css. Dan menambahkan line <meta name="viewport" content="width=device-width, initial-scale=1"> untuk membuatnya jadi responsive. Setelah itu membuat card dengan mengambil referensi dari <a href ="https://getbootstrap.com/docs/4.1/components/card/#card-groups">ini</a>.

</p>
