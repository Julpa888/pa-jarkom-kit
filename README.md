# 🌷 PA Jarkom Survival Kit — Huawei VRP (eNSP)

Aplikasi web belajar interaktif untuk persiapan Proyek Akhir Praktikum Jaringan Komputer menggunakan perangkat **Huawei VRP (eNSP)**.

## Fitur Utama
1. **3 Mode Tema Real-Time** (tersimpan di `localStorage`):
   - 🌸 **Pink Coquette (Default)**
   - ☀️ **Light Clean**
   - 🌙 **Dark Hacker Mode**
2. **Smart Huawei VRP CLI Simulator**:
   - Mendukung singkatan resmi Huawei VRP & bersifat *case-insensitive* (`sys`, `u t m`, `sy [nama]`, `int g0/0/1`, `int g0/0/1.10`, `int eth-trunk 1`, `int vlanif 10`, `int lo0`, `ip add ...`, `dis this`, `dis cur`, `dis stp br`, `q`).
   - Dilengkapi tombol **💡 Hint**, **⏭️ Skip Step**, dan **🔄 Reset Terminal**.
3. **Kurikulum Lengkap 8 Modul Praktikum + 2 Boss Battle (Simulasi PA)**:
   - Modul 1: Basic Configuration
   - Modul 2: FTP (File Transfer Protocol)
   - Modul 3: Static Route & OSPF
   - Modul 4: Ethernet Basics & VLAN Configuration
   - Modul 5: Ethernet Link Aggregation & Inter-VLAN Communication
   - Modul 6: Spanning Tree Protocol (STP & RSTP)
   - Modul 7: DHCP & WLAN (AC + AP)
   - Modul 8: ACL (Access Control List)
   - 🌟 Boss Battle 1: Simulasi Posttest 7 (Router-on-a-Stick + Multi-VLAN + DHCP Static Bind)
   - 🔥 Boss Battle 2: Prediksi PA Lengkap (Multi-Area OSPF + 6 VLAN Sekolah + Inter-VLAN)

## Cara Menjalankan dengan Python Flask
1. Ekstrak file `.zip` ini.
2. Install Flask:
   ```bash
   pip install -r requirements.txt
   ```
3. Jalankan server:
   ```bash
   python app.py
   ```
4. Buka browser ke `http://127.0.0.1:5000` (atau buka langsung `templates/index.html` di browser).
