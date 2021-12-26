from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from base.models import Task
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


class CustomLoginView(LoginView):
    """Вход пользователя в систему"""
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        """Переход в случаи успешного входа"""
        return reverse_lazy('tasks')


class RegisterPageView(FormView):
    """Регистрация в системе"""
    template_name = 'base/register.html'
    #  форма которая будет использоваться при регистрации
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        user = form.save()
        #  если пользователь зарегистрировался то автовход в систему
        if user is not None:
            login(self.request, user)
        return super(RegisterPageView, self).form_valid(form)

    def get(self, *args, **kwargs):
        #  реализация запрета заходить авторизованому пользователю на страницу регистрации
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegisterPageView, self).get(*args, **kwargs)


class TaskList(LoginRequiredMixin, ListView):
    """Список задач"""
    model = Task
    template_name = 'base/tasks_list.html'
    context_object_name = 'tasks'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        #  фильтруем задачи только для конктретного пользователя
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()
        #  получаем запрос от формы поиска
        search_input = self.request.GET.get('search-area') or ''
        #  если поиск осуществляется
        if search_input:
            #  фильтруем по вхождунию поискового запроса в наши заголовки задач
            context['tasks'] = context['tasks'].filter(title__icontains=search_input)
        context['search_input'] = search_input
        return context


class TaskDetail(LoginRequiredMixin, DetailView):
    """Детали задачи"""
    model = Task
    template_name = 'base/task.html'
    context_object_name = 'task'


class TaskCreate(LoginRequiredMixin, CreateView):
    """Создание новой задачи"""
    model = Task
    template_name = 'base/task_create.html'
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    """Обновление ифнормации о задачи"""
    model = Task
    template_name = 'base/task_create.html'
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')


class TaskDelete(LoginRequiredMixin, DeleteView):
    """Удаление задачи"""
    model = Task
    template_name = 'base/task_delete.html'
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
