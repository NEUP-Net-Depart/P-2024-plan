# Task 1

请补充个人信息后，在此完成报告！

@Author: Aoi-tori \\ 胡炜佳
@Email: 2959608864@qq.com

### 1.编辑器 or 编译器
我一开始不知道VScode本身只能算是一个高级的源代码编辑器，而非完整的IDE；后来阅读完教程后才明白想在VScode中实现编译和调试代码需要额外安装插件(如Mingw-w64)，并手动配置环境变量。

### 2.自定义配置与优化
首先打开“运行和调试”面板，点击“创建launch.json”,在顶部栏选择“GDB/LLDB”，点击“添加配置”，选择“c/c++(gdb)启动”，并在tasks.json中找到`${fileDirname}\\${fileBasenameNoExtension}.exe`复制到launch.json中；然后把"externalConsole"改为true，以实现在Windows控制台中运行exe文件。

### 3.编译的逻辑
网络上的说法是：.cpp文件将由launch.json指挥交由tasks.json使用g++编译器编译为.exe文件，然后由launch.json启动此.exe文件在gdb.exe进行调试。实操中，在配置好launch文件点击页面右上角的debug按钮后，就会编译出.exe文件并运行。（其实这里我仍然不是很懂）

### 4. 多个文件间的链接
因为最开始接触cpp使用的是visual studio2022，所以在使用VScode之后我就好奇VScode能否像VS2022一样编译并链接多个文件；然后通过B站了解到，VScode没有自动编译所有文件的功能，需要在launch.json文件中手动设置：可以在`"args"`一栏添加“.c”或“.cpp”，就能实现编译所有文件并合并成一个可执行文件。但是多个文件需要分别编译时，就要在launch.json文件中为每个文件分别添加配置。