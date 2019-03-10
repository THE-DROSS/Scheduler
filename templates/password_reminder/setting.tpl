{% extends "password_reminder/base" %}

{% block title %}Setting{% endblock %}

{% block content %}

{% if error_message %}<p><strong>{{ error_message }}</strong></p>{% endif %}

<form action="./{{ onetime_url_param }}" method="post">
{{ csrf_input }}
    新しいパスワードを入力してください。<br>
    (8文字以上, 英語の大文字、英語の小文字、数字、記号のうち3種以上を利用する。)<br>
    {{ form.new_password }}</input><br>
    {{ form.new_password_confirmed }}<br>
    <input type="submit"value="送信" />
</form>
{% endblock %}