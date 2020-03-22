# CSS盒模型

#### 两种盒模型

1. W3C的标准盒模型：

   外盒尺寸（元素空间尺寸）：

   ​	元素空间高度=内容高度+内距+边框+外距

   ​	元素空间宽度=内容宽度+内距+边框+外距

   内盒尺寸（元素大小）：

   ​	元素高度=内容高度+内距+边框（height为内容高度）

   ​	元素宽度=内容宽度+内距+边框（width为内容宽度）

2. IE传统下盒模型：

   外盒尺寸（元素空间尺寸）：

   ​	元素空间高度=内容高度+外距（height包含了元素内容宽度、边框、内距）

   ​	元素空间宽度=内容宽度+外距（width包含了元素的内容宽度、边框、内距）

   内盒尺寸（元素大小）：

   ​	元素高度=内容高度（height包含了元素内容宽度、边框、内距）

   ​	元素宽度=内容宽度（width包含了元素的内容宽度、边框、内距）

   #### box-sizing属性的语法及参数

   **box-sizing: content-box | border-box | inherit**

   - content-box:默认值，让元素维持W3C的标准盒模型。

   - border-box:重新定义，让元素维持IE传统 盒模型。

   - inherit:使元素继承父元素的盒模型形式。

     border-box的使用：

     `-mox-box-sizing: border-box;`

     `-webkit-box-sizing: border-box;`

     `-o-box-sizing: border-box;`

     `-ms-box-sizing: border-box;`

     `-box-sizing: border-box;`

     

     

     

     

   