from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from blog.models import CommentForm, Comment


def index(request):
    return HttpResponse("Blog Sayfası")


@login_required(login_url='/login') #login olup olmadığını kontrol et
def addcomment(request, id, slug):
    url = request.META.get('HTTP_REFERER')  # son urlyi al
    if request.method == 'POST':  #form post edildiyse
        form = CommentForm(request.POST)
        if form.is_valid():
            current_user = request.user  #kullanıcı oturum bilgisine erişme
            data = Comment()  #model ile bağlantı kur
            data.user_id = current_user.id
            data.post_id = id
            data.subject = form.cleaned_data['subject']
            data.comment = form.cleaned_data['comment']
            data.ip = request.META.get('REMOTE_ADDR')  #client ip adresi alma
            data.save()  #veritabanına kaydet
            messages.success(request, "Yorumunuz gönderildi")
            return HttpResponseRedirect(url)
    messages.warning(request, "Hata: Yorumunuz gönderilemedi")
    return HttpResponseRedirect(url)
