from .is_latin import islatin
from .quranlist import quranlist
from .quranlist2 import quranlist2
#from quranuz import quranlist
from fuzzywuzzy import fuzz
from .transliterate import to_cyrillic, to_latin


async def search(matn, accuracy=80, trans = 0):
    quran = {}
    if not trans:
        quran = quranlist
    else:
        quran = quranlist2
    
    text = await to_cyrillic(matn)
    res = {}
    for oyat in quran:
        
        if fuzz.partial_ratio(oyat["text"].lower(), text.lower())>=accuracy:
            res[f"{oyat['text']} [{oyat['chapter']}:{oyat['verse']}]"] = fuzz.partial_ratio(text.lower(), oyat["text"].lower())
    
    res =  sorted(res.items(), key=lambda item: item[1], reverse = True)
    answer = []
    tartib = 1
    if await islatin(matn):
        for i in res:
            answer.append(f"{tartib}.\n{await to_latin(i[0])}")
            tartib += 1
    else:
            for i in res:
                answer.append(f"{tartib}.\n{i[0]}")
                tartib += 1
    if answer:
        return answer
    
    elif await islatin(matn):
        return ["qidiruv natijasi mavjud emas"]
    else:
        return ['қидирув натижаси мавжуд эмас']
        
# for k in search("alomatlar bor", 80):
#     print(k, end = "\n\n")


async def make(arr, length=4000) -> list:
    res = []
    answer = ''
    for i in arr:
        
        if len(answer+i)<length:
            answer += i + '\n\n'
        else:
            res.append(answer)
            answer = i + '\n\n'
    if answer:
        res.append(answer)
    return res