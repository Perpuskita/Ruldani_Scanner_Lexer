# reguler expression

Reguler expression adalah sebuah bahasa yang digunakan untuk membuat sebuah expressi dari sebuah pola. reguler expression pertama kali dikemukakan oleh Stephen Klenee pada tahun 1950. reguler expression ini merupakan salah satu elemen pondasi dari teori automata dan komputasi. Reguler expression digunakan pada design compiler dalam tahapan lexical analysis untuk mendeskripsikan jenis dari sebuah token.

Aturan dasar dalam reguler expression terdiri dari beberapa jenis operator ekspresi yang perlu diketahui. Ekspressi tersebut adalah klenee closure, concatination, dan alternation. Klenee closure menghasilkan penggabungan string beberapa kali maupun nol kali ( sehingga menghasilkan empty) dalam sebuah ekspressi. Concationation merupakan penggabungan dari beberapa string sehingga membentuk satu string. Alternation adalah operator dimana reguler expression hanya dapat memilih salah satu dari string yang diberikan.

Dalam reguler expression terdapat kaidah untuk mengatur ekspressi mana yang harus diselesaikan terlebih dahulu. aturan ini disebut sebagai presendece yang juga berlaku dalam ekspressi matematika. Klenee closure merupakan prioritas tertinggi dari urutan prosedur yang harus diselesaikan terlebih dahulu diikuti dengan concatination dan urutan terendahnya adalah alternation.

Untuk mendefinisikan reguler expression yang sangat panjang terdapar beberaoa operasi pembantu yang dapat digunakan. Bayangkan ketika ingin mendefinisikan alternation dari 1 sampai 4, sangat tidak efisien jika menuliskanya dengan (1|2|3|4) oleh karena itu operasi pembantu ini diperlukan. Beberapa operasi adalah sebagi berikut.

s?    = mendefinisikan opsional dari s atau bisa ditulis (s|epsilon)
s+    = mendefinisikan bahwa s harus dicetak 1 atau lebih
[a-z] = mendefinisikan karakter apapun dalam rentang tersebut
[^x]  = mendefinisikan karakter selain karakter tesebut