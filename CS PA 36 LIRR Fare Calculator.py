#Name:  ...Lowai Dobie...
#Email:  ...lowai.dobie76@myhunter.cuny.edu...
#Date: October 28, 2020
#This program prints: LIRR Fare Calculator 
def computeFare(zone, tickettype):
    
    if zone==1 and tickettype=="peak":
        fare=8.75
    elif zone==1 and tickettype=="off-peak":
        fare=6.25
    elif (zone==2 or zone==3) and tickettype=="peak":
        fare=10.25
    elif (zone==2 or zone==3) and tickettype=="off-peak":
        fare=7.50
    elif zone==4 and tickettype=="peak":
        fare=12.00
    elif zone==4 and tickettype=="off-peak":
        fare=8.75
    elif (zone==5 or zone==6 or zone==7) and tickettype=="peak":
        fare=13.50
    elif (zone==5 or zone==6 or zone==7) and tickettype=="off-peak":
        fare=9.75
    else:
        fare= -1
    return(fare) 
    

def main():
    z=int(input("Enter the number of zones: "))
    t=input("Enter the ticket type (peak/off-peak): ").lower()
    fare = computeFare(z, t)
    print('The fare is', fare)

if __name__ == "__main__":
    main()
