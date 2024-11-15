function changeImage() {
  // TODO
  // 在此处，实现小灯开关的功能！
  element=document.getElementById('myimage')
	if (element.src.match("bulbon"))
	{
		element.src="/resources/imgs/pic_bulboff.gif";
	}
	else
	{
		element.src="/resources/imgs/pic_bulbon.gif";
	}
}
