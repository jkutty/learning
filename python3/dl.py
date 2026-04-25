base_str = 'http://warashi-asian-pornstars.fr/WAPdB-img/pornostars-f-galeries/5000/5828/large/wapdb-carole-tong-pornostar-asiatique.warashi-asian-pornstars.fr-5828-'
end_str = '.jpg'
num = 1
dl_list = []
dl_file = open('dllist.txt', 'w')

while num < 10: 
    dl_list.append(base_str + str(num) + end_str)
    dl_file.write(f'{base_str}00{num}{end_str}\n')
    num += 1

while num > 9 and num < 18:
    dl_file.write(f'{base_str}0{num}{end_str}\n')
    num += 1

#print(dl_list)
dl_file.close()
