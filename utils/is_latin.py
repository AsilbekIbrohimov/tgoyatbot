from string import punctuation

async def islatin(text, part: int = 50):
    #ru = ""
#    
#    for i in range(1024, 1329):
#        ru+=chr(i)
        
    punc = punctuation
    
    uz =""
    
    for i in range(593):
        uz+=chr(i)
        
    for i in punc:
        uz.replace(i, "")
    matn = ""
    for i in text:
        if i not in punc:
            matn+=i
    latin = 0 
    others = 0
    
    for harf in matn:
        if harf in uz:
            latin += 1
        else:
            others += 1
    
    if not latin:
        return False
    elif latin == others:

        
        if matn[0] in uz:
            return True
        else:
            return False
    
    elif latin/len(matn)*100>part:
        return True
    
    else:
        return False
        


#def is_arabic(text):
#    ar = ""
#    
#    for i in range(1530, 1793):
#        ru+=chr(i)