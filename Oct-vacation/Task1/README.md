# Task 1
## 配置完成图片

<img src="./Screenshot 2024-10-06 161436.png" alt="test">

## 遇到的几个问题
### 1.配置mingw
由于之前使用的CLion，而CLion自带的MinGW，我懒得下载新的MinGW，就将其配置在VSCode里面，但是一直不能正常运行(我怀疑是因为**gcc**和**gdb**所在目录不是同一个，环境变量杂乱导致的)，于是按照B站教程[vscode安装配置c/c++教程](https://www.bilibili.com/video/BV1BQ4y1j7fY/?spm_id_from=333.337.search-card.all.click&vd_source=a8c6487c3459ae95573a2371b6fbc23b)重新安装并配置了一下环境变量，成功配置好了C语言环境

### 2.中文乱码
由于调试界面一输出汉字就乱码，我从CSDN得知需要改变编码格式，将UTF-8改为了gbk，解决了问题

@Author: 艾合拉木·阿里木

@Email:2668976818@qq.com
