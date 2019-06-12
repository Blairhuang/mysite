from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.models import User 
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin #载入Mixin 给class增加功能

posts = [
    {
        'author' : 'Blair',
        'title' : 'Blog post 1', #,勿忘
        'content' : 'First post content',
        'date_posted' : '2019/6/7'
    },
    {
        'author' : 'Blair',
        'title' : 'Blog post 2',
        'content' : 'Second post content',
        'date_posted':'2019/6/8'
    }
]

def home(request):
    context = {
        'posts': Post.objects.all() #创造一个context key->posts value->posts Pass info into template
    }
    return render(request,'blog/home.html',context)
    # ADDING VALUE//原有的:HttpResponse('<doctype>...') ##DOCTYPE ...表明会有更多的内容
    # render 即从templates 底下的blog 里面提取home.html
    # 说明展现三个内容 request, home.html, context 

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' #指明template的名字 但是因为def home 定义的key 为posts, 所以要更改name = posts  <app>/<model>_<viewtype>.html
    context_object_name = 'posts' #let the class know the new context , 因为default postlistview context=object 所以设定objectname为context
    ordering = ['-date_posted'] #将posts按照时间顺序更改
    paginate_by = 2 #分页 2页 paginator已经在cmd 里面install

class UserPostListView(ListView): 
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 2

    def get_query_set(self): 
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted') #不用get_query_set 的话默认是Post.objects.all(),
        #此条件用于当作者等于user 时， 不等于则返回404 page, 并且按照时间顺序排序


class PostDetailView(DetailView): #显示每个单独的post的detail view 
    model = Post

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView): #表现了基本顺序 登陆，通过用户证明，删除成功
    model = Post
    success_url = '/' #即意味着Postdelete成功以后直接转入home page (URL)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title', 'content']
    
    def form_valid(self,form): #create author//self, form as arguments
        form.instance.author = self.request.user #take the instance and set the author 即设置更新的作者为登陆的用户 self.request.user
        return super().form_valid(form)  #RUNNING the form //setting the author before run 


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title','content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object() #先获取post

        if self.request.user == post.author: #检车用户是否是作者，如果是的话才有资格update post
            return True
        else:
            return False



def about(request):
    return render(request,'blog/about.html',{'title':'About'})



#DJANGO provide shortcuts: 即直接render

# Create your views here.
# blog-> templates -> blog -> template.html 基本路径
