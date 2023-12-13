# destination_darling
# Welcome to Destination Darling! 
## The travel app for all your planning needs. 

Version 3.4.0

# Accounts
The accounts app contains the data of the user model.

The model contains the typical username, email, etc but additionally logs country of user, user status, and number of publications (used internally)

# Destinations
These destinations are an app built to hold posts and editting/deleting
in order to make the web app more user friendly
and readable

# Attractions
These attractions are an app built to be nested within 
destinations in order to make the web app more user friendly
and readable

# Pages
These pages are a small app that holds our Home Page, About Page, and Our Find Out More Page

## Installation
Use the package manager [pip] to install .venv, django=4.2.0, black, django-crispy-froms==2.0, crispy-bootstrap5==0.7, gunicorn==20.1.0, environs[django]==9.5.0, psycopg[binary]==3.1.8, whitenoise==6.4.0, and Pillow

## Usage

# controls tagging within html
{{ accounts.blank }}
{{ pages.blank }}
{{ destinations.blank }}
{{ attractions.blank }}

# allows for implementation of urls in html
{% url 'login' %}
{% url 'logout' %}
{% url 'signup' %}
{% url 'user_profile' %}
{% url 'index' %}
{% url 'about' %}
{% url 'destinations.blank %}
{% url 'attractions.blank' %}

# gets specific destination's path to attraction
{{ attraction.get_url }}

# url specifics
/attractions/ is blank, in order to visit a specific destionation's attraction list you will need to tag the url as 
"{{ attraction.get_url }}/attractions/"
thise will lead you to destinations/somehwere,someplace/attractions

destinations.pk will direct you to a specific destination within your destinations list. this is primarily for url functionality.


