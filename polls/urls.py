from django.urls import path
from polls.views import hello
from polls.views import animals
from polls.views import my_template
from polls.views import polls, questions, answers, index
from polls.views import PollView, QuestionView, AnswerView
from polls.views import PollTemplateView, QuestionTemplateView, AnswerTemplateView
from polls.views import PollListView, QuestionListView, AnswerListView
from polls.views import get_name, poll_form, question_form, answer_form
from polls.views import QuestionFormView, PollFormMethodView, QuestionCreateView


app_name = "polls"
urlpatterns = [
    path("my-question-create-viev/", QuestionCreateView.as_view(), name = "my-question-create-viev" )
    path("my-poll-form-method-view/", PollFormMethodView.as_view(), name ="my-poll-form-method-view"),
    path("my-question-form-view/", QuestionFormView.as_view(), name = "my-question-form-view"),
    path("my-name-form/", get_name),
    path("my-poll-form/", poll_form),
    path('my-question-form/', question_form),
    path('my-answer-form/', answer_form),

    path('hello/<str:s0>/', hello),
    path("animals/", animals),
    path('my_template/<str:s0>/', my_template),
    path('polls/', polls, name="polls"),
    path('questions/', questions, name="questions"),
    path('answers/', answers, name="answers"),
    path('', index, name="index"),
    path('polls-class/', PollView.as_view(), name="polls-class"),
    path('questions-class/', QuestionView.as_view(), name="answers-class"),
    path('answers-class/', AnswerView.as_view(), name="questions-class"),

    path("polls-temp/", PollTemplateView.as_view(), name="polls-temp"),
    path("questions-temp/", QuestionTemplateView.as_view(), name="questions-temp"),
    path("answers-temp/", AnswerTemplateView.as_view(), name="answers-temp"),
    path("polls-list/", PollListView.as_view(), name="polls-temp"),
    path("questions-list/", QuestionListView.as_view(), name="questions-temp"),
    path("answers-list/", AnswerListView.as_view(), name="answers-temp"),
]