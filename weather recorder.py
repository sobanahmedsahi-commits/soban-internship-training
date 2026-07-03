ttemp=0
maximum=-99999999
minimum=999999999
for i in range(1,365):
    todays_temperature=float(input("enter todays temperature: "))
    todays_humidity=float(input("enter todays humidity level"))
    ttemp+=todays_temperature
    thumidity+=todays_humidity
    if todays_temperature> maximum:
        maximum=todays_temperature
        print(f"maximum temperature for the year: {maximum}")
    elif todays_temperature<minimum:
        minimum=todays_temperature
        print(f"minimum temperature for the year: ",{minimum})
    
avgtemp= ttemp/ 365
avghumidity=thumidity/365
print(f"average temperature of the year",avgtemp)
print(f"average humidity of the year: ",avghumidity)
