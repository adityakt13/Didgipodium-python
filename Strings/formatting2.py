movies = ['Dhol', 'Bahubali', 'Jab Tak Hai Jaan', 'PK']
stars = ['****' , '*****' , '*' , '*****']

for movie, star in zip(movies,stars):
    print(f'{movie:<16} | {star}')