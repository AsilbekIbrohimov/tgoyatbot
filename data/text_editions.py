"""Oyat MATNI uchun tarjima/transliteratsiya variantlari.

'local.*' — botdagi mahalliy o'zbekcha ma'lumot (tez, oflayn, qidiruvda ishlaydi).
Qolganlari — AlQuran Cloud API'dan olinadigan edition'lar.
"""

DEFAULT_TEXT_ED = "local.sodiq"

# (identifier, ko'rsatiladigan nom)
TEXT_EDITIONS = [
    ('local.sodiq', 'Shayx Muhammad Sodiq (uz) 🇺🇿'),
    ('local.mansur', 'Alovuddin Mansur (uz) 🇺🇿'),
    ('en.sahih', 'Saheeh International [en]'),
    ('en.transliteration', 'Transliteration — lotin oʻqilishi [en]'),
    ('en.pickthall', 'Pickthall [en]'),
    ('ru.kuliev', 'Кулиев [ru]'),
    ('tr.diyanet', 'Diyanet [tr]'),
    ('ur.jalandhry', 'Jalandhry [ur]'),
    ('fa.ghomshei', 'Ghomshei [fa]'),
    ('fr.hamidullah', 'Hamidullah [fr]'),
    ('de.aburida', 'Abu Rida [de]'),
    ('id.indonesian', 'Indonesian [id]'),
]

# Mahalliy edition -> eski `trans` (0/1) moslamasi (qidiruv shunga tayanadi)
LOCAL_TRANS = {'local.sodiq': 0, 'local.mansur': 1}

LABEL_TO_ID = {label: ident for ident, label in TEXT_EDITIONS}
ID_TO_LABEL = {ident: label for ident, label in TEXT_EDITIONS}
