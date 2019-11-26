var page = require('webpage').create();

page.open('https://stackoverflow.com/questions/10848900/how-to-take-partial-screenshot-frame-with-selenium-webdriver?noredirect=1&lq=1', function() {
  // being the actual size of the headless browser
  page.viewportSize = { width: 1440, height: 900 };

  var clipRect = page.evaluate(function(){
    return document.querySelector('.answer').getBoundingClientRect();
  });

  page.clipRect = {
    top:    clipRect.top,
    left:   clipRect.left,
    width:  clipRect.width,
    height: clipRect.height
  };

  page.render('google.png');
  phantom.exit();
});