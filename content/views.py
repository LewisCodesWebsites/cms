from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistrationForm, ContentItemForm
from .models import ContentItem


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("content_list")
    else:
        form = RegistrationForm()
    return render(request, "registration/register.html", {"form": form})


@login_required
def content_list(request):
    items = ContentItem.objects.filter(created_by=request.user)
    return render(request, "content/list.html", {"items": items})


@login_required
def content_create(request):
    if request.method == "POST":
        form = ContentItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect("content_detail", pk=item.pk)
    else:
        form = ContentItemForm()
    return render(request, "content/form.html", {"form": form, "create": True})


@login_required
def content_detail(request, pk):
    item = get_object_or_404(ContentItem, pk=pk, created_by=request.user)
    return render(request, "content/detail.html", {"item": item})


@login_required
def content_edit(request, pk):
    item = get_object_or_404(ContentItem, pk=pk, created_by=request.user)
    if request.method == "POST":
        form = ContentItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("content_detail", pk=item.pk)
    else:
        form = ContentItemForm(instance=item)
    return render(request, "content/form.html", {"form": form, "create": False})
