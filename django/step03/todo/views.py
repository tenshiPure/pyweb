from django.shortcuts import redirect
from django.views.generic import CreateView
from todo.models import *

class TaskCreateView(CreateView):
	template_name = "task/form.html"
	model = Task
	success_url = '/story'
	fields = ('body', 'end', 'status',)

	def form_valid(self, form):
		fk = self.kwargs.get('fk')
		story = Story.objects.get(pk = fk)
		self.object = form.save(commit = False)
		self.object.storyId = story
		self.object.save()

		return redirect(self.success_url)

	def get_context_data(self, **kwargs):
		context = super(TaskCreateView, self).get_context_data(**kwargs)

		context['story_id'] = 1

		return context
