# Create your views here.
from django.shortcuts import get_object_or_404,render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect,Http404
from django.core.urlresolvers import reverse
from Todo.todolist.models import Poll,Choice
from django.template import RequestContext,loader
from django.views.decorators.csrf import csrf_protect


def index(request):
    latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = RequestContext(request,{
               'latest_poll_list':latest_poll_list,})
    return HttpResponse(template.render(context))

def detail(request,poll_id):
    try:
        p = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExist:
        raise Http404
    return render_to_response('polls/detail.html',{'poll':p},context_instance=RequestContext(request))

def results(request,poll_id):
    p = get_object_or_404(Poll,pk=poll_id)
    return render_to_response('polls/results.html',{'poll':p},context_instance=RequestContext(request))

@csrf_protect
def vote(request,poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render_to_response('polls/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        },context_instance=RequestContext(request))
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('Todo.todolist.views.results', args=(p.id,)))
