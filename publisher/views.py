from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Book
from .forms import BookForm
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    books = Book.objects.filter(user=request.user)
    return render(request, 'publisher/index.html', {'books': books})

@login_required
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.user = request.user
            book.save()
            return redirect('publisher_index')
    else:
        form = BookForm()
    return render(request, 'publisher/add_book.html', {'form': form})


@login_required
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('publisher_index')
    else:
        form = BookForm(instance=book)
    return render(request, 'publisher/edit_book.html', {'form': form})


@login_required
def download_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    response = HttpResponse(book.pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{book.title}.pdf"'
    return response
