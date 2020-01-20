code =["START 101","READ N","MOVER BREG ONE","MOVEM BREG TERM","AGAIN MULT BREG TERM","MOVER CREG TERM","ADD CREG ONE","MOVEM CREG TERM","COMP CREG N","BC LE AGAIN","MOVEM BREG RESULT","PRINT RESULT","STOP","N DS 1","RESULT DS 1","ONE DC 1","TERM DS 1","END"]

opcode = [("START","AD",1),("ADD","IS","01"),("SUB","IS","02"),("MULT","IS","03"),("MOVER","IS","04"),("MOVEM","IS","05"),("COMP","IS","06"),("STOP","IS","00"),("BC","IS","07"),("DIV","IS","08"),("READ","IS","09"),("PRINT","IS","10"),("END","AD","02"),("LTORG","AD","03"),("EQU","AD","04"),("ORIGIN","AD","05"),("DS","DL","02"),("DC","DL","01"),("LE","CS","02"))]

def change(coding):
    for word,state,number in opcode:
        if coding.split()[0]== word:
            line = f"({state},{number})(c,{coding.split()[1]})"
            print(line)  
           
change(code[0])    

