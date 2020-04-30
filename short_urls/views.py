from django.contrib import messages
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect

from short_urls.forms import UrlForm
from short_urls.models import URL


def home(request):
    if request.method == "POST":
        form = UrlForm(request.POST or None)
        if form.is_valid():
            url = form.cleaned_data.get("url")
            obj, created = URL.objects.get_or_create(url=url)
            domain = request.get_host()
            context = {
                "object": obj,
                "created": created,
                "form": form,
                "domain": domain
            }
            msg = 'Этот адрес уже существует'
            if created:
                msg = 'Короткий адрес был успешно создан.'
            messages.success(request, msg)
            return render(request, 'short_urls/home.html', context)
        return render(request, 'short_urls/home.html', {"form": form})
    form = UrlForm()
    return render(request, 'short_urls/home.html', {"form": form})


def url_redirect(request, short_url=None):
    if short_url:
        qs = URL.objects.filter(short=short_url)
        if not qs.exists():
            raise Http404
        obj = qs.first()
        obj.cnt += 1
        obj.save()
        return HttpResponseRedirect(obj.url)
    return redirect('home')
