// window.onload = getImages;

var faces = [];

var getImages = function(){
  faces = document.getElementsByClassName('img');
  swapImages();
};

var swapImages = function() {
  var random = Math.floor(Math.random() * 215) + 1
  var random_pic = "images/" + random + ".png"
  var newimg = chrome.extension.getURL(random_pic);
  for (var i = 0; i < faces.length; i++) {
    faces[i].src = newimg;
  }
}

var observer = new MutationObserver(function(mutations) {
    mutations.forEach(function(mutation) {
      getImages();
    });
});

var config = {
    attributes: true,
    childList: true,
    characterData: true
};

getImages();
observer.observe(document.body, config);
