from django.contrib.auth import logout, get_user_model, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.sites.models import Site
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponseNotFound, HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views import View
from django.views.generic import ListView, CreateView, FormView
from django.contrib import messages
from .forms import *
from .token import account_activation_token
from .utils import *
from django.contrib.auth.models import User


def start(request):
    context = {'title': title,
               'possibility': possibility}
    return render(request, 'base/index.html', context=context)


class AddFile(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddFileForm
    template_name = 'base/addfile.html'
    success_url = reverse_lazy('file')
    login_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(**kwargs)
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        form.save()
        return super(AddFile, self).form_valid(form)


class ContactFormView(DataMixin, FormView):
    form_class = ContactForm
    template_name = 'base/info.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(**kwargs)
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home')


class RegisterUser(DataMixin, CreateView):
    form_class = RegistrationForm
    template_name = 'base/registration.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(**kwargs)
        return dict(list(context.items()) + list(c_def.items()))

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            current_site = get_current_site(request)
            subject = 'Подтверждение регистрации. AvdBASE'
            message = render_to_string('base/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            messages.add_message(self.request, messages.INFO, 'Откройте сообщение на почте')
            messages.success(request, 'Пожалуйста перейдите по этой ссылке для подтверждения регистрации.')

            return redirect('login')

        return render(request, self.template_name, {'form': form})


class ActivateAccount(View):

    def get(self, request, uidb64, token, *args, **kwargs):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.profile.email_confirmed = True
            user.save()
            login(request, user)
            messages.success(request, 'Вы подтвердили свой аккаунт. Спасибо')
            return redirect('user_page')
        else:
            messages.warning(request, 'Ошибка. Такой пользователь уже существует')
            return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginForm
    template_name = 'base/login.html'
    success_url = reverse_lazy('user_page')


def logout_user(request):
    logout(request)
    return redirect('home')


@login_required
def user_page(request):
    context = {'title': title,
               'possibility': possibility}
    return render(request, 'base/user_page.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


class FileListView(LoginRequiredMixin, DataMixin, ListView):
    model = File
    success_url = reverse_lazy('file')
    login_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(**kwargs)
        return dict(list(context.items()) + list(c_def.items()))
