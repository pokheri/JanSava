from django.db import models
from django.contrib.auth import get_user_model
from accounts.models import Profile
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation,GenericForeignKey
from django.db.models import Q



User = get_user_model()



class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    update_at  =models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True



class Region(models.Model):

    region_code = models.CharField(max_length=10,default='BBN')
    pin_code = models.CharField(max_length=12)
    location = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.region_code}'
    





class ComplaintCategory(models.TextChoices):

    ELECTRICITY  = 'Electricity'
    ROAD = 'Road'
    GARBAGE = 'Garbage'
    WATER = 'Water'
    POLUTION = 'Polution'
    OTHER  = 'Other'

class Image(models.Model):
    image = models.ImageField(upload_to='evidence/images/')   

class Video(models.Model):
    video = models.FileField(verbose_name='Video file ', upload_to='evidence/videos') 


class Evidence(TimeStampModel):
    
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type','object_id')

    # our fields 
    images = models.ManyToManyField(Image)
    videos = models.ManyToManyField(Video)
    


    def __str__(self):
        return f'Evidence {self.complaint.title}'
    




class Complaint( TimeStampModel):

    citizen = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='my_complaints',limit_choices_to={'profile__user_role': Profile.UserRole.CI},null=True)
    issue = models.CharField(max_length=12, choices=ComplaintCategory, default=ComplaintCategory.ROAD)
    title = models.CharField(max_length=200)
    description = models.TextField()
    vote = models.PositiveIntegerField(default=1)
    region = models.ForeignKey(Region,on_delete=models.CASCADE,related_name='complaints', null=True,blank=True)
    location  = models.TextField(null=True,blank=True)


    evidence = GenericRelation(Evidence)   



    class Meta:
        ordering = ['-created_at']
       

    def __str__(self):
        return f'complaint of {self.citizen}' 
    

class ComplaintUpdated(TimeStampModel):
    complaint = models.OneToOneField(Complaint, on_delete=models.CASCADE,related_name='complaint_resolve')
    desciption  = models.TextField()
    evidence = GenericRelation(Evidence)    
    
    feedbacks = GenericRelation('FeedBack')

    
    def __str__(self):
        return f'{self.complaint.created_at},complaint update '
    




class Event( TimeStampModel):

    # the admin will create this 
    title  = models.CharField(max_length=200)
    description = models.TextField()
    event_date = models.DateField()
    event_time_info = models.CharField(max_length=50)
    location  = models.CharField(max_length=200)
    banner = models.ImageField(upload_to='event/banner/')
    max_registration_limit = models.PositiveIntegerField(default=1000)
    is_active = models.BooleanField(default=True)

    feedbacks = GenericRelation('FeedBack')


    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return f'Event -->  {self.event_date}'
    

class EventRegistration(TimeStampModel):

    event = models.ForeignKey(Event, on_delete=models.CASCADE,related_name='registered_event')  
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    confirmed = models.BooleanField(default=True)



    def __str__(self):
        return f'{self.user.profile.id}, {self.event.event_date}'
    
class FeedBack( TimeStampModel):

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type','object_id')


    citizen = models.OneToOneField(User, on_delete=models.SET_NULL, related_name='feedbacks', null=True)
    message = models.TextField()

    def __str__(self):
        return f'{self.citizen.profile.name}'
    

class EventGallery(TimeStampModel):

    event = models.OneToOneField(Event,on_delete=models.CASCADE, related_name='gallery')
    images =models.ManyToManyField(Image)
    videos = models.ManyToManyField(Video)
    description = models.TextField(null=True,blank=True)

    def __str__(self):
        return f'{self.event.event_date}'
    



class Assignment( TimeStampModel):


    class AssignmentStatus(models.TextChoices):
        P = 'P','Pending'
        C = 'C','Completed'
        W = 'W','Working'

    complaint = models.OneToOneField(Complaint, on_delete=models.CASCADE)
    manager = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={
        'profile__user_role' : Profile.UserRole.MA
        })
    status = models.CharField(max_length=1, choices=AssignmentStatus, default=AssignmentStatus.P)



class PublicNotice(TimeStampModel):
    
    title = models.CharField(max_length=200)
    description =models.TextField()
    date = models.DateField()
    region = models.ForeignKey(Region, on_delete=models.CASCADE)


    def __str__(self):
        return f'Public Notice, {self.date} '