f = open("bios.txt",'r')

data = f.readlines()

while (data.count("\n")):
        data.remove("\n")


dict1 = {}
dict2 = {}
dict3 = {}
dict4 = {}


for lines in data:
    if (lines.startswith("BIOS Information")):
        m = lines[0:16]
        dict2['BIOS Information'] = m
    elif(lines.startswith("Handle")):
        d = lines[0:6]
        a = lines[7:13]
        b = lines[15:23]
        c = lines[24:-1]
        dict2[d] = a
        dict2[b] = c
    elif(lines.startswith("\tVendor")):
        e = lines[9:-1]
        dict2['Vendor'] = e
    elif (lines.startswith("\tVersion")):
        f = lines[10:-1]
        dict2['Version'] = f
    elif (lines.startswith("\tRelease Date")):
        g = lines[14:-1]
        dict2['Release Date'] = g
    elif (lines.startswith("\tAddress")):
        h = lines[9:-1]
        dict2['Address'] = h
    elif (lines.startswith("\tRuntime Size")):
        i = lines[14:-1]
        dict2['Runtime Size'] = i
    elif (lines.startswith("\tROM Size")):
        j = lines[10:-1]
        dict2['ROM Size'] = j
    elif (lines.startswith("\tCharacteristics")):
        k = lines[17:-1]
        dict2['Characteristics'] = k

        dict1[dict2['BIOS Information']] = dict2
    elif (lines.startswith("BIOS Language Information")):
        n = lines[0:25]
        dict3["BIOS Language Information"] = n
    elif (lines.startswith("\tLanguage Description Format")):
        o = lines[29:-1]
        dict3["Language Description Format"] = o
    elif (lines.startswith("\tInstallable Languages")):
        p = lines[23:-1]
        dict3["Installable Languages"] = p
    elif (lines.startswith("\tCurrently Installed Language")):
        q = lines[30:-1]
        dict3["Currently Installed Language"] = q
        dict4[dict3['BIOS Language Information']] = dict3

    else:
        pass
    dic = []
    dic.append(dict1)
    dic.append(dict4)
print(dic)
#print(dict4)