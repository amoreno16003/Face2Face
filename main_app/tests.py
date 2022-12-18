from django.test import TestCase

# Create your tests here.
# @method_decorator(login_required, name='dispatch')
# def send(request, self):
#     message = request.POST['message']
#     # username = request.POST['username']
#     room_id = request.POST['room_id']

#     sender = request.user
    
#     new_message = Message.objects.create(value=message, sender=sender, room=room_id)
#     new_message.save()
#     return HttpResponse('Message sent successfully')

# <!-- <script type="text/javascript" src="{% static 'assets/AgoraRTC_N-4.8.0.js' %}"></script> -->
# <!-- </html>
# {% extends 'base.html' %}
# {% load static %}
# <head>
#   <link rel='stylesheet' type='text/css' href="{% static '/styles/createChatroom.css' %}">
# </head>
# {% block content %}

# <div class='form'> 
#   <form id="post-form" method="POST" action="">
#       {% csrf_token %}
#       <label>Create a Chatroom or Join an Existing Chatroom</label>
#       {% comment %}Need to display existing chatrooms to choose from {% endcomment %}
#       <input type="text" name="chatroom" id="chatroom" width="100px" />
#       <input type="submit" value="Entering the Room">
#   </form>
# </div>

# <div class="login-box">
#   <form>
#     <div class="user-box">
#       <input type="text" name="" required="">
#       <label>Username</label>
#     </div>
#     <div class="user-box">
#       <input type="password" name="" required="">
#       <label>Password</label>
#     </div>
#     <a href="#">
#       <span></span>
#       <span></span>
#       <span></span>
#       <span></span>
#       Submit
#     </a>
#   </form>
# </div>

# {% endblock %} -->