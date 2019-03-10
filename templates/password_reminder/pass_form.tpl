{% extends "password_reminder/base" %}

{% block title %}PassForm{% endblock %}

{% block content %}

{% if error_message %}<p><strong>{{ error_message }}</strong></p>{% endif %}

<form action="./{{ onetime_url_param }}" method="post">
{{ csrf_input }}
    パスワードを入力してください。<br>
    {{form.password}}
    <input type="submit"value="送信" />
</form>
{% endblock %}