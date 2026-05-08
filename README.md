# Simulasi Static Uneven Distribution
**Nama:** [Isi Nama Kamu]  
**NRP:** 174 (Genap)  
**Mata Kuliah:** Komputasi Paralel & Sistem Terdistribusi

## Deskripsi Tugas
Tugas ini mendemonstrasikan pembagian beban kerja secara statis namun tidak merata (uneven) menggunakan library `multiprocessing` di Python.

## Analisis Hasil
Berdasarkan hasil eksekusi program:
1. **Static Distribution:** Tugas (Task 1-4) dibagikan secara tetap sebelum eksekusi dimulai.
2. **Uneven Load:** Beban kerja bervariasi antara 1 detik hingga 5 detik.
3. **Ideal Reach:** Kondisi ideal tercapai karena total waktu eksekusi (~5.28 detik) mendekati durasi tugas terberat (5 detik). Ini membuktikan bahwa core prosesor bekerja secara paralel, bukan sekuensial.
