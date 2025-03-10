from django.shortcuts import render, redirect
from . import views
from django.urls import path
from . views import JobHomeView, JobDetailsView, AddJobPostView, EditJobPostView, DeleteJobPostView, AddJobCategoryView, JobDraftPostDetailsView, JobDraftsListView, AddJobDraftPostView, EditJobDraftPostView, DeleteJobDraftPostView
from  django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage



app_name = 'jobs'

urlpatterns = [
    path('job/', JobHomeView.as_view(), name="job_list"),
    path('job/<int:pk>/', JobDetailsView.as_view(), name='job_details'),


    path('add_job_post/', AddJobPostView.as_view(), name='add_job_post'),
    path('job/edit/<int:pk>', EditJobPostView.as_view(), name='edit_job_post' ),
    path('job/<int:pk>/delete', DeleteJobPostView.as_view(), name='delete_job_post' ),
    
    path('add_job_category/', AddJobCategoryView.as_view(), name='add_job_category'),       
    path('job_category/<str:category_name>/', views.JobCategoryView, name='job_category_list'), 
    path('view_job_category/', views.ListJobCategory, name='view_job_category'), 

    path('<int:pk>/add_job_comment/', views.add_job_comment, name='add_job_comment'),


    path('job_drafts/', JobDraftsListView.as_view(), name='job_drafts_list'),
    path('add_job_draft_post/', AddJobDraftPostView.as_view(), name='add_job_draft_post'),
    path('job_draft_details/<int:pk>/', JobDraftPostDetailsView.as_view(), name='job_draft_details'),
    path('job_draft/edit/<int:pk>', EditJobDraftPostView.as_view(), name='edit_job_draft_post' ),
    path('job_draft/<int:pk>/delete', DeleteJobDraftPostView.as_view(), name='delete_job_draft_post' ),
    path('publish/<int:job_draft_pk>/', views.publish_job_draft, name='publish_job_draft'),
]