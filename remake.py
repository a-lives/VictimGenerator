import json

popularity = 50

tg = ["甲","乙","丙","丁","戊","己","庚","辛","壬","癸"]
dz = ["子","丑","寅","卯","辰","巳","午","未","申","酉","戌","亥"]
namelist = []

for p in range(popularity):
    if p < 60:
        namelist.append( tg[p%10] + dz[p%12] )

# print(namelist)
with open("namelist.json",'w+') as f:
    f.write(json.dumps(namelist))