from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import School, Category, Region
from django.db.models import Q


def index(request):
    return render(request, 'blog/index.html', {})


def contact(request):
    return render(request, 'blog/contact.html', {})


def about(request):
    return render(request, 'blog/about.html', {})


def team(request):
    return render(request, 'blog/team.html', {})


def school_list(request):
    cat = request.GET.get('cat', '')
    reg = request.GET.get('reg', '')
    txt = request.GET.get('txt', '')
    categories = Category.objects.all()
    regions = Region.objects.all()
    try:
        cat= int(cat)
    except:
        cat = False

    if cat is False:
        if txt == '':
            if reg == '':
                schools = School.objects.filter(published_date__lte=timezone.now()).order_by('school_name')
            else:
                schools = School.objects.filter(published_date__lte=timezone.now()).filter(region=reg).order_by(
                    'school_name')
        else:
            schools = School.objects.filter(Q(text__contains=txt) | Q(school_name__contains=txt) | Q(owner__contains=txt)).order_by('school_name')
    else:
        schools = School.objects.filter(published_date__lte=timezone.now()).filter(category=cat).order_by('school_name')
    return render(request, 'blog/school_list.html', {'schools': schools, 'categories': categories, 'regions': regions})



def school_detail(request, pk):
    school = get_object_or_404(School, pk=pk)
    return render(request, 'blog/school_detail.html', {'school': school})
# Create your views here.
