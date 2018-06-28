import re
from django.forms import ModelForm
from .models import Task
from django import forms
from django.utils import timezone
from apps.opportunity.models import Opportunity
from apps.users.models import MyUser
from apps.client.models import CLIENT
from apps.project.models import IT_Project
from django.db.models import Q
from datetime import datetime

class CreateTaskForm(ModelForm):

    task_status = (
        ('start later', 'start later'),
        ('started', 'started'),
        ('completed', 'completed'),
        ('in progress', 'in progress'),
    )




    project = forms.ModelChoiceField(
        label='PROJECT NAME',
        # required=False,
        queryset=IT_Project.objects.all(),
        widget=forms.Select(),
    )

    # project = forms.CharField(
    #     widget=forms.TextInput(attrs={'readonly': True}), label='PROJECT NAME'
    # )

    task_name = forms.CharField(
        label = 'TASK NAME',

        widget=forms.TextInput(

        )
    )

    task_description = forms.CharField(
        label= 'TASK DESCRIPTION',
        required=False,
        widget=forms.Textarea()
    )

    employee_id = forms.ModelChoiceField(
        label='ASSIGN TO',
        # required=False,

        queryset=MyUser.objects.filter(Q(department='IT') & Q(designation='Employee')),
        widget=forms.Select(),
    )

    task_start_date_time = forms.DateField(
        label='TASK START DATE',
        required=False,
        widget=forms.TextInput(
            attrs={'type': 'date'}
        )
    )
    task_end_date_time = forms.DateField(
        label='TASK END DATE',
        required=False,
        widget=forms.TextInput(
            attrs={'type': 'date'}
        )
    )
    expected_time = forms.IntegerField(
        label='EXPECTED WORKING HOURS',
        widget=forms.TextInput()
    )

    status = forms.ChoiceField(
        label='STATUS',
        choices=task_status,
        widget=forms.Select()
    )

    class Meta:
        model = Task
        fields = (
            'project',
            'task_name',
            'task_description',
            'employee_id',
            'task_start_date_time',
            'task_end_date_time',
            'status',
            'expected_time',
        )



    # def clean_task_name(self):
    #     value = self.cleaned_data.get('task_name')
    #     if len(value) < 3:
    #         raise forms.ValidationError('Name too small')
    #     return value

    # def clean_opportunity(self):
    #     value = self.cleaned_data['opportunity']
    #     print(" ##############################  ",value.id)
    #     if self.instance.pk is not None:
    #         return value
    #     else:
    #         pass

    def clean_project_name(self):
        data = self.cleaned_data.get('project_name')
        if re.match('^\w*$', data):
        #if re.match(r'^[-a-zA-Z0-9_]+$',data):
            return data
        else:
            raise forms.ValidationError("Only alphabets and numbers are allowed")

    def clean_project_description(self):
        data = self.cleaned_data.get('project_description')
        if re.match('^\w*$', data):
        #if re.match(r'^[-a-zA-Z0-9_]+$',data):
            return data
        else:
            raise forms.ValidationError("Only alphabets and numbers are allowed")



    def clean_expected_time(self):
         data = self.cleaned_data.get('expected_time')
         data = str(data)
         if re.match(r'^[0-9_]+$', data):
             return data
         else:
             raise forms.ValidationError("Only Numbers are alllowed")

    def clean_project_total_working_hr(self):
         data = self.cleaned_data.get('project_total_working_hr')
         data = str(data)
         if re.match(r'^[0-9_]+$', data):
             return data
         else:
             raise forms.ValidationError("Only Numbers are alllowed")

