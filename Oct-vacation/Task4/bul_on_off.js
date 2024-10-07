function changeImage() {
  element = document.getElementById('myimage')
  if (element.src.match("bulbon")) {
    element.src = "pic_bulboff.gif";
  }
  else {
    element.src = "pic_bulbon.gif";
  }
}