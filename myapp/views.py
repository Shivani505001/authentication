from django.contrib.auth.hashers import make_password, check_password
from .models import User
from django.shortcuts import render, redirect
from django.contrib.auth import logout

def base(request):
    return render ( request , 'home.html' )

def register (request):
    if request.method == 'POST':
        name=request.POST['name']
        roll_number=request.POST['roll_number']
        password = request.POST['password']
        phone_number = request.POST['phone_number']
        
        if not (any(char.isupper() for char in password) and any(char.isdigit() for char in password)):
            return render(request, 'register.html', {'error': 'Password must contain at least one uppercase letter and one digit.'})
        
        # Hash the password before saving it to the database
        hashed_password = make_password(password)
        
        user = User(name=name, roll_number=roll_number, password=hashed_password, phone_number=phone_number)
        user.save()
        return redirect('home')
    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        roll_number = request.POST['roll_number']
        password = request.POST['password']

        try:
            user = User.objects.get(roll_number=roll_number)
        
        # Check if the provided password matches the stored hashed password
            if check_password(password, user.password):
                # Successful login
                return render(request, 'success.html', {'user': user})  
            else:
                # Invalid password
                return render(request, 'login.html', {'error': 'Invalid password'})
        except User.DoesNotExist:
            # User does not exist
            return render(request, 'login.html', {'error': 'User does not exist'})
        

    return render(request, 'login.html')
        


def logout_view(request):
    logout(request)
    return redirect('home')  # Redirect to the home page or any other desired page