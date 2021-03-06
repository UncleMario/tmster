import urllib

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.utils import simplejson

from tmster.engine.forms import StudentForm, SurveyForm
from tmster.engine.models import Survey, Opinion, Comment, Student

def search(request):
	q = urllib.unquote(request.GET.get('q',''))
	q = q.strip()
	if q != '':
		results = Student.objects.filter(name__icontains= q)
		total = results.count()
	return render_to_response('results.html', 
		{'results':results, 'total':total, 'student' : q}, context_instance=RequestContext(request))


def view_student(request, studentID):
	student = get_object_or_404(Student, pk=studentID)
	grades = Survey.objects.filter(student=student)
	return render_to_response('view_student.html', 
		{'student':student, 'grades':grades}, context_instance=RequestContext(request))

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
	from tmster.engine.functions import update_calification

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

			#update user calification
			update_calification(survey.student, survey.get_grade())

			return HttpResponseRedirect('/student/%s' % (survey.student.pk))
	else:
		form = SurveyForm()
	return render_to_response('survey.html', 
		{'form':form}, context_instance=RequestContext(request))

def autocomp(request):
	q = request.GET.get('term', '')
	students = Student.objects.filter(name__icontains = q )[:10]
	results = []
	for s in students:
		s_json = {}
		s_json['id'] = s.id
		s_json['label'] = s.name
		s_json['value'] = s.name
		results.append(s_json)
	data = simplejson.dumps(results)
	mimetype = 'application/json'
	return HttpResponse(data, mimetype)


