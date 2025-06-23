# tes_markdesign
nama : Umi Aliya Ayu Adhiba

Pertanyaan 1 : Pasangan Jumlah Tertentu
Program mencari semua pasangan unik dari array yang jika dijumlahkan menghasilkan target, dengan kompleksitas O(n).
menampilkan Output : [(2, 3), (1, 4)]
Fungsi ini mencari semua pasangan angka unik dalam sebuah array yang jika dijumlahkan hasilnya sama dengan target tertentu.
Cara Kerja:
Gunakan set seen untuk menyimpan angka yang sudah diperiksa.
Untuk setiap angka, cari pasangan komplemennya (target - num)
Jika komplemen sudah ada di seen, tambahkan pasangan (min, max) ke output untuk menghindari duplikat urutan.

Pertanyaan 2 : Bentuk Kata dari Array Huruf
Program mengecek apakah kata target bisa dibentuk dari array huruf, satu kali pakai per huruf.
Fungsi ini memeriksa apakah sebuah kata (target) dapat dibentuk dari huruf-huruf yang tersedia dalam sebuah array (array).
Cara Kerja:
Hitung frekuensi tiap huruf dalam array.
Periksa setiap huruf dalam target apakah tersedia dalam jumlah cukup di array.
Jika semua huruf tersedia sesuai kebutuhan, fungsi mengembalikan True, jika tidak False.

Pertanyaan 3 : Urutkan Angka Tapi Tetap Posisi Ganjil
Program mengurutkan angka di indeks genap, tetapi mempertahankan angka pada indeks ganjil tetap di tempatnya.
Fungsi ini mengurutkan angka yang berada pada indeks genap di sebuah array, sedangkan angka di indeks ganjil tetap pada posisi aslinya.
Cara Kerja:
Ekstrak elemen pada indeks genap.
Urutkan elemen genap secara manual menggunakan manual_sort.
Kembalikan array baru dengan elemen genap yang sudah terurut dan elemen ganjil tetap di tempatnya.
