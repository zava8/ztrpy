import re
# ɦ(small_0266) (U+0144 ń) (U+03B1 α)
# (U+03C4 τ) (U+0442 small_т) (U+0503 small_ԃ)
# ɧ(small_0267) (U+00A2 ¢) (U+0256 ɖ) (U+0257 ɗ) (ć)
table_adhnt_itou = str.maketrans('ADHNT', 'αԃɦńт')
table_adhnt_utoi = str.maketrans('αԃɦńт', 'ADHNT')
table_jqv_zkw = str.maketrans('jqv','zkw')

ADHNT_u = str.maketrans('ADHNT', 'αԃɦńт') # ć
u_ADHNT = str.maketrans('αԃɦńтć', 'ADHNTc')
qvj_kwz = str.maketrans('jqv','zkw')
t1 = "aNgur Trbuz ThAli anAr aAm DuuDh DHi"
t2=t1.translate(ADHNT_u)
print(f"t1 is {t1}\nt2 is {t2}")

# https://stackoverflow.com/questions/20742076/replace-uppercase-with-lowercase-letters
def kh_K(i):
    i = re.sub(r'([])h', r'\1H', i, re.I)
    i = re.sub(r'([^kgcjztdpbswKGCJZTDPBSW])h', r'\1H', i, re.I)

def phonetic_h(i):
    i = re.sub('H','h', i)
    i = re.sub(r'(\s)h', r'\1H', i, re.I)
    i = re.sub(r'([^kgcjztdpbswKGCJZTDPBSW])h', r'\1H', i, re.I)
def phonetic_n(i):
    i = re.sub(r'N', 'n', i)
    i = re.sub(r'n([cgk])\b', r'ṅ\1', i, flags=re.I)
    i = re.sub(r'\bn', 'ñ', i, flags=re.I)
    i = re.sub(r'([a-z])nk', r'\1ṅk', i, flags=re.I)
    i = re.sub(r'oung', 'ouṅg', i, flags=re.I)
    i = re.sub(r'ginge', 'giñge', i, flags=re.I)
    i = re.sub(r'([ht])inge', r'\1iñge', i, flags=re.I)
    i = re.sub(r'([fyc])ring', r'\1riñg', i, flags=re.I)
    i = re.sub(r'engin', 'eñgin', i, flags=re.I)
    i = re.sub(r'ngth', 'ñgth', i, flags=re.I)
    i = re.sub(r'ange([^dr])', r'añge\1', i, flags=re.I)
    i = re.sub(r'\bt([ai])ng([ei])', r't\1ñg\2', i, flags=re.I)
    i = re.sub(r'\bangi', 'añgi', i, flags=re.I)
    i = re.sub(r'inge', 'iñge', i, flags=re.I)
    i = re.sub(r'ing', 'iṅg', i, flags=re.I)
    i = re.sub(r'nge\b', 'ñge', i, flags=re.I)
    i = re.sub(r'ngel', 'ñgel', i, flags=re.I)
    i = re.sub(r'([dr])ang([ei])', r'\1añg\2', i, flags=re.I)
    i = re.sub(r'([lv])eng', r'\1eñg', i, flags=re.I)
    i = re.sub(r'chang([ei])', r'chañg\1', i, flags=re.I)
    i = re.sub(r'sseng', 'sseñg', i, flags=re.I)
    i = re.sub(r'nger', 'ṅger', i, flags=re.I)
    i = re.sub(r'([a-z])ng', r'\1ṅg', i, flags=re.I)
    i = re.sub(r'sync', 'syṅc', i, flags=re.I)
    i = re.sub(r'anchor', 'aṅchor', i, flags=re.I)
    i = re.sub(r'linco', 'liṅco', i, flags=re.I)
    i = re.sub(r'sincl', 'siṅcl', i, flags=re.I)
    i = re.sub(r'\buncle(s?)\b', r'uṅcle\1', i, flags=re.I)
    i = re.sub(r'menco', 'meṅco', i, flags=re.I)
    i = re.sub(r'([iu])nct', r'\1ṅct', i, flags=re.I)
    i = re.sub(r'nc([hyei])', r'ñc\1', i, flags=re.I)
    i = re.sub(r'inc([^hueioay])', r'iṅc\1', i, flags=re.I)
    i = re.sub(r'inc([aeiou])', r'iñc\1', i, flags=re.I)
    i = re.sub(r'([a-z])unc([^hyei])', r'\1uṅc\2', i, flags=re.I)
    i = re.sub(r'enc([^eiyh])', r'eñc\1', i, flags=re.I)
    i = re.sub(r'([ao])nc([^hyei])', r'\1ṅc\2', i, flags=re.I)
    i = re.sub(r'ṅ', 'N', i)
    i = re.sub(r'ñ', 'n', i)
def phonetic_a(i):
    i = re.sub(r'A', 'a', i)
    i = re.sub(r'aft', 'αft', i, flags=re.I)
    i = re.sub(r'aw([kf\s])', r'αw\1', i, flags=re.I)
    i = re.sub(r'\bar([cekmst])\b', r'αr\1', i, flags=re.I)
    i = re.sub(r'guar', 'guαr', i, flags=re.I)
    i = re.sub(r'ijab', 'ijαb', i, flags=re.I)
    i = re.sub(r'ebab', 'ebαb', i, flags=re.I)
    i = re.sub(r'ihad', 'iHαԃ', i, flags=re.I)
    i = re.sub(r'ia([ck])', r'iα\1', i, flags=re.I)
    i = re.sub(r'\ba', 'à', i, flags=re.I)
    i = re.sub(r'ai\b', 'αi', i)
    i = re.sub(r'uar([bce-su-z])', r'uàr\1', i, flags=re.I)
    i = re.sub(r'([a-z])a\b', r'\1α', i, flags=re.I)
    i = re.sub(r'a([w])\b', r'α\1', i, flags=re.I)
    i = re.sub(r'\ba([ntsmd])\b', r'à\1', i, flags=re.I)
    i = re.sub(r'ar([aiey])', r'àr\1', i, flags=re.I)
    i = re.sub(r'([^uheio\s])arre([^lasn])', r'\1αrre\2', i, flags=re.I)
    i = re.sub(r'([eio\s])ar', r'\1àr', i, flags=re.I)
    i = re.sub(r'i([lgn])ar([^y])', r'i\1αr\2', i, flags=re.I)
    i = re.sub(r'([^beiuohlgn])ar([^y])', r'\1αr\2', i, flags=re.I)
    i = re.sub(r'bar([^oiuer])', r'bαr\1', i, flags=re.I)
    i = re.sub(r'era([\b\s])', r'erα\1', i, flags=re.I)
    i = re.sub(r'([bcdfह\b\s])all([^yo])', r'\1αll\2', i, flags=re.I)
    i = re.sub(r'ava', 'αvα', i, flags=re.I)
    i = re.sub(r'([^\b\soe])ard', r'\1αrd', i, flags=re.I)
    i = re.sub(r'([ag])raph', r'\1rαph', i, flags=re.I)
    i = re.sub(r'las([skmt])', r'lαs\1', i, flags=re.I)
def e_to_i(i):
    i=phonetic_h(i)
    i=phonetic_n(i)
    i=phonetic_a(i)
    i = i.replace('H', 'ɦ').replace('N', 'ń').replace('à', 'a')
    i = i.lower().replace('th','тh')

def Etoi_A(i):
    i = i.replace('A', 'α')
def Etoi_H(i):
    i = i.replace('H', 'ɦ')
def Etoi_N(i):
    i = i.replace('N', 'ń')
def Etoi_D(i):
    i = i.replace('D', 'ԃ')
def Etoi_T(i):
    i = i.replace('T', 'т')
def Etoi_c(i):
    i = re.sub(r'c', 'ć', i, flags=re.IGNORECASE)
def Etoi6(i):
    i = (
        i.replace('A', 'α')
            .replace('N', 'ń')
            .replace('H', 'ɦ')
            .replace('D', 'ԃ')
            .replace('T', 'т')
    )
    i = re.sub(r'c', 'ć', i, flags=re.IGNORECASE)
    return i
def itoE_A(i):
    return i.replace('α', 'A')
def itoE_N(i):
    return i.replace('ń', 'N')
def itoE_H(i):
    return i.replace('ɦ', 'H')
def itoE_D(i):
    return i.replace('ԃ', 'D')  # (U+0503 ԃ)
def itoE_T(i):
    return i.replace('т', 'T')  # (U+0442 small_т)
def itoE_c(i):
    return i.replace('ć', 'c')  # ćꞇ
def itoE6(i):
    return i.replace('α', 'A').replace('ń', 'N').replace('ɦ', 'H').replace('ԃ', 'D').replace('т', 'T').replace('ć', 'c')
    

if __name__ == "__main__":
    i = """
all heavy after car cab \nhorse khel king kin rin ring 
yhel uncheck incite pencil ONCE FRANCES throw boTh siKh UNCLE AFTER
"""
    print("i initial value", i)
    i=e_to_i(i)
    print("i αfter e_to_i(i) is:", i)
    i=itoE6(i)
    print("i αfter itoE6(i) is:", i)
    Etoi6(i)
    print("i αfter Etoi6(i) is:", i)