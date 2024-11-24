from flask import Flask, render_template, request, send_file, jsonify
import yt_dlp
import os
from flask_cors import CORS  # Import CORS untuk menangani CORS

app = Flask(__name__)

# Aktifkan CORS untuk seluruh aplikasi
CORS(app)

# Folder untuk menyimpan file yang diunduh
DOWNLOAD_FOLDER = "downloads"
if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/convert", methods=["POST"])
def convert():
    data = request.get_json()  # Ambil data JSON yang dikirim dari frontend
    url = data.get("url")

    if not url:
        return jsonify({"error": "URL is required"}), 400

    # Download video dari URL menggunakan yt-dlp
    ydl_opts = {
        'format': 'bestaudio/best',  # Mendownload audio terbaik
        'outtmpl': os.path.join(DOWNLOAD_FOLDER, '%(id)s.%(ext)s'),  # Menyimpan di folder yang sudah dibuat
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',  # Gunakan postprocessor yang benar
            'preferredcodec': 'mp3',  # Mengonversi ke MP3
            'preferredquality': '192',  # Kualitas MP3
        }],
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            video_id = info_dict.get("id")
            filename = f"{video_id}.mp3"
        
        mp3_file = os.path.join(DOWNLOAD_FOLDER, filename)
        return send_file(mp3_file, as_attachment=True)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
