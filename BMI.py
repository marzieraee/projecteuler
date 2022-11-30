n = int(input())
m = float(input())
BMI = float(n/(m**2))
if BMI < 18.5 :
    print('%.2f\nUnderweight'%BMI)
elif 18.5<=BMI<25 :
    print('%.2f\nNormal'%BMI)
elif 25<=BMI<30 :
    print('%.2f\nOverweight'%BMI)
elif 30<=BMI :
    print('%.2f\nObese'%BMI)
    
