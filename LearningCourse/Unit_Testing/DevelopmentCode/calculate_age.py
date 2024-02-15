from datetime import date

def get_age(date_of_birth):
    today = date.today()
    age = today.year - date_of_birth.year
    if today.year < date_of_birth.year or (today.month == date_of_birth.month and today.day < date_of_birth.day):
        age = 0
        raise ValueError("Birth year is in the future")
    elif date_of_birth.year < 0:
        raise ValueError("Birth year is negative")  
    elif date_of_birth.year <= 1000:
        raise ValueError("Birth year is in the distant past")  
    return age

# Call the get_age function with a date of birth
#date_of_birth = date(1991, 5, 15)
#age = get_age(date_of_birth)
#print(age)
