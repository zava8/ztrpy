import re
# ɦ(small_0266) (U+0144 ń) (U+03B1 α)
# (U+03C4 τ) (U+0442 small_т) (U+0503 small_ԃ)
# ɧ(small_0267) (U+00A2 ¢) (U+0256 ɖ) (U+0257 ɗ)
def phonetic_h(ioz):
    text = ioz['i']
    text = re.sub('H','h', text)
    text = re.sub(r'(\s)h', r'\1H', text, re.I)
    text = re.sub(r'([^kgcjztdpbswKGCJZTDPBSW])h', r'\1H', text, re.I)
    ioz['i'] = text
def phonetic_n(ioz):
    ioz["i"] = re.sub(r'N', 'n', ioz["i"])
    ioz["i"] = re.sub(r'n([cgk])\b', r'ṅ\1', ioz["i"], flags=re.I)
    ioz["i"] = re.sub(r'\bn', 'ñ', ioz["i"], flags=re.I)
    ioz["i"] = re.sub(r'([a-z])nk', r'\1ṅk', ioz["i"], flags=re.I)
    ioz["i"] = re.sub(r'oung', 'ouṅg', ioz["i"], flags=re.I)
    ioz["i"] = re.sub(r'ginge', 'giñge', ioz["i"], flags=re.I)
    ioz["i"] = re.sub(r'([ht])inge', r'\1iñge', ioz["i"], flags=re.I)
    ioz["i"] = re.sub(r'([fyc])ring', r'\1riñg', ioz["i"], flags=re.I)
    ioz["i"] = re.sub(r'engin', 'eñgin', ioz["i"], flags=re.I)
    ioz["i"] = re.sub(r'ngth', 'ñgth', ioz["i"], flags=re.I)
    ioz["i"] = re.sub(r'ange([^dr])', r'añge\1', ioz["i"], flags=re.I)
    ioz["i"] = re.sub(r'\bt([ai])ng([ei])', r't\1ñg\2', ioz["i"], flags=re.I)
    ioz["i"] = re.sub(r'\bangi', 'añgi', ioz["i"], flags=re.I)
    ioz["i"] = re.sub(r'inge', 'iñge', ioz["i"], flags=re.I)
    ioz["i"] = re.sub(r'ing', 'iṅg', ioz["i"], flags=re.I)
    ioz["i"] = re.sub(r'nge\b', 'ñge', ioz["i"], flags=re.I)
    ioz["i"] = re.sub(r'ngel', 'ñgel', ioz["i"], flags=re.I)
    ioz["i"] = re.sub(r'([dr])ang([ei])', r'\1añg\2', ioz["i"], flags=re.I)
    ioz["i"] = re.sub(r'([lv])eng', r'\1eñg', ioz["i"], flags=re.I)
    ioz["i"] = re.sub(r'chang([ei])', r'chañg\1', ioz["i"], flags=re.I)
    ioz["i"] = re.sub(r'sseng', 'sseñg', ioz["i"], flags=re.I)
    ioz["i"] = re.sub(r'nger', 'ṅger', ioz["i"], flags=re.I)
    ioz["i"] = re.sub(r'([a-z])ng', r'\1ṅg', ioz["i"], flags=re.I)
    ioz["i"] = re.sub(r'sync', 'syṅc', ioz["i"], flags=re.I)
    ioz["i"] = re.sub(r'anchor', 'aṅchor', ioz["i"], flags=re.I)
    ioz["i"] = re.sub(r'linco', 'liṅco', ioz["i"], flags=re.I)
    ioz["i"] = re.sub(r'sincl', 'siṅcl', ioz["i"], flags=re.I)
    ioz["i"] = re.sub(r'\buncle(s?)\b', r'uṅcle\1', ioz["i"], flags=re.I)
    ioz["i"] = re.sub(r'menco', 'meṅco', ioz["i"], flags=re.I)
    ioz["i"] = re.sub(r'([iu])nct', r'\1ṅct', ioz["i"], flags=re.I)
    ioz["i"] = re.sub(r'nc([hyei])', r'ñc\1', ioz["i"], flags=re.I)
    ioz["i"] = re.sub(r'inc([^hueioay])', r'iṅc\1', ioz["i"], flags=re.I)
    ioz["i"] = re.sub(r'inc([aeiou])', r'iñc\1', ioz["i"], flags=re.I)
    ioz["i"] = re.sub(r'([a-z])unc([^hyei])', r'\1uṅc\2', ioz["i"], flags=re.I)
    ioz["i"] = re.sub(r'enc([^eiyh])', r'eñc\1', ioz["i"], flags=re.I)
    ioz["i"] = re.sub(r'([ao])nc([^hyei])', r'\1ṅc\2', ioz["i"], flags=re.I)
    ioz["i"] = re.sub(r'ṅ', 'N', ioz["i"])
    ioz["i"] = re.sub(r'ñ', 'n', ioz["i"])

def phonetic_a(ioz):
    ioz["i"] = re.sub(r'A', 'a', ioz["i"])
    ioz["i"] = re.sub(r'aft', 'αft', ioz["i"], flags=re.I)
    ioz["i"] = re.sub(r'aw([kf\s])', r'αw\1', ioz["i"], flags=re.I)
    ioz["i"] = re.sub(r'\bar([cekmst])\b', r'αr\1', ioz["i"], flags=re.I)
    ioz["i"] = re.sub(r'guar', 'guαr', ioz["i"], flags=re.I)
    ioz["i"] = re.sub(r'ijab', 'ijαb', ioz["i"], flags=re.I)
    ioz["i"] = re.sub(r'ebab', 'ebαb', ioz["i"], flags=re.I)
    ioz["i"] = re.sub(r'ihad', 'iHαԃ', ioz["i"], flags=re.I)
    ioz["i"] = re.sub(r'ia([ck])', r'iα\1', ioz["i"], flags=re.I)
    ioz["i"] = re.sub(r'\ba', 'à', ioz["i"], flags=re.I)
    ioz["i"] = re.sub(r'ai\b', 'αi', ioz["i"])
    ioz["i"] = re.sub(r'uar([bce-su-z])', r'uàr\1', ioz["i"], flags=re.I)
    ioz["i"] = re.sub(r'([a-z])a\b', r'\1α', ioz["i"], flags=re.I)
    ioz["i"] = re.sub(r'a([w])\b', r'α\1', ioz["i"], flags=re.I)
    ioz["i"] = re.sub(r'\ba([ntsmd])\b', r'à\1', ioz["i"], flags=re.I)
    ioz["i"] = re.sub(r'ar([aiey])', r'àr\1', ioz["i"], flags=re.I)
    ioz["i"] = re.sub(r'([^uheio\s])arre([^lasn])', r'\1αrre\2', ioz["i"], flags=re.I)
    ioz["i"] = re.sub(r'([eio\s])ar', r'\1àr', ioz["i"], flags=re.I)
    ioz["i"] = re.sub(r'i([lgn])ar([^y])', r'i\1αr\2', ioz["i"], flags=re.I)
    ioz["i"] = re.sub(r'([^beiuohlgn])ar([^y])', r'\1αr\2', ioz["i"], flags=re.I)
    ioz["i"] = re.sub(r'bar([^oiuer])', r'bαr\1', ioz["i"], flags=re.I)
    ioz["i"] = re.sub(r'era([\b\s])', r'erα\1', ioz["i"], flags=re.I)
    ioz["i"] = re.sub(r'([bcdfह\b\s])all([^yo])', r'\1αll\2', ioz["i"], flags=re.I)
    ioz["i"] = re.sub(r'ava', 'αvα', ioz["i"], flags=re.I)
    ioz["i"] = re.sub(r'([^\b\soe])ard', r'\1αrd', ioz["i"], flags=re.I)
    ioz["i"] = re.sub(r'([ag])raph', r'\1rαph', ioz["i"], flags=re.I)
    ioz["i"] = re.sub(r'las([skmt])', r'lαs\1', ioz["i"], flags=re.I)
def e_to_i(ioz):
    phonetic_h(ioz)
    phonetic_n(ioz)
    phonetic_a(ioz)
    ioz['i'] = ioz['i'].replace('H', 'ɦ').replace('N', 'ń').replace('à', 'a')
    ioz['i'] = ioz['i'].lower().replace('th','тh')

def Etoi_A(ioz):
    ioz['i'] = ioz['i'].replace('A', 'α')
def Etoi_H(ioz):
    ioz['i'] = ioz['i'].replace('H', 'ɦ')
def Etoi_N(ioz):
    ioz['i'] = ioz['i'].replace('N', 'ń')
def Etoi_D(ioz):
    ioz['i'] = ioz['i'].replace('D', 'ԃ')
def Etoi_T(ioz):
    ioz['i'] = ioz['i'].replace('T', 'т')
def Etoi_c(ioz):
    ioz['i'] = re.sub(r'c', 'ć', ioz['i'], flags=re.IGNORECASE)
def Etoi6(ioz):
    ioz['i'] = (
        ioz['i'].replace('A', 'α')
             .replace('N', 'ń')
             .replace('H', 'ɦ')
             .replace('D', 'ԃ')
             .replace('T', 'т')
    )
    ioz['i'] = re.sub(r'c', 'ć', ioz['i'], flags=re.IGNORECASE)
def itoE_A(ioz):
    ioz['i'] = ioz['i'].replace('α', 'A')
def itoE_N(ioz):
    ioz['i'] = ioz['i'].replace('ń', 'N')
def itoE_H(ioz):
    ioz['i'] = ioz['i'].replace('ɦ', 'H')
def itoE_D(ioz):
    ioz['i'] = ioz['i'].replace('ԃ', 'D')  # (U+0503 ԃ)
def itoE_T(ioz):
    ioz['i'] = ioz['i'].replace('т', 'T')  # (U+0442 small_т)
def itoE_c(ioz):
    ioz['i'] = ioz['i'].replace('ć', 'c')  # ćꞇ
def itoE6(ioz):
    ioz['i'] = ioz['i'].replace('α', 'A').replace('ń', 'N').replace('ɦ', 'H').replace('ԃ', 'D').replace('т', 'T').replace('ć', 'c')

ts = """
all heavy after car cab \nhorse khel king kin rin ring 
yhel uncheck incite pencil ONCE FRANCES throw boTh siKh UNCLE AFTER
"""
ioz = {"i": ts,"o":""}
print("ioz['i']=ts= ", ioz['i'])
e_to_i(ioz)
print("ioz['i'] αfter e_to_i(ioz) is:", ioz['i'])
itoE6(ioz)
print("ioz['i'] αfter itoE6(ioz) is:", ioz['i'])
Etoi6(ioz)
print("ioz['i'] αfter Etoi6(ioz) is:", ioz['i'])