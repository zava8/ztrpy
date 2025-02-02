import re
from u2idict import u2idict
def is_in_it(lst, val):
    if not isinstance(lst, tuple):
        tpl = tuple(lst.keys())
    return val in tpl
def u_to_i2(i):
    input_length = len(i)
    indeks = 0
    o=''
    curr_char = ''
    nekst_char = ''
    curr_char_code = 0
    nekst_char_code = 0
    prev_lang_code = 0
    curr_lang_code = 0
    nekst_lang_code = 0
    prev_char_modulo = 0
    curr_char_modulo = 0
    nekst_char_modulo = 0
    while indeks < input_length:
        prev_lang_code = curr_lang_code
        prev_char_modulo = curr_char_modulo

        if indeks == 0:
            curr_char = i[0]
        else:
            curr_char = nekst_char

        curr_char_code = ord(curr_char)
        curr_lang_code = curr_char_code // 0x80
        curr_char_modulo = curr_char_code % 0x80

        if indeks + 1 < input_length:
            nekst_char = i[indeks + 1]
            nekst_char_code = ord(nekst_char)
            nekst_lang_code = nekst_char_code // 0x80
            nekst_char_modulo = nekst_char_code % 0x80
        else:
            nekst_char = ''
            nekst_char_code = nekst_lang_code = nekst_char_modulo = -1
        if 0x11 < curr_lang_code < 0x1B:
            if is_in_it([7, 8, 9, 0xA, 0xD, 0xE, 0xF, 0x10, 0x13, 0x14], curr_char_modulo):
                if prev_lang_code > 0 and 0x14 < prev_char_modulo < 0x3A:
                    o += 'a'
                o += u2idict['all_phoniks_list'][curr_char_modulo]
            else:
                o += u2idict['all_phoniks_list'][curr_char_modulo]
            indeks += 1
        else:
            o += curr_char
            indeks += 1    
    return o

def N2null(i):
    i = re.sub(r'ń$', '', i)
    i = re.sub(r'ń([),\s\.!\?naeiouhć])', r'\1', i)
    i = re.sub(r'ń([bp])', r'm\1', i)
    i = re.sub(r'ń([^kg])', r'n\1', i)
    return i

def extendedhindi(i):
    i = re.sub(r'(\s)क्ष', r'\1sh', i)
    i = re.sub(r'^क्ष', 'sh', i)
    i = re.sub(r'ज्ञ', 'gy', i)
    return i

# ioz.i.value = ioz.i.value.replaceAll(
# 	/(\s)क्ष/g, "$1sh").replaceAll(
# 	/^क्ष/g, 'sh').replaceAll(
# 	'ज्ञ', 'gy');
def u_to_i(i):
    i=extendedhindi(i)
    i=u_to_i2(i)
    i=N2null(i)
    return i

if __name__ == "__main__":
    i = "क्ष राजनीतिज्ञों के पास जो कार्य करना चाहिए,आमआमआम वह करने कि अनुमति क्षनहीं है ."
    i=u_to_i(i)
    print(i)

# '''
# /********************** others
#  * compart.com/en/unicode/block/
#  * https://www.compart.com/en/unicode/U+03B1
#  * (U+00A3 £) (U+00A2 ¢) (U+00E0 à) (U+00E1 á) (U+0103 ă) (U+0127 ħ) (U+0144 ń)
#  * (U+0253 ɓ) (U+0256 ɖ) (U+0257 ɗ) (U+0266 ɦ) (U+0267 ɧ) (U+0271 ɱ) (U+029c small ʜ)
#  * (U+03B1 α) (U+03C4 τ)
#  * (U+043D small_н) (U+0442 small_т) (U+045B ћ)
#  * (U+0502 Ԃ) (U+0503 ԃ) (U+050F ԏ)
# **********************
# **********************
# **********************
# ********************** most liked ADHTN
#  * ɦ(small_0266) (U+0144 ń) (U+03B1 α)
#  * (U+03C4 τ) (U+0442 small_т) (U+0503 ԃ)
#  * ɧ(small_0267) (U+00A2 ¢) (U+0256 ɖ) (U+0257 ɗ)
# **********************
# **********************

# ********************** most liked others
#  * ɓ(small_0253) ɱ(small_0271) (U+00A3 £) (U+00A2 ¢)
# **********************
# **********************
# **********************/
# '''
# ɦ(small_0266) (U+0144 ń) (U+03B1 α)
# (U+03C4 τ) (U+0442 small_т) (U+0503 ԃ)
# ɧ(small_0267) (U+00A2 ¢) (U+0256 ɖ) (U+0257 ɗ)