from .is_latin import islatin
from data.qurandict import qurandict
from data.qurandict2 import qurandict2
#from quranuz import quran
from fuzzywuzzy import fuzz
from .transliterate import to_cyrillic, to_latin


async def search2(sura, matn, accuracy=70, trans=0):
# def search2(sura, matn, accuracy=70):
    quran = {}
    if not trans:
        quran = qurandict
    else:
        quran = qurandict2
    text = await to_cyrillic(matn)
    res = {}
    for oyat in quran[str(sura)]:
        
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