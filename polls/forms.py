from django.forms import CharField, Form, DateTimeField, ModelChoiceField, ModelForm
from django.core.exceptions import ValidationError
from polls.models import Poll, Question

from datetime import datetime
import pytz


class PastDateField(DateTimeField):
    utc = pytz.UTC
    def validate(self, value):
        super().validate(value)
        if value >= datetime.today().replace(tzinfo=self.utc):
            raise ValidationError("Only past dates allowed here")

class NameForm(Form):
    name = CharField(max_length=128)
    birth_date = DateTimeField()

class PollForm(Form):
    name = CharField(max_length=128)

def capitalized_validator(value):
    if value[0].islower():
        raise ValidationError("Value must be capitalized.")

class QuestionForm(Form):
    question_text = CharField(max_length=128, validators=[capitalized_validator], label="Pytanie:")
    poll = ModelChoiceField(queryset=Poll.objects.all())
    pub_date = PastDateField(label="Publication Date")

    def clean_question_text(self):
        initial = self.cleaned_data["question_text"]
        return initial.replace(" ","*")

    def clean(self):
        result = super().clean()
        if result['question_text'][0] == "A" and result['pub_date'].year < 2000:
            self.add_error('question_text', "Can't start with A")
            self.add_error('pub_date', "Add year after 1999")
            raise ValidationError("Dont put")
        return result

class AnswerForm(Form):
    answer_text = CharField(max_length=128)
    question = ModelChoiceField(queryset=Question.objects.all())

class QuestionModelForm(ModelForm):
    class Meta:
        model = Question
        fields = "__all__"