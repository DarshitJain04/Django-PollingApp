from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from .forms import *
from django.forms import modelformset_factory
from django.urls import reverse

def index(request):
	questions = Question.objects.all().order_by('-pub_date')
	context = {'questions':questions
	}
	return render(request,'polls/home.html',context)




def create(request):
	#inlineformset can also be used
	choiceformset = modelformset_factory(Choice, form=ChoiceCreationForm, fields=('option',), extra=3)
	if request.method == 'POST':
		q_form = QuestionCreationForm(data=request.POST)
		c_form = choiceformset(request.POST, request.FILES)
		if q_form.is_valid() and c_form.is_valid():
			question = q_form.save()
			forms = c_form.save(commit=False)
			for form in forms:
				form.question = question
				form.save()
			return redirect('/')

	else:
		q_form = QuestionCreationForm()
		c_form = choiceformset(queryset=Choice.objects.none(),)

	context = {'q_form': q_form, 'c_form': c_form

	}
	return render(request,'polls/create.html',context)



def vote(request, question_id ):
	question = get_object_or_404(Question,pk=question_id)
	options = question.choice_set.all() #or choices = Choice.objects.filter(question=question)
	if request.method == 'POST':
		selected_option =  question.choice_set.get(pk=request.POST['options'])
		selected_option.votes = selected_option.votes +1
		selected_option.save()
		return reverse('result', kwargs={'pk':question_id})
	context = {'options':options, 'question':question
	}
	return render(request,'polls/vote.html',context)


def result(request, question_id):
	question = get_object_or_404(Question,pk=question_id)
	options = question.choice_set.all()
	context = {'options':options, 'question':question
	}
	return render(request,'polls/result.html',context)
