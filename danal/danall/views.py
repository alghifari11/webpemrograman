from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Selamat Datang di Situs Saya</h1><p>Terima kasih telah mengunjungi situs saya. perkenalkan nama saya Akhdan Al-ghifari!</p>")
