from django.db import models
from django.utils import timezone


# Create your models here.

class feedback(models.Model):
    feedback_value = (
        ('Very poor', u'Very poor'),
        ('Poor', u'Poor'),
        ('Average', u'Average'),
        ('Good', u'Good'),
        ('Excellent', u'Excellent')
    )
    branch_name = [
        ('CS', u'CS'),
        ('EC', u'EC'),
        ('IT', u'IT'),
        ('CE', u'CE'),
        ('ME', u'ME'),
        ('EN', u'EN'),
    ]
    your_name = models.CharField(max_length=70)
    your_email = models.EmailField()
    about_college = models.TextField()
    your_branch = models.CharField(max_length=20, choices=branch_name)
    faculty_name = models.CharField(max_length=50)
    subj_teacher = models.CharField(max_length=50)
    teaching_skill = models.CharField(max_length=10, choices=feedback_value)
    class_feedback = models.CharField(max_length=10, choices=feedback_value)
    after_class_feedback = models.CharField(max_length=10, choices=feedback_value)
    faculty_behaviour = models.CharField(max_length=10, choices=feedback_value)
    knowledge_about_subj = models.CharField(max_length=10, choices=feedback_value)
    Doubt_clearing = models.CharField(max_length=10, choices=feedback_value)
    your_suggestion = models.TextField()
    feedback_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.your_name
