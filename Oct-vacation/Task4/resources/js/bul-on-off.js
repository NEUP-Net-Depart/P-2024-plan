function changeImage() {
  element=document.getElementById('myimage')
    if (element.src.match("bulbon"))
    {
        element.src="resources/imgs/pic_bulboff.gif";
    }
    else
    {
        element.src="resources/imgs/pic_bulbon.gif";
    }
}
