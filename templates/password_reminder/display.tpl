{% extends "password_reminder/base" %}

{% block title %}Display{% endblock %}

{% block content %}
{{ form.email }}に送信しました。
メールに記載されているアドレスにアクセスし、パスワードを入力してください。
パスワード：{{ form.password }}
{% endblock %}