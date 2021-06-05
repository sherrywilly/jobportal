from django.db import models
from django.contrib.auth.models import User


class RecruterExtra(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=40)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.user.first_name

    @property
    def get_id(self):
        return self.user.id

    @property
    def get_name(self):
        return self.user.first_name + " " + self.user.last_name


EDUCATION = [('bca', 'BCA'), ('B-TECH', 'BTECH'), ('MCA', 'MCA'), ('M-TECH', 'M-TECH'),
             ('EEE', 'EEE'), ('COMPUTER_SCIENCE',
                              'COMPUTER_SCIENCE'), ('BBA', 'BBA'), ('BCOM', 'B-COM')
             ]


class StudentExtra(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    university = models.CharField(max_length=300, null=True)
    image = models.ImageField(upload_to='user_image',
                              null=True, default='default.jpg')
    college = models.CharField(max_length=300, null=True)
    education = models.CharField(choices=EDUCATION, max_length=100, null=True)
    college_aggregate = models.IntegerField(null=True)
    college_year_of_passing = models.IntegerField(null=True)

    school = models.CharField(max_length=300, null=True)
    school_aggregate = models.IntegerField(null=True)
    school_year_of_passing = models.IntegerField(null=True)

    hsc = models.CharField(max_length=300, null=True)
    hsc_aggregate = models.IntegerField(null=True)
    hsc_year_of_passing = models.IntegerField(null=True)

    mobile = models.CharField(max_length=40, null=True)
    status = models.BooleanField(default=False)

    @property
    def get_name(self):
        return self.user.first_name + " " + self.user.last_name

    @property
    def get_id(self):
        return self.user.id

    def __str__(self):
        return self.user.first_name


class Job(models.Model):
    recruter = models.ForeignKey(
        RecruterExtra, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=400, null=True)
    salary = models.IntegerField()
    education = models.CharField(max_length=200)
    email = models.EmailField()
    description = models.TextField()

    def __str__(self):
        return str(self.title)


class JobRequest(models.Model):
    Job = models.ForeignKey(Job, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)


class FAQ(models.Model):
    question = models.CharField(max_length=300, null=True)
    answer = models.CharField(max_length=400, null=True)

    def __str__(self):
        return str(self.question)
