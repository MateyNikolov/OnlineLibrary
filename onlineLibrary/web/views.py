from django.shortcuts import render, redirect

from onlineLibrary.web.forms import BaseProfileForm, BaseBookForm, EditBookForm, EditProfileForm, DeleteProfileForm
from onlineLibrary.web.models import Profile, Book


def get_profile():
    try:
        profile = Profile.objects.get()
        return profile
    except Profile.DoesNotExist as ex:
        return None


def show_home_page(request):
    profile = get_profile()
    if profile:
        books = Book.objects.all()

        context = {
            'books': books,
            'profile': profile,

        }
        return render(request, 'home/home-with-profile.html', context)
    else:
        if request.method == 'GET':
            form = BaseProfileForm()
        else:
            form = BaseProfileForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('index')

        context = {
            'form': form,
        }

        return render(request, 'home/home-no-profile.html', context)


def add_book(request):
    if request.method == 'GET':
        form = BaseBookForm()
    else:
        form = BaseBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'profile': get_profile(),
    }

    return render(request, 'book/add-book.html', context)


def edit_book(request, pk):
    current_book = Book.objects.get(pk=pk)
    if request.method == 'GET':
        form = EditBookForm(instance=current_book)
    else:
        form = EditBookForm(request.POST, instance=current_book)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'profile': get_profile(),
        'book': current_book,
    }

    return render(
        request,
        'book/edit-book.html',
        context
    )


def details_book(request, pk):
    current_book = Book.objects.get(pk=pk)

    context = {
        'book': current_book,
    }

    return render(
        request,
        'book/book-details.html',
        context,
    )


def delete_book(request, pk):
    current_book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        current_book.delete()
        return redirect('index')


def show_profile(request):
    profile = Profile.objects.get()

    context = {
        'profile': profile
    }

    return render(
        request,
        'profile/profile.html',
        context
    )


def edit_profile(request):
    if request.method == 'GET':
        form = EditProfileForm(instance=get_profile())
    else:
        form = EditProfileForm(request.POST, instance=get_profile())
        if form.is_valid():
            form.save()
            return redirect('profile')

    context = {
        'form': form,
    }

    return render(
        request,
        'profile/edit-profile.html',
        context
    )


def delete_profile(request):
    if request.method == 'GET':
        form = DeleteProfileForm(instance=get_profile())
    else:
        form = DeleteProfileForm(request.POST, instance=get_profile())
        if form.is_valid():
            form.save()
            Book.objects.all().delete()
            return redirect('index')

    context = {
        'form': form,
    }

    return render(
        request,
        'profile/delete-profile.html',
        context
    )
