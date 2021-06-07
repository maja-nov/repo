from django.db import models
class Poll(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Question(models.Model):
    question_text = models.CharField(max_length=250)
    pub_date = models.DateTimeField(auto_now_add=True)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, null=True, blank=True, related_name="questions")

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers")
    answer_text = models.CharField(max_length=128)
    date_added = models.DateTimeField(auto_now_add=True)