## CSS3外轮廓属性

**outline: [outline-color] || [outline-style] || [outline-width] || [outline-offset] || [inherit]**

- outline-color：定义轮廓线的颜色，属性为CSS中定义线的样式。省略时此参数的默认值为黑色。

- outline-style：定义轮廓线的样式，属性为CSS中定义线的样式。省略时此参数的默认值为none，省略后不对该轮廓线进行任何绘制。

- outline-width：定义轮廓线的宽度，属性值可以为一个宽度值。省略时此参数的默认值为medium，表示绘制中等宽度的轮廓线。

- outline-offset：定义轮廓边框的偏移位置的数值，此值可以取负数值。当参数的值为正时，表示轮廓边框向外偏移多少个像素；当参数值为负时，表示轮廓边框向内偏移多少个像素。

- inherit：元素继承父元素的outline效果.

  -------

  **outline和border的对比**

  - border属于盒模型的一部分，直接影响元素盒子的大小，而outline创建的外轮廓线是画在一个框的“上面”，不会影响文档流，也不会破坏网页布局。
  - outline创建的外轮廓线在元素各边都一样，不能像border边框一样，设置outline-top或outline-left之类的。
  - border创建的元素边框可以单边设置，而outline创建的外轮廓线始终是闭合的。
  - border创建的外轮廓线可能是非矩形的，如果是多行元素，外轮廓线就至少是能够包含该元素所有框的外轮廓。而norder使用一个边框包括整个元素。
    - border仅可以设置元素的边框，只能向外扩展，而outline创建的外轮廓线可以通过outline-offset的值，向元素外部或内部创建封闭的轮廓。