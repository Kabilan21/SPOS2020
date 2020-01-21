code =["START 101","READ N","MOVER BREG ONE","MOVEM BREG TERM","AGAIN MULT BREG TERM","MOVER CREG TERM","ADD CREG ONE","MOVEM CREG TERM","COMP CREG N","BC LE AGAIN","MOVEM BREG RESULT","PRINT RESULT","STOP","N DS 1","RESULT DS 1","ONE DC 1","TERM DS 1","END"]

opcode = [("START","AD","01"),("ADD","IS","01"),("SUB","IS","02"),("MULT","IS","03"),("MOVER","IS","04"),("MOVEM","IS","05"),("COMP","IS","06"),("STOP","IS","00"),("BC","IS","07"),("DIV","IS","08"),("READ","IS","09"),("PRINT","IS","10"),("END","AD","02"),("LTORG","AD","03"),("EQU","AD","04"),("ORIGIN","AD","05"),("DS","DL","02"),("DC","DL","01"),("LE","CS","02")]

relate = [("LT","1"),("LE","2"),("EQ","3"),("GT","4"),("GE","5"),("ANY","6")]

register= [("AREG","1"),("BREG","2"),("CREG","3"),("DREG","4")]

symtab = []

lc = 0

this_entry = 0 

def rel_check(word):
    for reg,num in relate:
        if reg == word:
            return num

def symtab_append(word):
    set = True
    for sym,_,_ in symtab:
        if sym == word:
            set = False
    if set == True:        
        symtab.append((word,None,None))

def enternet(word):
    i = 1
    for sym,_,_ in symtab:
        if sym == word:
            break
        else:
            i = i+1
    return i
def register_check(word):
    for reg,num in register:
        if reg == word:
            return num

cont = 1

for coding in code:
    for word,state,number in opcode:
        if coding.split()[0]== word:
            if word == 'START':
                line = f"({state},{number})(c,{coding.split()[1]})"
                lc = int(coding.split()[1])
                print(line)
            if word == 'READ': 
                symtab_append(coding.split()[1])
                lc = lc + 1
                this_entry = 1
                line = f"({state},{number})(0)(s,{this_entry})"
                print(line)
            if word == 'MOVER':
                lc = lc + 1
                symtab_append(coding.split()[2])
                line = f"({state},{number})({register_check(coding.split()[1])})(s,{enternet(coding.split()[2])})"
                print(line)
            if word == 'MOVEM':
                lc = lc + 1
                symtab_append(coding.split()[2])
                line = f"({state},{number})({register_check(coding.split()[1])})(s,{enternet(coding.split()[2])})" 
                print(line)               
            if word == 'MULT':
                lc = lc + 1
                symtab_append(coding.split()[2])
                line = f"({state},{number})({register_check(coding.split()[1])})(s,{enternet(coding.split()[2])})" 
                print(line) 
            if word == 'ADD':
                lc = lc + 1
                symtab_append(coding.split()[2])
                line = f"({state},{number})({register_check(coding.split()[1])})(s,{enternet(coding.split()[2])})" 
                print(line)
            if word == 'COMP':
                lc = lc + 1
                symtab_append(coding.split()[2])
                line = f"({state},{number})({register_check(coding.split()[1])})(s,{enternet(coding.split()[2])})" 
                print(line)
            if word == 'BC':
                lc = lc + 1
                line = f"({state},{number})({rel_check(coding.split()[1])})(s,{enternet(coding.split()[2])})" 
                print(line)    
            if word == 'PRINT':
                lc = lc + 1
                line = f"({state},{number})(0)(s,{enternet(coding.split()[1])})" 
                print(line) 
            if word == 'STOP':
                lc = lc + 1
                line = f"({state},{number})" 
                print(line)
                
                
    if coding.split()[0] == 'AGAIN':
        symtab.append((coding.split()[0],lc,1))
        for word1,state1,number1 in opcode:
            if coding.split()[1] == word1:
                if word1 == 'MULT':
                    lc = lc + 1
                    symtab_append(coding.split()[3])
                    line = f"({state1},{number1})({register_check(coding.split()[2])})(s,{enternet(coding.split()[3])})" 
                    print(line)
     
    for sym, address , length in symtab:
        if coding.split()[0] == sym:
            for word2,state2,number2 in opcode:
                if coding.split()[1] == word2:
                    if coding.split()[1] == 'DS':
                        lc = lc + 1
                        line = f"({state2},{number2})(c,{coding.split()[2]})" 
                        print(line)
                    if coding.split()[1] == 'DC':
                        lc = lc + 1
                        line = f"({state2},{number2})(c,{coding.split()[2]})" 
                        print(line)
                        
            





    
    cont = cont +1
    if cont == 11:
        pass   
print(symtab,lc)                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
        

