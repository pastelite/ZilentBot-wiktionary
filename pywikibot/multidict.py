from pyquery import PyQuery as pq
import csv
import pywikibot as pwb

wordwantlist = ['ผลไม้','พืช','ใบ','ราก','ดอกไม้','วัว','ฉลาม','งู','เป็ด']
dictsave = []
dictsave2 = {}

for wordwant in wordwantlist:

    print('-'*20)
    print('Start' + wordwant)
    print('-'*20)

    with open('wikt/wn-wikt-tha.tab', encoding='utf-8', newline = '') as dicts:                                                                                          
        dictreader = csv.DictReader(dicts, delimiter='\t')
        for word in dictreader:
            if word['http://wiktionary.org/'] == wordwant:
                print(word['# Wiktionary'])
                if word['# Wiktionary'] not in dictsave2:
                    dictsave2[word['# Wiktionary']] = []
                dictsave2[word['# Wiktionary']].append(['th', word['http://wiktionary.org/']])
                dictsave.append(word['# Wiktionary'])
                
    print(dictsave)
            
    with open('wikt/wn-wikt-eng.tab', encoding='utf-8', newline = '') as dicts:                                                                                          
        dictreader = csv.DictReader(dicts, delimiter='\t')
        for word in dictreader:
            if word['# Wiktionary'] in dictsave:
                dictsave2[word['# Wiktionary']].append(['en', word['http://wiktionary.org/']])
                print(word['http://wiktionary.org/'])
            
    with open('wikt/wn-wikt-fra.tab', encoding='utf-8', newline = '') as dicts:                                                                                          
        dictreader = csv.DictReader(dicts, delimiter='\t')
        for word in dictreader:
            if word['# Wiktionary'] in dictsave:
                dictsave2[word['# Wiktionary']].append(['fr', word['http://wiktionary.org/']])
                print(word['http://wiktionary.org/'])

    with open('wikt/wn-wikt-rus.tab', encoding='utf-8', newline = '') as dicts:                                                                                          
        dictreader = csv.DictReader(dicts, delimiter='\t')
        for word in dictreader:
            if word['# Wiktionary'] in dictsave:
                dictsave2[word['# Wiktionary']].append(['ru', word['http://wiktionary.org/']])
                print(word['http://wiktionary.org/'])
            
    with open('wikt/wn-wikt-fin.tab', encoding='utf-8', newline = '') as dicts:                                                                                          
        dictreader = csv.DictReader(dicts, delimiter='\t')
        for word in dictreader:
            if word['# Wiktionary'] in dictsave:
                dictsave2[word['# Wiktionary']].append(['fi', word['http://wiktionary.org/']])
                print(word['http://wiktionary.org/'])

    with open('wikt/wn-wikt-deu.tab', encoding='utf-8', newline = '') as dicts:                                                                                          
        dictreader = csv.DictReader(dicts, delimiter='\t')
        for word in dictreader:
            if word['# Wiktionary'] in dictsave:
                dictsave2[word['# Wiktionary']].append(['de', word['http://wiktionary.org/']])
                print(word['http://wiktionary.org/'])

    with open('wikt/wn-wikt-spa.tab', encoding='utf-8', newline = '') as dicts:                                                                                          
        dictreader = csv.DictReader(dicts, delimiter='\t')
        for word in dictreader:
            if word['# Wiktionary'] in dictsave:
                dictsave2[word['# Wiktionary']].append(['es', word['http://wiktionary.org/']])
                print(word['http://wiktionary.org/'])

    with open('wikt/wn-wikt-jpn.tab', encoding='utf-8', newline = '') as dicts:                                                                                          
        dictreader = csv.DictReader(dicts, delimiter='\t')
        for word in dictreader:
            if word['# Wiktionary'] in dictsave:
                dictsave2[word['# Wiktionary']].append(['ja', word['http://wiktionary.org/']])
                print(word['http://wiktionary.org/'])
            
    with open('wikt/wn-wikt-hbs.tab', encoding='utf-8', newline = '') as dicts:                                                                                          
        dictreader = csv.DictReader(dicts, delimiter='\t')
        for word in dictreader:
            if word['# Wiktionary'] in dictsave:
                dictsave2[word['# Wiktionary']].append(['sh', word['http://wiktionary.org/']])
                print(word['http://wiktionary.org/'])

    with open('wikt/wn-wikt-nld.tab', encoding='utf-8', newline = '') as dicts:                                                                                          
        dictreader = csv.DictReader(dicts, delimiter='\t')
        for word in dictreader:
            if word['# Wiktionary'] in dictsave:
                dictsave2[word['# Wiktionary']].append(['nl', word['http://wiktionary.org/']])
                print(word['http://wiktionary.org/'])
            
    with open('wikt/wn-wikt-ita.tab', encoding='utf-8', newline = '') as dicts:                                                                                          
        dictreader = csv.DictReader(dicts, delimiter='\t')
        for word in dictreader:
            if word['# Wiktionary'] in dictsave:
                dictsave2[word['# Wiktionary']].append(['it', word['http://wiktionary.org/']])
                print(word['http://wiktionary.org/'])

    with open('wikt/wn-wikt-cmn.tab', encoding='utf-8', newline = '') as dicts:                                                                                          
        dictreader = csv.DictReader(dicts, delimiter='\t')
        for word in dictreader:
            if word['# Wiktionary'] in dictsave:
                dictsave2[word['# Wiktionary']].append(['zh', word['http://wiktionary.org/']])
                print(word['http://wiktionary.org/'])

    with open('wikt/wn-wikt-ell.tab', encoding='utf-8', newline = '') as dicts:                                                                                          
        dictreader = csv.DictReader(dicts, delimiter='\t')
        for word in dictreader:
            if word['# Wiktionary'] in dictsave:
                dictsave2[word['# Wiktionary']].append(['el', word['http://wiktionary.org/']])
                print(word['http://wiktionary.org/'])
            
    with open('wikt/wn-wikt-por.tab', encoding='utf-8', newline = '') as dicts:                                                                                          
        dictreader = csv.DictReader(dicts, delimiter='\t')
        for word in dictreader:
            if word['# Wiktionary'] in dictsave:
                dictsave2[word['# Wiktionary']].append(['pt', word['http://wiktionary.org/']])
                print(word['http://wiktionary.org/'])

    with open('wikt/wn-wikt-swe.tab', encoding='utf-8', newline = '') as dicts:                                                                                          
        dictreader = csv.DictReader(dicts, delimiter='\t')
        for word in dictreader:
            if word['# Wiktionary'] in dictsave:
                dictsave2[word['# Wiktionary']].append(['sv', word['http://wiktionary.org/']])
                print(word['http://wiktionary.org/'])

    with open('wikt/wn-wikt-ces.tab', encoding='utf-8', newline = '') as dicts:                                                                                          
        dictreader = csv.DictReader(dicts, delimiter='\t')
        for word in dictreader:
            if word['# Wiktionary'] in dictsave:
                dictsave2[word['# Wiktionary']].append(['cz', word['http://wiktionary.org/']])
                print(word['http://wiktionary.org/'])
            
    with open('wikt/wn-wikt-bul.tab', encoding='utf-8', newline = '') as dicts:                                                                                          
        dictreader = csv.DictReader(dicts, delimiter='\t')
        for word in dictreader:
            if word['# Wiktionary'] in dictsave:
                dictsave2[word['# Wiktionary']].append(['bg', word['http://wiktionary.org/']])
                print(word['http://wiktionary.org/'])

    with open('wikt/wn-wikt-pol.tab', encoding='utf-8', newline = '') as dicts:                                                                                          
        dictreader = csv.DictReader(dicts, delimiter='\t')
        for word in dictreader:
            if word['# Wiktionary'] in dictsave:
                dictsave2[word['# Wiktionary']].append(['pl', word['http://wiktionary.org/']])
                print(word['http://wiktionary.org/'])
    print(dictsave2)

    for key in dictsave2:
        site = pwb.Site("pastldict")
        page = pwb.Page(site, 'def:'+key)
        page.text = '{| class="wikitable"\n'
        page.text += '|ID||[[Id::'+key[0:8]+']]\n|-\n'
        page.text += '|ID||[[Pos::'+key[9:]+']]\n|-\n'
        for lang in dictsave2[key]:
            page.text += '|'+lang[0]+'word||[['+lang[0]+'word::'+lang[1]+']]\n|-\n'
        page.text += '|}'
        print(page.text)
        page.save()
    
    ##site = pwb.Site("pastldict")
    ##page = pwb.Page(site, wordwant)
    ##page.text = '{{data|'+wordwant+'|th}}'
    ##page.save()
    
    dictsave = []
    dictsave2 = {}