from django.shortcuts import render, redirect
from .models import Movie, Comment
from .forms import MovieForm, CommentForm


def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)


def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.user = request.user
            movie.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm()
    context = {
        'form': form,
    }
    return render(request, 'movies/create.html', context)


def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    comment_form = CommentForm()
    comments = movie.comment_set.all()
    context = {
        'movie': movie,
        'comment_form' : comment_form,
        'comments' : comments,
    }
    return render(request, 'movies/detail.html', context)


def delete(request, pk):
    movie = Movie.objects.get(pk=pk)
    movie.delete()
    return redirect('movies:index')


def update(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm(instance=movie)
    context = {
        'movie': movie,
        'form': form,
    }
    return render(request, 'movies/update.html', context)

def comments_create(request, pk):
    
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    movie = Movie.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.movie = movie
        comment.user = request.user
        comment.save()
    return redirect('movies:detail', movie.pk)

def comments_delete(request, movie_pk, comment_pk):

    if not request.user.is_authenticated:
        return redirect('accounts:login')
    comment = Comment.objects.get(pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
    return redirect('movies:detail', movie_pk)


def likes(request, pk):
    if request.user.is_authenticated:
        movie = Movie.objects.get(pk=pk)
        if movie.like_users.filter(pk=request.user.pk).exists():
            movie.like_users.remove(request.user)
        else:
            movie.like_users.add(request.user)

        return redirect('movies:index')
    return redirect('accounts:login')

def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        if " " in searched:
            if not searched:
                return redirect('movies:index')
            elif len(searched.split(" ")) >= 2:
                movies = Movie.objects.filter(description__contains=searched) | Movie.objects.filter(title__contains=searched)
                context = {'movies': movies}

                return render(request, 'movies/search.html', context)
        else:
            movies = Movie.objects.filter(description__contains=searched) | Movie.objects.filter(title__contains=searched)
            context = {'movies': movies}

            return render(request, 'movies/search.html', context)
    else:
        return redirect('movies:index')