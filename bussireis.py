import os

os.system('cls')

def getArrival():
    arrival = input("Sisesta saabumisaeg (xx:xx): ")

    try:
        arrivalHour = int(arrival[:2])
        arrivalMinute = int(arrival[3:])

        if (len(arrival[2:-2]) != 1 or arrival[2:-2] != ":" or arrivalHour > 23 or arrivalHour < 0 or arrivalMinute > 59 or arrivalMinute < 0): 
            print("Sisend kellaeg on valesti vormistatud1")

            arrival = getArrival()

            return arrival

        return [arrivalHour, arrivalMinute]
        

    except ValueError:
        print("Sisend kellaaeg on valesti vormistatud2")

        arrival = getArrival()

    return arrival

def getLeaving():
    leaving = input("Sisesta väljumisaeg (xx:xx)")

    try:
        leavingHour = int(leaving[:2])
        leavingMinute = int(leaving[3:])

        if (len(leaving[2:-2]) != 1 or leaving[2:-2] != ":" or leavingHour > 23 or leavingHour < 0 or leavingMinute > 59 or leavingMinute < 0): 
            print("Sisend kellaeg on valesti vormistatud1")

            leaving = getleaving()

            return leaving

        return [leavingHour, leavingMinute]
        

    except ValueError:
        print("Sisend kellaaeg on valesti vormistatud2")

        leaving = getleaving()

    return leaving

def duration(arrival, leaving):
    hours = arrival[0] - leaving[0]

    print(hours)

arrival = getArrival()
leaving = getLeaving()


