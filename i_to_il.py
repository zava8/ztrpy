i_to_il_arr = ["टडपबसयरलमनफद","টডপবসযরলমনফদ","ਟਡਪਬਸਯਰਲਮਨਫਦ",
        "ટડપબસયરલમનફદ","ଟଡପବସଯରଲମନଫଦ","டdபbஸயரலமநfԃ","టడపబసయరలమనఫద",
        "ಟಡಪಬಸಯರಲಮನಫದ","tഡപബസയരലമനഫദ","ටඩපබසයරලමනඵԃ","ㅌㄸㅍㅂㅅㅑㄹ을ㅁㄴfԃ","тдпБсйрлмɦфԃ"]

def i_to_il(ioz):
    input_length = len(ioz['i'])
    ioz['o'] = ''
    oarr = [""] * 12
    indeks = 0
    hinchars = "tdpbsyrlmnf"

    while indeks < input_length:
        curr_char = ioz['i'][indeks]
        izileven = hinchars.find(curr_char)
        for i in range(12):
            if izileven > -1:
                oarr[i] += i_to_il_arr[i][izileven]
            else:
                oarr[i] += curr_char
        indeks += 1
    ioz['o'] = oarr

ioz = {'i':"TDaiueohcgtdpbs_yrlmnf",'o':""}
i_to_il(ioz)
print("ioz is: ", ioz)