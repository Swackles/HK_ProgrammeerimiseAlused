import os

os.system('cls')

def getArrival():
    arrival = input("Sisesta saabumisaeg (xx:xx): ")

    try:
        arrivalHour = int(arrival[:2])
        arrivalMinute = int(arrival[3:])

        if (len(arrival[2:-2]) != 1 or arrival[2:-2] != ":" or arrivalHour > 23 or arrivalHour < 0 or arrivalMinute > 59 or arrivalMinute < 0): 
            print("Sisend kellaeg on valesti vormistatud")

            arrival = getArrival()

            return arrival

        return [arrivalHour, arrivalMinute]
        

    except ValueError:
        print("Sisend kellaaeg on valesti vormistatud")

        arrival = getArrival()

        return arrival

def getLeaving():
    leaving = input("Sisesta väljumisaeg (xx:xx): ")

    try:
        leavingHour = int(leaving[:2])
        leavingMinute = int(leaving[3:])

        if (len(leaving[2:-2]) != 1 or leaving[2:-2] != ":" or leavingHour > 23 or leavingHour < 0 or leavingMinute > 59 or leavingMinute < 0): 
            print("Sisend kellaeg on valesti vormistatud")

            leaving = getLeaving()

            return leaving

        return [leavingHour, leavingMinute]
        

    except ValueError:
        print("Sisend kellaaeg on valesti vormistatud")

        leaving = getLeaving()

        return leaving

    return percent

arrival = getArrival()
leaving = getLeaving()

hours = arrival[0] - leaving[0]
minutes = arrival[1] - leaving[1]

if hours < 0:
    hours = (24 - leaving[0]) + arrival[0]

if minutes < 0:
    minutes =(60 - leaving[1]) + arrival[1]

durationMinutes = hours * 60 + minutes
durationHours = round(hours + (((minutes * 100) / 60 ) / 100), 2)

print(durationMinutes)

print("""
    Väljub: {}
    Saabub: {}
""".format(str(leaving[0]) + ":" + str(leaving[1]), str(arrival[0]) + ":" + str(arrival[1])))
print("""   {} minutit või {} tundi""".format(durationMinutes, durationHours))


