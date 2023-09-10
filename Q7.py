fahrenhite = -100 
  
 while fahrenhite < 100: 
     celcius = (fahrenhite - 32) * 5/9 
     if int(celcius) == fahrenhite and celcius - int(celcius) == 0: 
         break 
     fahrenhite += 1 
  
 if fahrenhite < 100: 
     print("At ",fahrenhite ,"the scales are equal") 
 else: 
     print("No same temperature found.")
