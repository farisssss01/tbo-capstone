# TBO Studio
### Capstone Project - Teori Bahasa dan Otomata

TBO Studio adalah aplikasi berbasis **Flask** yang dikembangkan sebagai proyek Capstone Mata Kuliah **Teori Bahasa dan Otomata**. Aplikasi ini menyediakan simulasi beberapa konsep utama dalam teori bahasa formal dan automata secara interaktif melalui web.

---

## Fitur

### 1. Finite State Automata (FSA)

- Simulasi Deterministic Finite Automata (DFA)
- Input State
- Input Alphabet
- Input Transition
- Input Start State
- Input Final State
- Simulasi Input String
- Trace Perpindahan State
- Visualisasi Diagram DFA
- Tabel Transisi

---

### 2. Regular Expression

- Regex Matcher
- Validasi String
- Penjelasan Operator Regular Expression

---

### 3. Context Free Grammar (CFG) & Pushdown Automata (PDA)

- Input Grammar CFG
- Validasi Grammar
- Leftmost Derivation
- Parse Tree Visualization
- Simulasi Stack PDA

---

### 4. Chomsky Hierarchy

- Analisis Grammar
- Klasifikasi Grammar
- Konversi menuju Chomsky Normal Form (CNF)

---

## Teknologi

- Python 3
- Flask
- Bootstrap 5
- NetworkX
- Matplotlib

---

## Struktur Project

```
tbo-capstone/

│

├── app.py

├── requirements.txt

├── README.md

│

├── modules/

│   ├── cfg.py
│   ├── chomsky.py
│   ├── fsa.py
│   ├── graph.py
│   ├── parser.py
│   ├── pda.py
│   ├── regex_engine.py
│   └── tree.py

│

├── templates/

│

├── static/

│

└── docs/
```

---

## Instalasi

Clone repository

```bash
git clone https://github.com/USERNAME/tbo-capstone.git
```

Masuk ke folder project

```bash
cd tbo-capstone
```

Install dependency

```bash
pip install -r requirements.txt
```

Jalankan aplikasi

```bash
python app.py
```

Buka browser

```
http://127.0.0.1:5000
```

---

## Tampilan Aplikasi

- Dashboard
- Finite State Automata
- Regular Expression
- CFG & PDA
- Hierarki Chomsky

---

## Pengembang

**Faris**

Mahasiswa Teknik Informatika

---

## Lisensi

Project ini dibuat untuk memenuhi tugas Capstone Mata Kuliah Teori Bahasa dan Otomata."# tbo-capstone" 
