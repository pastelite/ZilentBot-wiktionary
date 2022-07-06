import pywikibot as pwb
from pyquery import PyQuery as pq
site = pwb.Site("th","wiktionary")
pagename = 'projekti'
a = pq('https://th.wiktionary.org/wiki/'+pagename)      
def fi():
    lemma = a(this).text()
    form = a(this).parents('.form-of').attr('class')[8:-16].split('-')
    sp = form[0][:1]
    fo = form[1][:3]
    page = pwb.Page(site, lemma)
    page.text = '== ภาษาฟินแลนด์ =='
    page.text += '\n=== การออกเสียง ==='
    page.text += '\n* {{fi-IPA}}'
    page.text += '\n'
    page.text += '\n=== คำนาม ==='
    page.text += '\n{{head|fi|รูปผันคำนาม}}'
    page.text += '\n'
    page.text += '\n# {{{{inflection of|{}||{}|{}|lang=fi}}}}'.format(pagename,fo,sp)
    page.save(u"create finnish declension")
a('.form-of,.lang-fi').find('a').each(fi)
