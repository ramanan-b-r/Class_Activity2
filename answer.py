def find_cube_pairs(target):#first of all no colon here
    solutions = [] #unneccsary semicolon
    max_num = round(target ** (1/3))  #for power it is ** not ***
    #its target not targ

    for a in range(1, max_num + 1):#its range not ranges and no semilcolon
        for b in range(a, max_num + 1):#its range not ranges and no semilcolon
            if a**3 + b**3 == target: #for power it is ** not *** and no semicolon
                #its target not targ
                solutions.append((a, b)); #solutions should be used not sol
    return solutions #reuturn solutions not sol

pairs = find_cube_pairs(1729) 
#removing the comma as it makes pairs a tuple containing a list


print("Valid cube pairs for 1729:") #its print not printf
#its 1729 not 1728
#again removing unncesary comma

for a, b in pairs: # no semicolon and its pairs not pair
    print(f" → {a}³ + {b}³ = {a**3} + {b**3} = 1729") #its print not printf
    #its 1729 not 1728
