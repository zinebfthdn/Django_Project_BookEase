from django.shortcuts import render, get_object_or_404, redirect
from publisher.models import Book
from django.contrib.auth.models import User
from django.http import HttpResponse
from publisher.forms import BookForm
from .forms import PublisherEditForm
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    books = Book.objects.all()
    Users = User.objects.all()
    return render(request, 'adminpanel/index.html', {'books': books, 'Users': Users})


@login_required
def approve_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.approved = True
    book.save()
    return redirect('admin_index')


@login_required
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('admin_index')
    else:
        form = BookForm(instance=book)
    return render(request, 'adminpanel/edit_book.html', {'form': form, 'book': book})

@login_required
def view_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'adminpanel/view_book.html', {'book': book})

@login_required
def download_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    response = HttpResponse(book.pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{book.title}.pdf"'
    return response


def edit_publisher(request, publisher_id):
    publisher = get_object_or_404(User, id=publisher_id, user_type='publisher')
    if request.method == 'POST':
        form = PublisherEditForm(request.POST, instance=publisher)
        if form.is_valid():
            form.save()
            return redirect('admin_index')
    else:
        form = PublisherEditForm(instance=publisher)
    return render(request, 'adminpanel/edit_publisher.html', {'form': form})

@login_required
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return redirect('admin_index')

@login_required
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect('admin_index')