def modify_string(argstring):
    table_adhnt = str.maketrans('ADHNT', 'αԃɦńт')
    argstring = argstring.translate(table_adhnt)
    return argstring
# ɦ(small_0266) (U+0144 ń) (U+03B1 α)
# (U+03C4 τ) (U+0442 small_т) (U+0503 ԃ)
# ɧ(small_0267) (U+00A2 ¢) (U+0256 ɖ) (U+0257 ɗ)
my_string = 'AAM amruuD DHi DuuDh aNguur Trbuz tomato jug'
modified_string = modify_string(my_string)

print(my_string)
print(modified_string)