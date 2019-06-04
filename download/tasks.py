import youtube_dl
from mp3_downloader.celery import app
from django.core.mail import send_mail
from django.conf import settings


@app.task
def download(url, email, host):
    options = {
        'format': 'bestaudio/best',
        'outtmpl': 'media/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]}
    with youtube_dl.YoutubeDL(options) as ydl:
        info = ydl.extract_info(url)
        file_title = info['title']
        link = ('http://'+host+'/media/'+file_title).replace(" ", "%20")+'.mp3'
        send_mail(
            'Download link',
            link,
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False
        )

