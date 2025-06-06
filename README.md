#  QuizTube: Kuis Interaktif dari Video YouTube dengan Streamlit

## Deskripsi Singkat
QuizTube adalah aplikasi yang memudahkan Anda mengubah video YouTube menjadi kuis interaktif secara otomatis. Latar belakang aplikasi ini adalah kebutuhan untuk meningkatkan pemahaman dan interaksi terhadap konten video edukasi, tutorial, atau hiburan. Dengan QuizTube, pengguna dapat menguji pemahaman mereka terhadap isi video secara langsung melalui soal-soal yang dihasilkan oleh AI.

## Fitur-Fitur Utama
- Ekstraksi subtitle/caption otomatis dari video YouTube (menggunakan youtube-transcript-api)
- Pembuatan soal kuis pilihan ganda secara otomatis dengan LLM (OpenRouter/DeepSeek)
- Antarmuka interaktif berbasis Streamlit
- Penilaian otomatis dan review jawaban


## Cara Menjalankan di Lokal
1. **Clone repository dan masuk ke folder project**
2. **Aktifkan virtual environment** (jika belum):
   ```powershell
   .\myvenv\Scripts\Activate.ps1
   ```
3. **Install dependencies**
   ```powershell
   pip install -r requirements.txt
   ```
4. **Jalankan aplikasi**
   ```powershell
   streamlit run streamlit_app.py
   ```
5. **Buka browser ke** [http://localhost:8501](http://localhost:8501)

## Preview Aplikasi


![Preview QuizTube](preview.png)

## Link Deploy Aplikasi
👉 [QuizTube Online](https://quiztube.streamlit.app/)


