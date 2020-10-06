# Penting
- Repo original https://github.com/lzzy12/python-aria-mirror-bot
- So, credits dimiliki pemilik repo.
- Repo in (atau custom repo lain) tidak disupport pada official bot support group.
- jadi jika kamu mengalami masalah cek apakah masalah tersebut ada di repo official atau tidak, Kamu hanya boleh melaporkan masalah pada grup official jika masalah juga ada pada repo official.

## Credits :-
- First of all, full credit goes to [Shivam Jha aka lzzy12](https://github.com/lzzy12) He build up this bot from scratch.
- Then a huge thanks to [Sreeraj V R](https://github.com/SVR666) You can checkout his [repo here](https://github.com/SVR666/LoaderX-Bot)
- Features added from [Sreeraj V R's](https://github.com/SVR666) repo -
```
1. Added Inline Buttons
2. Added /del command to delete files from drive
3. /list module will post search result on telegra.ph
```
- Special thanks to [archie](https://github.com/archie9211) for very much useful feature **Unzipmirror**
- Features added from [archie's](https://github.com/archie9211) repo
- UPTOBOX support added [jovanzers](https://github.com/jovanzers) 
```
1. unzipmirror
2. Update tracker list dynamically
3. Fix SSL handsake error
```

# Repo apa ini?
Ini adalah repo telegram bot yang akan mengupload file ke google drive.
# Inspiration 
This project is heavily inspired from @out386 's telegram bot which is written in JS.

# Features supported:
- Mirroring direct download links to google drive
- Mirroring Mega.nz links to google drive (In development stage)
- Mirror Telegram files to google drive
- Mirror all youtube-dl supported links
- Extract these filetypes and uploads to google drive
> ZIP, RAR, TAR, 7z, ISO, WIM, CAB, GZIP, BZIP2, 
> APM, ARJ, CHM, CPIO, CramFS, DEB, DMG, FAT, 
> HFS, LZH, LZMA, LZMA2, MBR, MSI, MSLZ, NSIS, 
> NTFS, RPM, SquashFS, UDF, VHD, XAR, Z.
- Copy files from someone's drive to your drive (using Autorclone)
- Service account support in cloning and uploading
- Download progress
- Upload progress
- Download/upload speeds and ETAs
- Docker support
- Uploading To Team Drives.
- Index Link support
- Shortener support

## Bot commands yang harus diset pada botfather

```
mirror - Start Mirroring
tarmirror - Upload tar (zipped) file
unzipmirror - Extract file
salin - salin folder ke drive
ytdl - mirror YT-DL support link
tarytdl - mirror youtube playlist link sebagai tar
batal - batalkan tugas
batalsemua - batalkan semua tugas
hapus - hapus file dari Drive
daftar - [query] mencari file di G-Drive
status - menampilkan Status Mirror
stats - Statistik bot
bantuan - Bantuan
log - Bot Log [hanya pemilik]
```

# How to deploy? Simple Method
Ikuti langkah ini:
## Installing requirements
```
ikuti langkah
1. Fork Repo ini
2. Credentials.json & Token Pickle
3. User Session String.
4. Klik pada tombol Deploy, dan isi kolom

```

```
STEP 1 :
Signup or Login to your account then :
- Fork this repo
After forked, you need to upload Credentials.json, token.pickle and token_sa.pickle to your forked repo.
If Using SA's you will also need to upload your accounts folrder.

Proceed to step 2

```

```
STEP 2 :

## Getting Google OAuth API credential file

- Buka link [Google Cloud Console](https://console.developers.google.com/apis/credentials)
- Pergi ke OAuth Consent tab, isi terus simpan.
- Pergi ke Credentials tab terus klik Create Credentials -> OAuth Client ID
- Pilih Desktop dan Create.
- Download credentials yang barusan dibuat (ada icon download gitu).
- Pindahkan ke dalam folder projek ini terus rename jadi credentials.json
- Pergi ke [Google API page](https://console.developers.google.com/apis/library)
- Cari Drive terus enable jika sebelumnya disabled
- Jalankan perintah ini untuk membuat file token (token.pickle) untuk Google Drive:

pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib
python3 generate_drive_token.py

Sekarang kita punya 
Credentials.json and token.pickle.. so Upload these files to your forked repo.
```



```
STEP 3 :
Untuk mendapatkan user session string jalankan perintah :
   python3 generate_string_session.py
```

```
STEP 4
## Deploying
KLIK TOMBOL DEPLOY PADA REPO YANG KAMU FORK, ITU SAJA !
```
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)


# How to deploy? Cara manual
Ikuti langkah berikut:
## Installing requirements

- Clone repo ini:
```
git clone https://github.com/bigbabyboost/WinTenCermin
cd mirror-bot
```

- Install requirements
Untuk base Debian
```
sudo apt install python3
sudo snap install docker 
```
- Untuk Arch dan turunannya:
```
sudo pacman -S docker python
```

## Setting up config file
- Copy file config_sample.env dan rename jadi config.env
```
cp config_sample.env config.env
```
- Hapus baris ini:
```
_____REMOVE_THIS_LINE_____=True
```
Isi data sesuai permintaan
- **BOT_TOKEN** : Telegram bot token dari @BotFather
- **GDRIVE_FOLDER_ID** : ID Folder Google Drive buat tempat upload hasil download
- **DOWNLOAD_DIR** : Lokasi unduhan default di servermu
- **DOWNLOAD_STATUS_UPDATE_INTERVAL** : Lama waktu status download diupdate, default 5
- **OWNER_ID** : user ID Telegram pembuat (bukan username). Cek id? Pake aja bot https://t.me/myidbot
- **AUTO_DELETE_MESSAGE_DURATION** : Lama waktu untuk menghapus pesan yang dikirim ke bot
- **IS_TEAM_DRIVE** : (optional) set "True" jika ingin menggunakan Team Drive
- **USE_SERVICE_ACCOUNTS**: Kalau ga paham kosongin aja.
- **INDEX_URL** : Link Google Drive Index, Baca aja di sini https://github.com/maple3142/GDIndex/
- **API_KEY** : Buat download file dari telegram butuh API ini, dambil di https://my.telegram.org (tanpa "")
- **API_HASH** : Buat download file dari telegram butuh API ini, dambil di https://my.telegram.org
- **USER_SESSION_STRING** : Jalankan perintah ini untuk ngambil session string:
```
python3 generate_string_session.py
```
- **MEGA_API_KEY**: API Mega.nz buat download dari mega.nz. Ambil di [Mega SDK Page](https://mega.nz/sdk)
- **MEGA_EMAIL_ID**: Email mega.nz untuk make akun premium
- **MEGA_PASSWORD**: Password mega.nz 
- **UPTOBOX_TOKEN**: Uptobox token untuk mirror uptobox links. Dapatkan disini [Uptobox Premium Account](https://uptobox.com/my_account)
- **STOP_DUPLICATE_MIRROR**: (Optional) (Kosongkan jika tidak yakin) kolom ini diset `True` , bot akan mengecek file di drive, jika sudah ada download dibatalkan. (Note - File dicek menggunakan nama file bukan hashfile, fitur belum sempurna)
- **BLOCK_MEGA_LINKS**: (Optional) jika ingin menghapus mega.nz mirror support (karena buggy dan tidak stabil), set ke `True`
- **SHORTENER**: (Optional) jika ingin menggunakan link shortener pada Gdrive dan index link, isi shotener url disini. Contoh :-

> exe.io

> gplinks.in

> shrinkme.io

> urlshortx.com

> shortzon.com

Note :- Diatas adalah url shortener yang disupport.
- **SHORTENER_API**: Isi shortener API jika menggunakan shortener

Note: Kalian bisa atur maksimal proses download dalam 1 waktu di MAX_CONCURRENT_DOWNLOADS di aria.sh. Bawaannya itu 4
 
## Ambil API Google OAuth credential file

- Buka link [Google Cloud Console](https://console.developers.google.com/apis/credentials)
- Pergi ke OAuth Consent tab, isi terus simpan.
- Pergi ke Credentials tab terus klik Create Credentials -> OAuth Client ID
- Pilih Desktop dan Create.
- Download credentials yang barusan dibuat (ada icon download gitu).
- Pindahkan ke dalam folder projek ini terus rename jadi credentials.json
- Pergi ke [Google API page](https://console.developers.google.com/apis/library)
- Cari Drive terus enable klo sebelumnya disabled
- Jalankan perintah ini untuk membuat file token (token.pickle) untuk Google Drive:
```
pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib
python3 generate_drive_token.py
```

## Deploying

- Start docker daemon (skip if already running):
```
sudo dockerd
```
- Build Docker image:
```
sudo docker build . -t mirror-bot
```
- Run the image:
```
sudo docker run mirror-bot
```

# Menggunakan Service Account
Agar Service Account bekerja, set USE_SERVICE_ACCOUNTS="True" pada config file
Many thanks to [AutoRClone](https://github.com/xyou365/AutoRclone) untuk scripts
## Generating service accounts
Step 1. Generate service accounts [What is service account](https://cloud.google.com/iam/docs/service-accounts)
---------------------------------
Biarkan kami membuat Service Account yang dibutuhkan. 
**Warning:** penyalahgunaan fitur ini bukanlah tujuan autorclone dan kami **TIDAK** merekomendasi membuat banyak project, hanya satu project dan 100 sa sudah cukup

```
Note: 1 service account dapat menyalin 750gb sehari, 1 project membuat 100 service accounts jadi 75tb sehari, itu sudah cukup. 
```

`python3 gen_sa_accounts.py --quick-setup 1 --new-only`

Sebuah folder bernama "accounts" akan dibuat yang berisi SA

NOTE: Jika kamu pernah membuat SAs dari script ini, kamu dapat mendownload key langsung dengan menjalankan perintah:
```
python3 gen_sa_accounts.py --download-keys project_id
```
# Menggunakan akun di web yang support Youtube-dl
Klo mau make premium akun yang support di youtube-dl, ubah netrc file dengan format:
```
machine host login username password my_youtube_password
```
host ini adalah website tujuan, misalnya youtube, twitch, dll. 
klo mau lebih dari 2 akun tinggal tambahin aja di baris baru.


# Thanks to
- jovanzers
- WinTenDev
