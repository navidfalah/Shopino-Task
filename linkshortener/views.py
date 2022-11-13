from django.shortcuts import render, redirect
from .models import Link

def redirect_page(request, slug):
    single_link = Link.objects.filter(new_link=slug).first()
    single_link.num_views = single_link.num_views + 1
    single_link.save()
    return redirect(single_link.old_link)
