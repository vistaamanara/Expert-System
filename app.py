from flask import Flask
from flask_pymongo import PyMongo, MongoClient
from flask_caching import Cache

app = Flask(__name__)
# app.config['MONGO_URI'] = 'mongodb+srv://vista:vistasayangbangagan@cluster0.0fjmb6i.mongodb.net/'
# mongo = PyMongo(app)
app.secret_key = "sistempakar112023iqbal01"
client = MongoClient("mongodb+srv://vista:vistasayangbangagan@cluster0.0fjmb6i.mongodb.net/?retryWrites=true&w=majority")
db = client.get_database("expertsystem_database")
pengguna = db.dataPengguna
admin_tabel = db.dataAdmin
pertanyaan_identifikasi = db.pertanyaanidentifikasi
aturan = db.aturanLogika
pengetahuan = db.basisPengetahuan
datakorban = db.datapersonalkorban

cache = Cache(app)

# Konfigurasi Flask-Caching
app.config['CACHE_TYPE'] = 'simple'  # Jenis cache sederhana
app.config['CACHE_DEFAULT_TIMEOUT'] = 300  # Waktu kedaluwarsa cache dalam detik
app.config['CACHE_KEY_PREFIX'] = 'myapp_'  # Awalan kunci cache

from views import views
app.register_blueprint(views, url_prefix="/views")

if __name__ == "__main__":
    app.run(debug=True)