# Accounts
The accounts app contains the data of the user model.

The model contains the typical username, email, etc but additionally logs country of user, user status, and number of publications (used internally)


## Installation
This app is installed with the forking of the repo, there is not additional packages needed specifically for this app

## Usage

# controls tagging within html
{{ user.blank }}

# allows for implementation of urls in html
{% url 'user.blank' %}
{% url 'login' %}
{% url 'logout' %}
{% url 'signup' %}
{% url 'user_profile' %}