# Beatriz is developing a customer service system for a service website.
# She wants to create a program that displays a personalized greeting depending on the time of day the user accesses the platform.
# The system must follow this rule:

# If it is before 12 PM, display "Good morning";

# Between 12 PM and 6 PM, display "Good afternoon";

# After 6 PM, display "Good evening".

def personalized_greeting(hour):
    if hour < 12:
        return 'Good morning'
    elif hour < 18:
        return 'Good afternoon'
    else:
        return 'Good evening'
    
user_name = input('Enter your name: ')
current_hour = int(input('Enter the current time (0-23): '))
print(f'{personalized_greeting(current_hour)}, {user_name}!')