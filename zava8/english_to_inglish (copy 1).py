import re
# ɦ(small_0266) (U+0144 ń) (U+03B1 α)
# (U+03C4 τ) (U+0442 small_т) (U+0503 small_ԃ)
# ɧ(small_0267) (U+00A2 ¢) (U+0256 ɖ) (U+0257 ɗ) (ć)
class ztrei:
    table_adhnt_itou = str.maketrans('ADHNTcC', 'αԃɦńтć')
    table_adhnt_utoi = str.maketrans('αԃɦńтć', 'ADHNTc')
    def __init__(self, i="", o=""):
        self.i = i
        self.o = o
    def __str__(self):
        return f"{self.i},{self.o})"
    def phonetic_h(self):
        self.i = re.sub('H','h', self.i)
        self.i = re.sub(r'(\s)h', r'\1H', self.i, re.I)
        self.i = re.sub(r'([^kgcjztdpbswKGCJZTDPBSW])h', r'\1H', self.i, re.I)
    def phonetic_n(self):
        self.i = re.sub(r'N', 'n', self.i)
        self.i = re.sub(r'n([cgk])\b', r'ṅ\1', self.i, flags=re.I)
        self.i = re.sub(r'\bn', 'ñ', self.i, flags=re.I)
        self.i = re.sub(r'([a-z])nk', r'\1ṅk', self.i, flags=re.I)
        self.i = re.sub(r'oung', 'ouṅg', self.i, flags=re.I)
        self.i = re.sub(r'ginge', 'giñge', self.i, flags=re.I)
        self.i = re.sub(r'([ht])inge', r'\1iñge', self.i, flags=re.I)
        self.i = re.sub(r'([fyc])ring', r'\1riñg', self.i, flags=re.I)
        self.i = re.sub(r'engin', 'eñgin', self.i, flags=re.I)
        self.i = re.sub(r'ngth', 'ñgth', self.i, flags=re.I)
        self.i = re.sub(r'ange([^dr])', r'añge\1', self.i, flags=re.I)
        self.i = re.sub(r'\bt([ai])ng([ei])', r't\1ñg\2', self.i, flags=re.I)
        self.i = re.sub(r'\bangi', 'añgi', self.i, flags=re.I)
        self.i = re.sub(r'inge', 'iñge', self.i, flags=re.I)
        self.i = re.sub(r'ing', 'iṅg', self.i, flags=re.I)
        self.i = re.sub(r'nge\b', 'ñge', self.i, flags=re.I)
        self.i = re.sub(r'ngel', 'ñgel', self.i, flags=re.I)
        self.i = re.sub(r'([dr])ang([ei])', r'\1añg\2', self.i, flags=re.I)
        self.i = re.sub(r'([lv])eng', r'\1eñg', self.i, flags=re.I)
        self.i = re.sub(r'chang([ei])', r'chañg\1', self.i, flags=re.I)
        self.i = re.sub(r'sseng', 'sseñg', self.i, flags=re.I)
        self.i = re.sub(r'nger', 'ṅger', self.i, flags=re.I)
        self.i = re.sub(r'([a-z])ng', r'\1ṅg', self.i, flags=re.I)
        self.i = re.sub(r'sync', 'syṅc', self.i, flags=re.I)
        self.i = re.sub(r'anchor', 'aṅchor', self.i, flags=re.I)
        self.i = re.sub(r'linco', 'liṅco', self.i, flags=re.I)
        self.i = re.sub(r'sincl', 'siṅcl', self.i, flags=re.I)
        self.i = re.sub(r'\buncle(s?)\b', r'uṅcle\1', self.i, flags=re.I)
        self.i = re.sub(r'menco', 'meṅco', self.i, flags=re.I)
        self.i = re.sub(r'([iu])nct', r'\1ṅct', self.i, flags=re.I)
        self.i = re.sub(r'nc([hyei])', r'ñc\1', self.i, flags=re.I)
        self.i = re.sub(r'inc([^hueioay])', r'iṅc\1', self.i, flags=re.I)
        self.i = re.sub(r'inc([aeiou])', r'iñc\1', self.i, flags=re.I)
        self.i = re.sub(r'([a-z])unc([^hyei])', r'\1uṅc\2', self.i, flags=re.I)
        self.i = re.sub(r'enc([^eiyh])', r'eñc\1', self.i, flags=re.I)
        self.i = re.sub(r'([ao])nc([^hyei])', r'\1ṅc\2', self.i, flags=re.I)
        self.i = re.sub(r'ṅ', 'N', self.i)
        self.i = re.sub(r'ñ', 'n', self.i)
    def phonetic_a(self):
        self.i = re.sub(r'A', 'a', self.i)
        self.i = re.sub(r'aft', 'αft', self.i, flags=re.I)
        self.i = re.sub(r'aw([kf\s])', r'αw\1', self.i, flags=re.I)
        self.i = re.sub(r'\bar([cekmst])\b', r'αr\1', self.i, flags=re.I)
        self.i = re.sub(r'guar', 'guαr', self.i, flags=re.I)
        self.i = re.sub(r'ijab', 'ijαb', self.i, flags=re.I)
        self.i = re.sub(r'ebab', 'ebαb', self.i, flags=re.I)
        self.i = re.sub(r'ihad', 'iHαԃ', self.i, flags=re.I)
        self.i = re.sub(r'ia([ck])', r'iα\1', self.i, flags=re.I)
        self.i = re.sub(r'\ba', 'à', self.i, flags=re.I)
        self.i = re.sub(r'ai\b', 'αi', self.i)
        self.i = re.sub(r'uar([bce-su-z])', r'uàr\1', self.i, flags=re.I)
        self.i = re.sub(r'([a-z])a\b', r'\1α', self.i, flags=re.I)
        self.i = re.sub(r'a([w])\b', r'α\1', self.i, flags=re.I)
        self.i = re.sub(r'\ba([ntsmd])\b', r'à\1', self.i, flags=re.I)
        self.i = re.sub(r'ar([aiey])', r'àr\1', self.i, flags=re.I)
        self.i = re.sub(r'([^uheio\s])arre([^lasn])', r'\1αrre\2', self.i, flags=re.I)
        self.i = re.sub(r'([eio\s])ar', r'\1àr', self.i, flags=re.I)
        self.i = re.sub(r'i([lgn])ar([^y])', r'i\1αr\2', self.i, flags=re.I)
        self.i = re.sub(r'([^beiuohlgn])ar([^y])', r'\1αr\2', self.i, flags=re.I)
        self.i = re.sub(r'bar([^oiuer])', r'bαr\1', self.i, flags=re.I)
        self.i = re.sub(r'era([\b\s])', r'erα\1', self.i, flags=re.I)
        self.i = re.sub(r'([bcdfह\b\s])all([^yo])', r'\1αll\2', self.i, flags=re.I)
        self.i = re.sub(r'ava', 'αvα', self.i, flags=re.I)
        self.i = re.sub(r'([^\b\soe])ard', r'\1αrd', self.i, flags=re.I)
        self.i = re.sub(r'([ag])raph', r'\1rαph', self.i, flags=re.I)
        self.i = re.sub(r'las([skmt])', r'lαs\1', self.i, flags=re.I)
    def e_to_i(self):
        self.phonetic_h()
        self.phonetic_n()
        self.phonetic_a()
        self.i = self.i.replace('H', 'ɦ').replace('N', 'ń').replace('à', 'a')
        self.i = self.i.lower().replace('th','тh')

    def Etoi_A(self):
        self.i = self.i.replace('A', 'α')
    def Etoi_H(self):
        self.i = self.i.replace('H', 'ɦ')
    def Etoi_N(self):
        self.i = self.i.replace('N', 'ń')
    def Etoi_D(self):
        self.i = self.i.replace('D', 'ԃ')
    def Etoi_T(self):
        self.i = self.i.replace('T', 'т')
    def Etoi_c(self):
        self.i = re.sub(r'c', 'ć', self.i, flags=re.IGNORECASE)
    def Etoi6(self):
        self.i = (
            self.i.replace('A', 'α')
                .replace('N', 'ń')
                .replace('H', 'ɦ')
                .replace('D', 'ԃ')
                .replace('T', 'т')
        )
        self.i = re.sub(r'c', 'ć', self.i, flags=re.IGNORECASE)
    def itoE_A(self):
        self.i = self.i.replace('α', 'A')
    def itoE_N(self):
        self.i = self.i.replace('ń', 'N')
    def itoE_H(self):
        self.i = self.i.replace('ɦ', 'H')
    def itoE_D(self):
        self.i = self.i.replace('ԃ', 'D')  # (U+0503 ԃ)
    def itoE_T(self):
        self.i = self.i.replace('т', 'T')  # (U+0442 small_т)
    def itoE_c(self):
        self.i = self.i.replace('ć', 'c')  # ćꞇ
    def itoE6(self):
        self.i = self.i.replace('α', 'A').replace('ń', 'N').replace('ɦ', 'H').replace('ԃ', 'D').replace('т', 'T').replace('ć', 'c')

if __name__ == "__main__":
    ts = """
all heavy after car cab \nhorse khel king kin rin ring 
yhel uncheck incite pencil ONCE FRANCES throw boTh siKh UNCLE AFTER
"""
    ztreio = ztrei(ts)
    print("ztreio.i initial value", ztreio.i)
    ztreio.e_to_i()
    print("ztreio.i αfter e_to_i() is:", ztreio)
    ztreio.itoE6()
    print("ztreio.i αfter itoE6() is:", ztreio.i)
    ztreio.Etoi6()
    print("ztreio.i αfter Etoi6() is:", ztreio.i)