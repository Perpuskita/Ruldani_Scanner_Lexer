
Cara Mesin Finite automata Menentukan inputan yang "Salah"

Berakhir di State Bukan Akhir (Non-Final State): Jika seluruh simbol pada string input telah habis dibaca dan posisi mesin berhenti di state yang bukan termasuk himpunan final state (\(F\)), maka string tersebut ditolak.

Menuju Trap State (State Jebakan): Dalam desain DFA yang lebih ketat (seperti sistem keamanan atau validasi), input yang menyimpang dari aturan sering kali diarahkan ke trap state atau dead state (state khusus yang terus melingkar ke dirinya sendiri atau tidak memiliki jalan keluar ke final state), sehingga sisa input akan otomatis digagalkan.

Simbol Tidak Terdaftar: Jika mesin menerima simbol yang tidak ada di dalam alfabet (\(\Sigma \)) yang didefinisikan oleh DFA tersebut, secara formal mesin tidak akan bisa melakukan fungsi transisi (\(\delta \)) dan proses akan terhenti/gagal.