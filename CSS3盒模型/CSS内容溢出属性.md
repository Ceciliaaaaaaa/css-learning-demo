## CSS内容溢出属性

#### overflow-x和overflow-y属性的语法及参数

overflow-x主要是用来定义对水平方向内容溢出的剪切，而overflow-y主要是用来定义对垂直方向内容溢出的剪切。基本语法如下：

**overflow-x: visible | hidden | scroll | auto | no-display | no-content**

**overflow-y: visible | hidden | scroll | auto | no-display | no-content**

- visible：默认值。表示不剪切容器中的任何内容、不添加滚动条，元素将被剪切为包含对象的窗口大小，而且clip属性设置将失效。
- auto：在需要时剪切内容并添加滚动条。也就是说当内容超过容器的宽度或者高度时，溢出的内容将会隐藏在容器中，并且会添加滚动条，用户可以拖动滚动条查看隐藏在容器中的内容。
- hidden：内容溢出容器时，所有内容都将隐藏，而且不显示滚动条。
- scroll：不管内容有没有溢出容器，overflow-x都会显示横向的滚动条，而overflow-y都会显示纵向的滚动条。
- no-display：当内容溢出容器时不显示元素，此时类似于元素添加了display:none声明一样。
- no-content：当内容溢出容器时不显示内容，此时类似于添加了visibility:hidden声明一样。