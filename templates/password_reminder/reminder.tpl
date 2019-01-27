{% extends "password_reminder/base" %}

{% block title %}Reminder{% endblock %}

{% block content %}

{% if error_message %}<p><strong>{{ error_message }}</strong></p>{% endif %}

<form action="." method="post">
{{ csrf_input }}
    {{form.email}}
    <input type="submit"value="送信" />
</form>
{% endblock %}