f = open("SomeFile.txt",'r')

data = f.readlines()

while (data.count("\n")):
        data.remove("\n")

dict1 = {}
dict2 = {}

for lines in data:
        if(lines.startswith("Handle")):
            h = lines[0:6]
            hv = lines[7:13]
            d = lines[15:23]
            dt = lines[24:-1]
            dict2[h] = hv
            dict2[d] = dt
        elif(lines.startswith("\tSocket")):
            s = lines[1:20]
            v = lines[21:-1]
            dict2[s] =v
        elif(lines.startswith("\tConfiguration:")):
            c = lines[1:14]
            v = lines[16:-1]
            dict2[c] = v
        elif(lines.startswith("\tOperational")):
            o = lines[1:17]
            v = lines[19:-1]
            dict2[o] = v
        elif(lines.startswith("\tLocation:")):
            l = lines[1:9]
            v = lines[11:-1]
            dict2[l] = v
        elif(lines.startswith("\tInstalled Size:")):
            i = lines[1:15]
            v = lines[17:-1]
            dict2[i] = v
        elif(lines.startswith("\tMaximum")):
            m = lines[1:13]
            v = lines[15:-1]
            dict2[m] = v
        elif(lines.startswith("\t\tSynchronous")):
            s = lines[2:-1]
            dict2['Supported SRAM Types']= s
        elif(lines.startswith("\tInstalled SRAM Type")):
            I = lines[1:20]
            v = lines[22:-1]
            dict2[I] = v
        elif(lines.startswith("\tSpeed:")):
            S = lines[1:6]
            v = lines[8:-1]
            dict2[S] = v
        elif(lines.startswith("\tError Correction Type:")):
            e = lines[1:22]
            v = lines[24:-1]
            dict2[e] = v
        elif(lines.startswith("\tSystem Type:")):
            s1 = lines[1:12]
            v = lines[14:-1]
            dict2[s1] = v
        elif(lines.startswith("\tAssociativity:")):
            a = lines[1:14]
            v = lines[16:-1]
            dict2[a] = v
            dict1[dict2['Handle']] = dict2
            #print(len(dict1))
            dict2={}
        else:
            pass

    #out_file = open("output.json","w")
    #obj = json.dump(dict1 , out_file , indent = (len(dict1)))
    #out_file.close()
print(dict1)