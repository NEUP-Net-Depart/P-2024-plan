function changeImage() {
  const light = document.getElementById('myimage');
  if(light.src.endsWith('pic_bulboff.gif')){
    light.src = 'pic_bulbon.gif';
}else{
  light.src = 'pic_bulboff.gif';
  }
}
