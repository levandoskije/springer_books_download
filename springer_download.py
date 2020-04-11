#!/usr/bin/env python3
# coding: utf-8

import os


file = {'title': [],
        'class': [],
        'doi': [],
        'link': [],
        'name_old': [],
        'name_new': []}
tab = open('tab_links.csv', 'r')

for row in tab:
    row = row.split(',')
    
    file['title'].append(row[0])
    file['class'].append(row[1])
    file['doi'].append(row[2])
    link = 'https://link.springer.com/content/pdf/' + str(row[-1])[8:-1].replace('/', '%2F') + '.pdf'
    file['link'].append(link)
    name_old = link.split('/')[-1]
    file['name_old'].append(name_old)
    name_new = str(row[1]) + '/' + str(row[0])  + '.pdf'
    name_new = name_new.replace('"', '').replace(':', '').strip()
    name_new = f'"{name_new}"'
    file['name_new'].append(name_new)

for i in file['class']:
    folder = 'mkdir ' + f'"{i.strip()}"'
    try:
        os.system(folder)
    except:
        pass
    
for i in range(len(file['title'])):
# for i in [1, 2, 5, 7, 11, 15, 24]:
    wget = 'wget ' + file['link'][i]
    name_new  = file['name_new'][i]
    mv = 'mv ' + file['name_old'][i] + ' ' + name_new
    
    try:
        os.system(wget)
        try:
            os.system(mv)
        except:
            print(f"Falha em renomear {file['name_old'][i]} => {name_new}")
            pass
        
        print(f'Arquivo {name_new} renomeado!')
    except:
        print(f'Falha no downlad de {name_new}')
        pass
    
    print(f'Download de {name_new} concluído!')
    




