import pyttsx3
engine = pyttsx3.init()


x='0'
y='0'

type= input("Choose your type * for times and / for devide and + for add and - for subtract")

y = int(input("pick number 1"))
x = int(input ("Pick number 2"))


if type == '*':
    ta = (y * x)
    engine.say(str(ta))
    engine.runAndWait()
    print(ta)
else:
    if type == '+':
     pa = y + x
     engine.say(str(pa))
     engine.runAndWait()
     print(pa)
    else:
       if type == '/' :
          da = y / x
          engine.say(str(da))
          engine.runAndWait()
          print(da)
       else:
          if type == '-':
             ma = y - x
             engine.say(str(ma))
             engine.runAndWait()
             print(ma)