from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView, FormView, CreateView

from polls.models import Poll, Question, Answer
from polls.forms import NameForm, PollForm, AnswerForm, QuestionForm, ModelForm
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy


def hello(request, s0):
    s1 = request.GET.get('s1', '')
    return render(
        request,
        template_name="hello.html",
        context={"adjectives":[s0, s1, "beautiful", "wonderful"]}
    )

def my_template(request, s0):
    s1 = request.GET.get('s1', '')
    return render(
        request,
        template_name="my_template.html",
        context={"animals":[s0, s1, "lion", "wolf"]}
    )

def animals(request):
    animals = request.GET.get("animals", "")
    return render(
        request,
        template_name="mytemp2.html",
        context={"animals": animals.split(",")}
    )

def polls(request):
    return render(
        request,
        template_name="polls.html",
        context={"polls": Poll.objects.all() }
    )

def questions(request):
    return render(
        request,
        template_name="questions.html",
        context={"questions": Question.objects.all() }
    )

def answers(request):
    return render(
        request,
        template_name="answers.html",
        context={"answers": Question.objects.all() }
    )

def index(request):
    return render(
        request,
        template_name="index.html"
    )

class PollView(View):
    def get(self, request):
        return render(
            request,
            template_name="polls.html",
            context={"polls": Poll.objects.all()}
        )

class QuestionView(View):
    def get(self, request):
        return render(
            request,
            template_name="questions.html",
            context={"questions": Question.objects.all()}
        )

class AnswerView(View):
    def get(self, request):
        return render(
            request,
            template_name="answers.html",
            context={"answers": Answer.objects.all()}

        )


class PollTemplateView(TemplateView):
    template_name = "polls.html"
    extra_context = {"polls": Poll.objects.all()}

class QuestionTemplateView(TemplateView):
    template_name = "questions.html"
    extra_context = {"questions": Question.objects.all()}

class AnswerTemplateView(TemplateView):
    template_name = "answers.html"
    extra_context = {"answers": Answer.objects.all()}


class PollListView(ListView):
    template_name = "polls.html"
    model = Poll

class QuestionListView(ListView):
    template_name = "questions.html"
    model = Question

class AnswerListView(ListView):
    template_name = "answers.html"
    model = Answer

def get_name(request):
    form = NameForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            return HttpResponse("IT WORKED")
    return render(request, "form.html", {'form': form})

def poll_form(request):
    form = PollForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data["name"]
        Poll.objects.create(name=name)
        return HttpResponse("IT WORKED")
    return render(request, "form.html", {'form': form})

def question_form(request):
    form = QuestionForm(request.POST or None)
    if form.is_valid():
        question_text = form.cleaned_data["question_text"]
        poll = form.cleaned_data["poll"]
        Question.objects.create(question_text=question_text, poll=poll)
        return HttpResponse("IT WORKED!")
    return render(
        request,
        template_name="form.html",
        context={"form": form}
    )

def answer_form(request):
    form = AnswerForm(request.POST or None)
    if form.is_valid():
        answer_text = form.cleaned_data["answer_text"]
        question = form.cleaned_data["question"]
        Answer.objects.create(answer_text=answer_text, question=question)
        return HttpResponse("IT WORKED!")
    return render(
        request,
        template_name="form.html",
        context={"form": form}
    )

class QuestionFormView(FormView):
    template_name = "form.html"
    form_class = QuestionForm
    succes_url = reverse_lazy("polls:index")

    def form_valid(self, form):
        result = super().form_valid()
        question_text = form.cleaned_data["question_text"]
        poll = form.cleaned_data["poll"]
        Question.objects.create(question_text=question_text, poll=poll)
        return result

    def form_invalid(self, form):
        return super().form_invalid()

class PollFormMethodView(View):
    def get(self, request):
        form = PollForm()
        return render(
            request,
            template_name="form.html",
            context={"form": form}
        )
    def post(self, request):
        form = PollForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            Poll.objects.create(name=name)
            return HttpResponseRedirect(reverse("polls:index"))
        return render(
            request,
            template_name="form.html",
            context={"form": form}
        )




class QuestionCreateView(CreateView):
    model = Question
    fields = "__all__"