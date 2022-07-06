import pywikibot as pwb
from pyquery import PyQuery as pq
site = pwb.Site("th","wiktionary")
pagename = 'év'
a = pq('https://th.wiktionary.org/wiki/'+pagename)      
def fi():
    lemma = a(this).text()
    form = a(this).parents('.form-of').attr('class')[16:-8].split('-')
    sp = form[1][:1]
    fo = form[0][:3]
    page = pwb.Page(site, lemma)
    page.text = '== ภาษาฮังการี =='
    page.text += '\n=== การออกเสียง ==='
    page.text += '\n* {{hu-IPA}}'
    page.text += '\n'
    page.text += '\n=== คำนาม ==='
    page.text += '\n{{head|hu|รูปผันคำนาม}}'
    page.text += '\n'
    page.text += '\n# {{{{inflection of|{}||{}|{}|lang=hu}}}}'.format(pagename,fo,sp)
    ##print(pagetext)
    page.save(u"create hungarian declension")
a('.form-of,.lang-hu').find('a').each(fi)
