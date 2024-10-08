function changeImage() { 

  var imageElement = document.getElementById('bulb');


  var offImagePath = '../resources/imgs/pic_bulboff.gif';
  var onImagePath = '../resources/imgs/pic_bulbon.gif';


  if (imageElement.src.includes(offImagePath.split('/').pop())) { 
      imageElement.src = onImagePath;
  } else {
      imageElement.src = offImagePath;
  }
}
