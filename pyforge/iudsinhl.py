iudsinhl = {
        # 'N':(0xD81,0xD82,), # 0xD81 $ઁ CANDRABINDU , 0xD82 $ං ANUSVARAYA
        'e':(0xD91,0xD92,0xD93,0xDD9,0xDDA,0xDCA,0xDDB),# 0xD91 එ_e, 0xD92 ඒ_ee, 0xD93 ඓ_ai, 0xDD9 ෙ$_e, 0xDDA ේ$_ee
        'a':(0xD83,0xD85,0xDD0),  #  ःD83visarga, 0D85_අ_a, 0xDD0 $ැ_ae
        'A':(0xD86,0xDCF,0xDD1),  # 0D86 ආ_A, 0xDCF $ා_A, 0xDD1 $ෑ _aae
        'i':(0xD89,0xD8A,0xDD2,0xDD3),  # 0D89_ඉ_i, # 0D8A_ඊ_ii # 0xDD2 $ි_i # 0xDD3 $ී_ii
        'u':(0xD8B,0xD8C,0xDD4,0xDD6),  # 0D8B_උ_u, 0D8C_ඌ_uu, # 0xDD4 $ු_u, # 0xDD6 ූ$_uu
        'r':(0xDBB,0xD8D,0xD8E,0xDF2,0xDD8,),# 0xDBB ර_ra, 0xD8D ඍ_r, 0xD8E ඎ_rr, 0xDF2 $ෳ_rr, 0xDD8 $ෘ_r
        'l':(0xDBD,0xD8F,0xD90,0xDF3,0xDC5,0xDDF,),# 0xDBD ල_la , 0xD8F ඏ_l, 0xD90 ඐ_ll, 0xDF3 $ෲ_ll, 0xDC5 ළ_lla
        'o':(0xD94,0xD95,0xD96,0xDDC,0xDCA,0xDDE),# 0xD94 ඔ_o, 0xD95 ඕ_oo, 0xD96 ඖ_au

        'k':(0xD9A,), # 0xD9A ක_k
        'K':(0xD9B,), # 0xD9B ඛ_kha	
        'g':(0xD9C,), # 0xD9C ග_g
        'G':(0xD9D,), # 0xD9D ඝ_gha
        'c':(0xDA0,), # 0xDA0 ච_ca
        'C':(0xDA1,), # 0xDA1 ඡ_cha
        'z':(0xDA2,), # 0xDA2 ජ_ja
        'Z':(0xDA3,), # 0xDA3 ඣ_jha
        'n':(0xDA4,), # 0xDA4 ඤ_nya
        't':(0xDA7,0xDA8,), # 0xDA7 ට_t, 0xDA8 ඨ_th
        'T':(0xDAD,0xDAE,), # 0xDAD ත_T, 0xDAE ථ_Th
        'd':(0xDA9,0xDAA,), # 0xDA9 ඩ_d, 0xDAA ඪ_dh
        'D':(0xDAF,0xDB0), # 0xDAF ද_D, 0xDB0 ධ_Dh 

        'p':(0xDB4,),  # 0xDB4 ප_pa	
        'f':(0xDB5,0xDC6),  # 0xDB5 ඵ_pha, 0xDC6 ෆ_fa
        'b':(0xDB6,),  # 0xDB6 බ_ba
        'B':(0xDB7,),  # 0xDB7 භ_bha	
        'm':(0xDB8,0xDB9,),  # 0xDB8 ම_ma 0xDB9 ඹ_mba
        'y':(0xDBA,),  # 0xDBA ය_ya

        'w':(0xDC0,), # 0xDC0 ව_va
        'S':(0xDC1,), # 0xDC1 ශ_sha
        's':(0xDC2,0xDC3,), # 0xDC2 ෂ_ssa, 0xDC3 ස_sa
        'H':(0x939,),  # 0xDC4 හ_ha

        '0':(0xDE6,),  # ० 0x966
        '1':(0xDE7,),  # १ 0x967
        '2':(0xDE8,),  # २ 0x968
        '3':(0xDE9,),  # ३ 0x969
        '4':(0xDEA,),  # ४ 0x96A
        '5':(0xDEB,),  # ५ 0x96B
        '6':(0xDEC,),  # ६ 0x96C
        '7':(0xDED,),  # ७ 0x96D
        '8':(0xDEE,),  # ८ 0x96E
        '9':(0xDEF,),  # ९ 0x96F
}

#################
# 0xD81 $ઁ SINHALA SIGN CANDRABINDU # • used in Sanskrit
# 0xD82 $ං SINHALA SIGN ANUSVARAYA # = anusvara
# 0xD83 $ඃ SINHALA SIGN VISARGAYA # = visarga
# 0xD85 අ_a
# 0xD86 ආ_A
# 0xD87 ඇ SINHALA LETTER AEYANNA # = sinhala letter ae
# 0xD88 ඈ SINHALA LETTER AEEYANNA # = sinhala letter aae
# 0xD89 ඉ_i
# 0xD8A ඊ_ii
# 0xD8B උ_u
# 0xD8C ඌ_uu
# 0xD8D ඍ_r
# 0xD8E ඎ_rr
# 0xD8F ඏ_l
# 0xD90 ඐ_ll
# 0xD91 එ_e
# 0xD92 ඒ_ee
# 0xD93 ඓ_ai=e
# 0xD94 ඔ_o
# 0xD95 ඕ_oo
# 0xD96 ඖ_au
############# Consonants ################
# 0xD9A ක_ka
# 0xD9B ඛ_kha
# 0xD9C ග_ga
# 0xD9D ඝ_gha
# 0xD9E ඞ_nga
# 0xD9F ඟ_nnga
# 0xDA0 ච_ca
# 0xDA1 ඡ_cha
# 0xDA2 ජ_ja
# 0xDA3 ඣ_jha
# 0xDA4 ඤ_nya
# 0xDA5 ඥ SINHALA LETTER TAALUJA SANYOOGA # NAAKSIKYAYA # = sinhala letter jnya 
# 0xDA6 ඦ SINHALA LETTER SANYAKA JAYANNA # = sinhala letter nyja
# 0xDA7 ට_t
# 0xDA8 ඨ_th
# 0xDA9 ඩ_d
# 0xDAA ඪ_dh
# 0xDAB ණ_nna
# 0xDAC ඬ_nndda
# 0xDAD ත_T
# 0xDAE ථ_Th
# 0xDAF ද_D
# 0xDB0 ධ_Dh
# 0xDB1 න_na
# 0xDB3 ඳ_nda
# 0xDB4 ප_pa
# 0xDB5 ඵ_pha
# 0xDB6 බ_ba
# 0xDB7 භ_bha
# 0xDB8 ම_ma
# 0xDB9 ඹ_mba
# 0xDBA ය_ya
# 0xDBB ර_ra
# 0xDBD ල_la
# 0xDC0 ව_va
# 0xDC1 ශ_sha
# 0xDC2 ෂ_ssa
# 0xDC3 ස_sa
# 0xDC4 හ_ha
# 0xDC5 ළ_lla
# 0xDC6 ෆ_fa
# 0xDCA $් SINHALA SIGN AL-LAKUNA # = virama
# Dependent vowel signs
# 0xDCF $ා_A
# 0xDD0 $ැ_ae
# 0xDD1 $ෑ _aae
# 0xDD2 $ි_i
# 0xDD3 $ී_ii
# 0xDD4 $ු_u
# 0xDD6 ූ$_uu
# 0xDD8 $ෘ_r
# 0xDD9 ෙ$_e
# 0xDDA ේ$_ee
# ≡ 0DD9ෙ$  0DCA $් 0DDBෛ$ SINHALA VOWEL SIGN KOMBU DEKA # = sinhala vowel sign ai
# Two-part dependent vowel signs
# These vowel signs have glyph pieces which stand on both
# sides of the consonant; they follow the consonant in logical
# order, and should be handled as a unit for most processing.
# 0xDDC ො$_o
# ≡ 0DD9ෙ$  0DCF $ා 0DDD ෝ$ SINHALA VOWEL SIGN KOMBUVA HAA DIGA
# AELA-PILLA
# = sinhala vowel sign oo
# ≡ 0DDCො$   0DCA $් 0DDE ෞ$ SINHALA VOWEL SIGN KOMBUVA HAA
# GAYANUKITTA
# = sinhala vowel sign au
# ≡ 0DD9ෙ$  0DDF $ෟ
# Dependent vowel sign
# 0xDDF $ෟ SINHALA VOWEL SIGN GAYANUKITTA
# = sinhala vowel sign vocalic
# 0xDE6 ෦ SINHALA LITH DIGIT ZERO
# 0xDE7 ෧ SINHALA LITH DIGIT ONE
# 0xDE8 ෨ SINHALA LITH DIGIT TWO
# 0xDE9 ෩ SINHALA LITH DIGIT THREE
# 0xDEA ෪ SINHALA LITH DIGIT FOUR
# 0xDEB ෫ SINHALA LITH DIGIT FIVE
# 0xDEC ෬ SINHALA LITH DIGIT SIX
# 0xDED ෭ SINHALA LITH DIGIT SEVEN
# 0xDEE ෮ SINHALA LITH DIGIT EIGHT
# 0xDEF ෯ SINHALA LITH DIGIT NINE
# Astrological digits
# These digits, also known as Sinhala Lith Illakkam, have been
# used primarily for writing horoscopes. This number system
# has a zero place holder concept, unlike the Sinhala archaic
# numbers, Sinhala Illakkam, encoded in the range 111E1-
# 111F4.

# Additional dependent vowel signs
# 0xDF2 $ෳ_rr
# 0xDF3 $ෲ_ll
# Punctuation
# 0xDF4 ෴ SINHALA PUNCTUATION KUNDDALIYA
# → 11FFFÄ  tamil punctuation end of text