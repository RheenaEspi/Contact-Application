from django.shortcuts import render, redirect

def index(request):
  session_user_id = request.session.get('session_user_id')
  if session_user_id:
    return render(request, 'pages/index.html')
  else:
    return redirect('login')
