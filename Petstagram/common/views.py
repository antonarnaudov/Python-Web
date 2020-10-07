from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render


# Create your views here.


def landing_page(request):
    return render(request, 'landing_page.html')


# class RegisterUserForm(forms.Form):
#     username = forms.CharField(label='Username')
#     first_name = forms.CharField(label='First Name')
#     surname = forms.CharField(label='Surname')
#     password = forms.CharField(label='Password')
#     email = forms.CharField(label='Email Address')
#
#     def save(self):
#         username = self.cleaned_data['username']
#         first_name = self.cleaned_data['first_name']
#         surname = self.cleaned_data['surname']
#         password = self.cleaned_data['password']
#         email = self.cleaned_data['email']
#
#         user = User(username=username, first_name=first_name, surname=surname, password=password, email=email)
#         user.save()
#
#
# class UserCreateView(View):
#     template_name = 'shared/register_form.html'
#
#     def get(self, request):
#         form = RegisterUserForm()
#         return render(request, self.template_name, {'form': form})
#
#     def post(self, request):
#         form = RegisterUserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/')
#
#

def register_form(request):
    form = UserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'shared/register_form.html', context)


def login_form(request):
    return render(request, 'shared/login_form.html')
