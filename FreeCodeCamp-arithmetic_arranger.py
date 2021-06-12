# First task: create a function to properly format simple operations
# and manage possible errors in input

def arithmetic_arranger(problems,Results=False):
  try:
    if len(problems)>5:
      raise ValueError("Error: Too many problems.")
    #Let's start with problems.
    #All problems are arranged in four lines
    FirstAddendum=[]
    SecondAddendum=[]
    Operators=[]
    for myproblem in problems:
      elements=myproblem.split(sep=" ")
      # not requested but useful
      if len(elements)!=3:
        raise ValueError("I'm confused: operation "+myproblem+"not well formatted.")
      # detect operator and raise error if not legal
      if elements[1]=="+" or elements[1]=="-":
        Operators.append(elements[1])
      else:
        raise ValueError("Error: Operator must be '+' or '-'.")
      # now let's look at addenda
      try:
        FirstAddendum.append(int(elements[0]))
        SecondAddendum.append(int(elements[2]))
      except ValueError:
        raise ValueError("Error: Numbers must only contain digits.")
      # The addenda are now loaded, let's look at number of digits
      if FirstAddendum[-1]>9999 or FirstAddendum[-1]<-999 or SecondAddendum[-1]>9999 or SecondAddendum[-1]<-999:
        raise ValueError("Error: Numbers cannot be more than four digits.")
      # if we're here everything is ok and we can proceed with the next problem
    # Now we start convertion
    # PlaceHolders
    FirstLine=[None]*len(Operators)
    SecondLine=[None]*len(Operators)
    ThirdLine=[None]*len(Operators)
    FourthLine=[None]*len(Operators)
    for i in range(len(Operators)):
      op_width=max(len(str(FirstAddendum[i])),len(str(SecondAddendum[i])))+2
      FirstLine[i]=str(FirstAddendum[i]).rjust(op_width)
      SecondLine[i]=str(SecondAddendum[i]).rjust(op_width-2)
      SecondLine[i]=Operators[i]+" "+SecondLine[i]
      ThirdLine[i]="-"*op_width
      if Results==True:
        aux=0
        if  Operators[i]=="+":
          aux=FirstAddendum[i]+SecondAddendum[i]
        else:
          aux=FirstAddendum[i]-SecondAddendum[i]
        FourthLine[i]=str(aux).rjust(op_width)
    # We now have all our elements
    line1=""
    line2=""
    line3=""
    line4=""
    for i in range(len(FirstLine)):
      pad=""
      if (i>0):
        pad=" "*4
      line1=line1+pad+FirstLine[i]
      line2=line2+pad+SecondLine[i]
      line3=line3+pad+ThirdLine[i]
      if Results==True:
        line4=line4+pad+FourthLine[i]
    arranged_problems=line1+"\n"+line2+"\n"+line3
    if Results==True:
      arranged_problems+=("\n"+line4)
  except ValueError as my_err:
    arranged_problems=str(my_err)
  return arranged_problems