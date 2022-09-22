<h1> Link menuju ke aplikasi https://aplikasi-katalog.herokuapp.com/mywatchlist/ </h1>
<h2>1. Jelaskan perbedaan antara JSON, XML, dan HTML!</h2>
<p>JSON merupakan format data yang cara penulisannya menggunakan objek JavaScript. XML adalah bahasa markup. JSON menyimpan elemen secara efisien sehingga tidak rapi untuk diliat berbeda dengan XML yang menyimpan elemennya secara terstruktur, sehingga mudah dibaca oleh pengguna. HTML adalah bahasa yang menggunakan tag yang akan ditafsirkan oleh browser sehingga dapat ditampilkan secara tepat.
</p>
<h2>2. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?</h2>
<p>Untuk mengirim data dari satu stack ke stack lainnya, data yang dikirim juga dapat bermacam-macam seperti html, xml, dan json.</p>
<h2>3. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.</h2>
<p>Awalnya menggunakan command python manage.py startapp mywatchlist untuk membuat aplikasi baru pada repositori. 
Setelah itu di project_django menambahkan path mywatchlist pada urls.py dan pada variabel INSTALLED_APPS di settings.py menambahkan mywatchlist. 
Setelah itu membuat model MyWatchList di models.py milik mywatchlist. Lalu membuat folder baru fixtures yang berisi file json dan folder templates berisi file .html yang akan menjadi tampilannya. Untuk menyajikan data menjadi format html, xml, dan json pada file views.py, kita mengimport HttpResponse dan Serializer, setelah itu mereturn function berupa HttpResponse yang berisi parameter data hasil query yang sudah diserialisasi menjadi XML dan juga JSON. Lalu menambahkan urlnya pada urls.py</p>
![html](https://user-images.githubusercontent.com/93859147/191661713-4aa0a9f6-f90d-4db2-ac7b-6653b7a9d961.jpg)
![json](https://user-images.githubusercontent.com/93859147/191661757-fcbe7faf-7e72-448e-9198-ed31d1e7690f.jpg)
![xml](https://user-images.githubusercontent.com/93859147/191661765-6615fbdf-f92b-4fe6-908e-f710fbda21e8.jpg)
