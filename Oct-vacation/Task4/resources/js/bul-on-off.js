function changeImage() {
  element=document.getElementById('myimage')
  if (element.src.match("bulbon"))
  {
      element.src="C:/Users/23242/P-2024-plan/Oct-vacation/Task4/resources/imgs/pic_bulboff.gif";
  }
  else
  {
      element.src="C:/Users/23242/P-2024-plan/Oct-vacation/Task4/resources/imgs/pic_bulbon.gif";
  }
}
