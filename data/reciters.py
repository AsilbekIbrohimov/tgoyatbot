"""AlQuran Cloud API dagi oyat-oyat audio qiroatlar (identifier -> nom)."""

DEFAULT_RECITER = "ar.alafasy"

RECITERS = [
    ('ar.abdullahbasfar', 'Abdullah Basfar'),
    ('ar.abdurrahmaansudais', 'Abdurrahmaan As-Sudais'),
    ('ar.abdulsamad', 'Abdul Samad'),
    ('ar.shaatree', 'Abu Bakr Ash-Shaatree'),
    ('ar.ahmedajamy', 'Ahmed ibn Ali al-Ajamy'),
    ('ar.alafasy', 'Alafasy'),
    ('ar.hanirifai', 'Hani Rifai'),
    ('ar.husary', 'Husary'),
    ('ar.husarymujawwad', 'Husary (Mujawwad)'),
    ('ar.hudhaify', 'Hudhaify'),
    ('ar.ibrahimakhbar', 'Ibrahim Akhdar'),
    ('ar.mahermuaiqly', 'Maher Al Muaiqly'),
    ('ar.muhammadayyoub', 'Muhammad Ayyoub'),
    ('ar.muhammadjibreel', 'Muhammad Jibreel'),
    ('ar.saoodshuraym', 'Saood bin Ibraaheem Ash-Shuraym'),
    ('en.walk', 'Ibrahim Walk [en]'),
    ('ar.parhizgar', 'Parhizgar'),
    ('ur.khan', 'Shamshad Ali Khan [ur]'),
    ('zh.chinese', 'Chinese [zh]'),
    ('fr.leclerc', 'Youssouf Leclerc [fr]'),
    ('ar.aymanswoaid', 'Ayman Sowaid'),
    ('ru.kuliev-audio', 'Elmir Kuliev by 1MuslimApp [ru]'),
    ('ru.kuliev-audio-2', 'Elmir Kuliev 2 by 1MuslimApp (2) [ru]'),
    ('kk.khalifahaltai-audio', 'Kazakh Translation Audio by Khalifah Altai [kk]'),
    ('ar.alafasy-2', 'Alafasy (2)'),
    ('ar.husary-2', 'Husary (2)'),
    ('ar.mahermuaiqly-2', 'Maher Al Muaiqly (2)'),
    ('ar.hudhaify-2', 'Hudhaify (2)'),
    ('ar.husarymujawwad-2', 'Husary (Mujawwad) (2)'),
    ('ar.muhammadayyoub-2', 'Muhammad Ayyoub (2)'),
    ('ar.muhammadjibreel-2', 'Muhammad Jibreel (2)'),
    ('uz.sodik-audio', 'Muhammad Sodik Muhammad Yusuf  [uz]'),
]

LABEL_TO_ID = {label: ident for ident, label in RECITERS}
ID_TO_LABEL = {ident: label for ident, label in RECITERS}
