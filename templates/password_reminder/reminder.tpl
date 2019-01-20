{% extends "password_reminder/base" %}

{% block title %}Reminder{% endblock %}

{% block content %}

{% if error_message %}<p><strong>{{ error_message }}</strong></p>{% endif %}

<form action="./display/" method="post">
{{ csrf_input }}
    <input type="text" name="email">
    <input type="submit"value="送信">
</form>
{% endblock %}