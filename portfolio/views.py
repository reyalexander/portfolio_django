from django.shortcuts import render
from django.views.generic import FormView, CreateView
from .models import *
from .forms import *
import datetime
# Create your views here.

def index(request):
    return render(request, 'portfolio.html')

def portfolio_create(request):
    portfolio = Portfolio.objects.all()
    form = PortfolioForm
    context = {'portfolio': portfolio, 'form': form}
    if request.method == 'POST':
        form = PortfolioForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            form.save()
        else:
            print('Error when you try to create a portfolio')
    
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    try:
        IpAddress.objects.get(ip_address=ip)
    except IpAddress.DoesNotExist:             #-----Here My Edit
        ip_address = IpAddress(ip_address=ip, pub_date=datetime.datetime.now())
        ip_address.save()

    return render(request, 'portfolio.html', context)


'''class RegisterView(CreateView):
  template_name = "register.html"
  form_class = NewUserForm

  def form_valid(self, form):
      form.save()
      return redirect('login')'''

'''class CreatePortfolio(CreateView):
    portf = get_object_or_404(Portfolio,)
    template_name = "test_forms/portfolio1.html"
    form_class = PortfolioForm
    print('Holaaaaa 111111')
    def form_valid(self, form):
        print('Holaaaaa')
        #portfolio = Portfolio.objects.create(form.cleaned_data)
        form.save()
        print('Creado exitosamente')
        return redirect('../portfolio')'''

'''
class CreatePortfolio(CreateView):
    template_name = "test_forms/portfolio1.html"
    form_class = PortfolioForm

    def __init__(self):
        super(PortfolioForm, self).__init__()

    def form_valid(self, form):
        form.save()
        print('hOLA MUNDOOOOO')
        return redirect('../portfolio')'''
      