var bot = require('nodemw')
var http = require("http");
const config = require('./config.json')

//Cheerio, jQuery in nodejs :thinking:
const cheerio = require('cheerio')
let $;

var client = new bot({
    protocol: 'https',           // Wikipedia now enforces HTTPS
    server: 'th.wiktionary.org',  // host name of MediaWiki-powered site
    path: '/w',                  // path to api.php script
    username: config.u,
    password: config.p,
    debug: false                 // is more verbose when set to true
  });

function creat (pagetocreat) {
  //Get html of page
  client.api.call({action:'parse',page:pagetocreat}, function (err,a,b,pass) {
    x = pass.parse.text['*']
    $ = cheerio.load(x)
    var decl = []
    //add text with form of to decl
    $('.form-of').find('a').each(function (i,elem) {
      decl.push($(this).text())
    })
    var uniquedecl = []
    //remove duplicate
    decl.forEach(function(el){
      if(uniquedecl.indexOf(el) === -1) uniquedecl.push(el);
    });
    //console.log(uniquedecl)
    //get decl and creat page
    uniquedecl.forEach(function (ele) {
      var ttc = []
      //get class of each
      $('a:contains('+ele+')').each(function () {
        if($(this).text().length === ele.length) {
          ttc.push($(this).parent().parent().attr('class'))
        }
      })
      var uniquettc = []
      //get rid of duplicate
      ttc.forEach(function(el){
        if(uniquettc.indexOf(el) === -1) uniquettc.push(el);
      });
      console.log(uniquettc)
      //var decl form class
      var infl = {
        'plural-nominative':'nom|p',
        'singular-genitive':'gen|s',
        'plural-genitive':'gen|p',
        'singular-partitive':'par|s',
        'plural-partitive':'par|p',
        'singular-inessive':'ine|s',
        'plural-inessive':'ine|p',
        'singular-elative':'ela|s',
        'plural-elative':'ela|p',
        'singular-illative':'ill|s',
        'plural-illative':'ill|p',
        'singular-adessive':'ade|s',
        'plural-adessive':'ade|p',
        'singular-ablative':'abl|s',
        'plural-ablative':'abl|p',
        'singular-allative':'all|s',
        'plural-allative':'all|p',
        'singular-essive':'ess|s',
        'plural-essive':'ess|p',
        'singular-translative':'tra|s',
        'plural-translative':'tra|p',
        'plural-instructive':'ins|p',
        'plural-comitative':'com|p',
        'singular-abessive':'abe|s',
        'plural-abessive':'abe|p'
      };
      //get export
      var exporttext
      exporttext = '== ภาษาฟินแลนด์ ==\n\n=== การออกเสียง ===\n* {{fi-IPA}}\n\n=== คำนาม ===\n{{head|fi|รูปผันคำนาม}}\n\n'
      uniquettc.forEach(function(el){
        var ins = el.slice(8,-16)
        exporttext += '# {{inflection of|'+pagetocreat+'||'+infl[ins]+'|lang=fi}}\n'
      })
      //console.log(exporttext)
      //แล้วทำการสร้างหน้า ยังดำเนินการทำสคริปต์อยู่
      client.api.call({action:'parse',page:ele},function (err) {
        if (err) {
          client.edit(ele,exporttext,'สร้างหน้าคำผันภาษาฟินแลนด์',function (err) {})
        } else {
          console.log('page already exist')
        }
      })
    })
  })
}
client.logIn( function () {
  creat('หน้าที่จะสร้าง')
});
