const json = require("./import/eng2thai.json")
const cheerio = require('cheerio')
const MWBot = require('mwbot');
const config = require('./config.json')
pl = ''
let enbot = new MWBot({
  apiUrl: 'https://en.wiktionary.org/w/api.php',
  username: config.u,
  password: config.p
})
let bot = new MWBot({
  apiUrl: 'https://th.wiktionary.org/w/api.php',
  username: config.u,
  password: config.p
})
let $;
var wait = ms => new Promise((r, j)=>setTimeout(r, ms))
async function getwikitext(search) {
  $ = cheerio.load(json)
  var wikitext ='== ภาษาอังกฤษ ==\n{{lexitronimport}}'
  var N = [],VT = [],VI = [],ADJ = [],ADV = [],ABBR = []
  var forchecksearch = []
  $(json).each((i,v) => {
    if (v.search==search) {
      if (v.type=="N") {
        N.push(v.result)
      }
      else if (v.type=="VI" || v.type=="VI, VT") {
        VI.push(v.result)
      }
      else if (v.type=="VT" || v.type=="VI, VT") {
        VT.push(v.result)
      }
      else if (v.type=="ADJ") {
        ADJ.push(v.result)
      }
      else if (v.type=="ADV") {
        ADV.push(v.result)
      }
      else if (v.type=="ABBR") {
        ABBR.push(v.result)
      }
      forchecksearch.push(v.search)
    }
  })
  if(forchecksearch.length==0) {
    console.log('err')
    return undefined
  }
  //Get
  res = await enbot.request({action:'parse',page:search,prop:'wikitext'})
  entext = res.parse.wikitext['*']
  entextwn = entext.replace(/\n/g,"<br>");
  //console.log(entext)
  //console.log(wikitext)
  //Pronunciation
  var enpro = entextwn.match(/===Pronunciation===(.*?)===/)
  if (enpro) {
    wikitext += '\n=== การออกเสียง{{botenimport}} ==='
    var sliced = '\n' + enpro[0].slice(23,-11).replace(/<br>/g,"\n")
    wikitext += sliced
  }
  //Noun
  var ennhead = entext.match(/{{en-noun(.*?)}}/)
  if (N.length > 0) {
    wikitext += '\n=== คำนาม ==='
    if (ennhead) {
      wikitext += '\n' + ennhead[0] + '{{botenimport}}'
    } else {
      wikitext += '\n{{head|en|คำนาม}}{{botdontfound}}'
    }
    N.forEach((ele)=> {
      wikitext += '\n# '+ele
    })
  }
  //Verb
  var envhead = entext.match(/{{en-verb(.*?)}}/)
  if (VI.length > 0 || VT.length > 0){
    wikitext += '\n=== คำกริยา ==='
    if (envhead) {
      wikitext += '\n' + envhead[0] + '{{botenimport}}'
    } else {
      wikitext += '\n{{head|en|คำกริยา}}{{botdontfound}}'
    }
    VI.forEach((ele) => {
      wikitext += '\n# {{lb|en|อกรรม}} ' + ele
    })
    VT.forEach((ele) => {
      wikitext += '\n# {{lb|en|สกรรม}} ' + ele
    })
  }
  //adj
  var enadjhead = entext.match(/{{en-adj(.*?)}}/)
  if (ADJ.length > 0 ) {
    wikitext += '\n=== คำคุณศัพท์ ==='
    if (enadjhead) {
      wikitext += '\n' + enadjhead[0] + '{{botenimport}}'
    } else {
      wikitext += '\n{{head|en|คำคุณศัพท์}}{{botdontfound}}'
    }
    ADJ.forEach((ele)=>{
      wikitext += '\n# ' + ele
    })
  }
  //adv
  var enadvhead = entext.match(/{{en-adv(.*?)}}/)
  if (ADV.length > 0 ) {
    wikitext += '\n=== คำกริยาวิเศษณ์ ==='
    if (enadvhead) {
      wikitext += '\n' + enadvhead[0] + '{{botenimport}}'
    } else {
      wikitext += '\n{{head|en|คำกริยาวิเศษณ์}}{{botdontfound}}'
    }
    ADV.forEach((ele)=>{
      wikitext += '\n# ' + ele
    })
  }
  //ABBR
  if (ABBR.length>0) {
    wikitext += '\n=== ตัวย่อ ===\n{{head|en|ตัวย่อ}}'
    ABBR.forEach((ele)=>{
      wikitext += '\n# ' + ele
    })
  }
  return wikitext
}
//main
async function main() {
  var pagelist = ['comfortably','command','comment','commercial','commission','commit','commitment']
  await pagelist.forEach(async (page)=>{
    paggg = await getwikitext(page)
    try {
      await bot.create(page,paggg,'นำเข้าคำจาก Lexitron')
    } catch(err) {
      console.log('err',page)
    }
    console.log('creat page',page,'succesfull')
    await wait(1000)
  })
}

bot.loginGetEditToken().then((res) => {
  main()
  //main()
})
