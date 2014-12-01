from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

# from .models import Post



context_base = {
    # 'categories': Category.objects.all(),
}



# Show homepage
def index(request):
    context = context_base
    # posts = Post.objects.all()[:5]
    # context['posts'] = posts
    return render(request, 'attendance/index.html', context)
