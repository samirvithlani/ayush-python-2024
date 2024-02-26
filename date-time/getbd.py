from datetime import datetime
age = 29

date = datetime(datetime.now().year - age, 1, 1)
print(date)


data = {"ayush":"1995-2-14","amit":"2000-5-19","raj":"1998-3-15","suresh":"1997-4-12","mukesh":"1993-6-11"}

oldest_user = None
oldest_birthdate = None

for user, birthdate in data.items():
    birthdate_obj = datetime.strptime(birthdate, "%Y-%m-%d")
    print(birthdate_obj)
    if oldest_birthdate is None or birthdate_obj < oldest_birthdate:
        oldest_user = user
        oldest_birthdate = birthdate_obj

print("The oldest user is:", oldest_user)