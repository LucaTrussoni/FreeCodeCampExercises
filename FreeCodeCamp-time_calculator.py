def ParseTime(timestring):
  elements=timestring.split(sep=":")
  Hours=int(elements[0])
  Mins=int(elements[1])
  return [Hours,Mins]

def add_time(start, duration, weekday=None):
  try:
    # Let's parse the input
    elements=start.split(sep=" ")
    ampm_remainder=0
    nextdays=0
    wkday_to_n={'monday':0,'tuesday':1,'wednesday':2,'thursday':3,
      'friday':4,'saturday':5,'sunday':6}
    AMPM={0:'AM',1:'PM'}
    n_to_wkday={0:'Monday',1:'Tuesday',2:'Wednesday',3:'Thursday',
      4:'Friday',5:'Saturday',6:'Sunday'}
    if len(elements)==2:
      if elements[1]=="AM":
        ampm_remainder=0
      elif elements[1]=="PM":
        ampm_remainder=1
      else:
        raise ValueError("Illegal format AMPM in start")
      StartHour=ParseTime(elements[0])
      DeltaHour=ParseTime(duration)
      EndTime=[0,0]
      EndTime[0]=StartHour[0]+DeltaHour[0]
      EndTime[1]=StartHour[1]+DeltaHour[1]
      # I prefer to reason with 24h hours
      EndTime[0]=EndTime[0]+12*ampm_remainder
      if EndTime[1]>=60:
        MinuteRemainder=EndTime[1]%60
        EndTime[0]=int(EndTime[0]+(EndTime[1]-MinuteRemainder)/60)
        EndTime[1]=MinuteRemainder
      if EndTime[0]>=24:
        DayRemainder=EndTime[0]%24
        nextdays=int((EndTime[0]-DayRemainder)/24)
        EndTime[0]=DayRemainder
      # let's get back to 12hours
      # we will use again ampm_remainder since it has no further
      # use and is human readable
      # Let us made some adjustments to have a human readable hour
      if EndTime[0]>12:
        ampm_remainder=1
        EndTime[0]=EndTime[0]-12
      elif EndTime[0]==12:
        # at 12:30 PM we will have the remainder to primt PM, but will not adjust the hour
        ampm_remainder=1
      else:
        ampm_remainder=0
      # Now 00:30 AM will be a legal hour, we need to transform it in 12:30 AM
      if EndTime[0]==0 and ampm_remainder==0:
        EndTime[0]=12
      # Now we have the arrival hour in EndTime[0]:EndTime[1] format
      # with AM/PM in ampm_remainder and number of days forward in
      # nextdays
      OutString=str(EndTime[0])+":"+format(EndTime[1],"02d")+" "+AMPM[ampm_remainder]
      if weekday!=None:
        targetweekday=wkday_to_n[weekday.lower()]
        targetweekday+=nextdays
        targetweekday=targetweekday%7
        OutString=OutString+", "+n_to_wkday[targetweekday]
      if nextdays>0:
        if nextdays==1:
          OutString=OutString+" (next day)"
        else:
          OutString=OutString+" ("+str(nextdays)+" days later)"
    new_time=OutString
  except ValueError as myErr:
    new_time=str(myErr)
  return new_time
