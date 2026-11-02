from django.urls import path
from api import views

urlspatterns=[
    path('about/',views.About.as_view(),name='About'),
    path('education/',views.Education.as_view(),name="Education"),
    path('project/',views.Project.as_view(),name="Project"),
    path('skill/',views.skill.as_view(),name="skill"),
    path('certification/',views.certification.as_view(),name='certification')
]