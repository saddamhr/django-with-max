from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, response
from django.urls import reverse

monthly_challenges = {
    'january': 'Eat no meat for the entire month!',
    'february': 'Walk for at least 20 minutes every day!',
    'march': 'Learn Django for at least 20 minutes every day!',
    'april': 'april',
    'may': 'may',
    'june': 'june',
    'july': 'july',
    'august': 'august',
    'september': 'september',
    'october': 'october',
    'november': 'november',
    'december': 'december',
}

def index(request):
    list_items = ''
    months = list(monthly_challenges.keys())

    for month in months:
        captalized_month = month.capitalize()
        month_path = reverse('month-challenge', args=[month])
        list_items += f"<li><a href=\"{month_path}\">{captalized_month}</a></li>"
    
    response_data = f'<ul>{list_items}</ul>'

    return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound('Invalid month')

    redirect_month = months[month - 1]
    redirect_path = reverse('month-challenge', args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]

        return render(request, 'challenges/challenge.html', {
            'text': challenge_text
        })
    except:
        return HttpResponseNotFound('<h1>This month is not supported!</h1>')
        
