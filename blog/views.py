from django.shortcuts import render
from .models import Post, Category, Tag
from django.views.generic import ListView, DetailView
from django.db.models import Q


class PostList(ListView):
    model = Post

    #작성일 역순으로 정렬
    def get_queryset(self):
        return Post.objects.order_by('-created')

    # 이미 코드가 정해져 있음
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        context['post_without_category'] = Post.objects.filter(category=None).count()

        return context


# 검색
class PostSearch(PostList):
    def get_queryset(self):
        q = self.kwargs['q']
        object_list = Post.objects.filter(Q(title__contains=q) | Q(content__contains=q))
        return object_list

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostSearch, self).get_context_data()
        context['search_info'] = 'Search Result >> {}'.format(self.kwargs['q'])
        return context


class PostDetail(DetailView):
    model = Post

    # 이미 코드가 정해져 있음
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        context['post_without_category'] = Post.objects.filter(category=None).count()

        return context


class PostListByTag(PostList):
        model = Post

        def get_queryset(self):
            tag_slug = self.kwargs['slug']
            tag = Tag.objects.get(slug=tag_slug)

            return tag.post_set.order_by('-created')


class PostListByCategory(PostList):
    def get_queryset(self):
        slug = self.kwargs['slug']

        if slug == '_none':
            category = None
        else:
            category = Category.objects.get(slug=slug)

        print(slug)

        return Post.objects.filter(category=category).order_by('-created')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostListByCategory, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        context['post_without_category'] = Post.objects.filter(category=None).count()

        slug = self.kwargs['slug']

        if slug == '_none':
            context['category'] = '미분류'
        else:
            category = Category.objects.get(slug=slug)
            context['category'] = category

        # context['title'] = 'Blog - {}'.format(category.name)
        # context['category'] = category

        return context



# def post_detail(request, pk):
#     blog_post = Post.objects.get(pk=pk)
#     context = {
#         'blog_post': blog_post,
#     }
#
#     return render(request, 'blog/post_detail.html', context)


# Create your views here.
# def index(request):
#     posts = Post.objects.all()
#     context = {'posts': posts,}
#     return render(request, 'blog/index.html', context)













