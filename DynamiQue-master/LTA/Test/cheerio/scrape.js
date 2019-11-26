const request = require('request');
const cheerio = require('cheerio');


let url = 'https://stackoverflow.com/search?q=dev';
request(url,(error,response,html)=>{
  let $ = cheerio.load(html);
  $('.question-summary search-result').each((i,element)=>{
    let omg = $(element).text();
    console.log(omg);
  });
});