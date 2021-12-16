print(r"""
              _,._      
  .||,       /_ _\\     
 \.`',/      |'L'| |    
 = ,. =      | -,| L    
 / || \    ,-'\"/,'`.   
   ||     ,'   `,,. `.  
   ,|____,' , ,;' \| |  
  (3|\    _/|/'   _| |  
   ||/,-''  | >-'' _,\\ 
   ||'      ==\ ,-'  ,' 
   ||       |  V \ ,|   
   ||       |    |` |   
   ||       |    |   \  
   ||       |    \    \ 
   ||       |     |    \
   ||       |      \_,-'
   ||       |___,,--")_\
   ||         |_|   ccc/
   ||        ccc/       
   ||                hjm
""")

q1 = input("Question 1?\n")

if q1.lower() == 'left':
    q2 = input("Question 2?\n")
    if q2.lower() == 'wait':
        q3 = input("Question 3?\n")
        if q3.lower() == 'yellow':
            print("You win!")
        else:
            print("Game Over")
    else:
        print("Game Over")
else:
    print("Game Over")