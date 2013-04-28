from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from tmster.engine.forms import StudentForm, SurveyForm
from tmster.engine.models import Survey, Opinion, Comment, Student

@login_required(login_url='/login/')
def student(request):
	if request.method == 'POST':
		form=StudentForm(request.POST)
		if form.is_valid():
			student=form.save()
			return HttpResponseRedirect("/")
	else:
		form=StudentForm()
	return render_to_response("addstudent.html", 
		{ 'form': form }, context_instance=RequestContext(request))


@login_required(login_url='/login/')
def survey(request, studentID):
	student = get_object_or_404(Student, pk=studentID)
	if request.method == 'POST':
		form = SurveyForm(request.POST)
		if form.is_valid():
			#Add comment to surver
			comment = Comment.objects.create(text=form.cleaned_data['comment'])
			#Create survey
			survey = Survey.objects.create(user=request.user, student=student, comment=comment)
			#Create opinions
			opinion1 = Opinion.objects.create(variant="1", value=form.cleaned_data['opinion1'])
			opinion2 = Opinion.objects.create(variant="2", value=form.cleaned_data['opinion2'])
			opinion3 = Opinion.objects.create(variant="3", value=form.cleaned_data['opinion3'])
			opinion4 = Opinion.objects.create(variant="4", value=form.cleaned_data['opinion4'])
			opinion5 = Opinion.objects.create(variant="5", value=form.cleaned_data['opinion5'])
			#Add opinions to survey
			survey.opinions.add(opinion1,opinion2,opinion3,opinion4,opinion5)

			#Save survey
			survey.save()
			return HttpResponseRedirect('/')
	else:
		form = SurveyForm()
	return render_to_response('survey.html', 
		{'form':form}, context_instance=RequestContext(request))




