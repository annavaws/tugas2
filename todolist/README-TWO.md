<h1> Link menuju ke aplikasi https://aplikasi-katalog.herokuapp.com/todolist/ </h1>
<h2>Perbedaan antara asynchronous programming dengan synchronous programming.</h2>
<p>Perbedaanya adalah cara program mengeksekusi program yang mempengaruhi lama waktunya.
Untuk asynchronous akan memakan waktuyang lebih singkat karena dapat mengeksekusi banyak function secara bersamaan. Untuk synchronous
waktu eksekusi akan lebih panjang karena menunggu function lain sampai selesai baru dapat
melanjutkannya dengan function lain.

<br></p>

<h2>Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. <br>Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.</h2>
<p>
Paradigma Event-Driven Programming adalah suatu alur pemrograman yang alurnya ditentukan
oleh sebuah event, seperti ketika suatu button yang diklik.
Contoh penerapan yang saya gunakan adalah <br>
 $("#btn_trigger").click(function(e){<br>
       <tab>console.log("triggerrr")<br>
       <tab>e.preventDefault();<br>
       <tab>$("#id_modal").modal();<br>
    });
Ketikan button diklik, maka akan mentrigger form modal untuk keluar
<br></p>

<h2> Jelaskan penerapan asynchronous programming pada AJAX.</h2>
<p>
Penerapannya adalah AJAX membuat halaman web menjadi asynchronous dengan mengirimkan
data ke server di balik layar. Sehingga kita dapat memperbarui sebagian elemen data 
pada halaman tanpa harus me-reload keseluruhan halaman.
<br></p>

<h2>Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.</h2>
<p>
- Membuat view baru show_json untuk mendapatkan data dalam bentuk json, lalu menghubungkannya dengan
path /todolist/json pada urls.py
- Menggunakan AJAX GET untuk mengambil data
- Membuat task modal dan button 'Add Task' berserta fungsinya yang berguna untuk membuka task modal tersebut
- Membuat view baru add pada views.py dan path /todolist/add pada urls.py
- Melakukan pengiriman data menggunakan AJAX POST
- Melakukan git add, commit, dan pull ke repository dan deploy ke Heroku
<br></p>
