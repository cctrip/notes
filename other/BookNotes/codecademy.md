# codecademy在线学习

## HTML和CSS学习

### HTML

#### html基本机构
    
    <!DOCTYPE html> //向浏览器声明类型
    <html> //所有的html代码都要包含在该元素内
      <head> //关于网页的信息，如标题
        <title>First Web Page</title>
      </head>
      <body> //可见的html代码内容都放在该元素内
        <p>Hello,World!</p>
      </body>
    </html>

#### 可见内容


* 标题
    
    heading

        <h1>head</h1>
        <h2>
        <h3>
        <h4>
        <h5>
        <h6>

* 段落
    
    paragraph

        <p>content</p>

* 无序列表

    unodered list, list item

        <ul>
          <li>sub</li>
        </ul> 


* 有序列表

    ordered list, list item

        <ol>
          <li>sub</li>
        </ol>

* 链接

    链接, href属性，属性提供更多元素内容的有关信息,在元素的开头标签中，由名称和值组成

        <a href="https://example.com" target="_blank">content</a>

    链接属性: 
    target属性指定链接要在新的浏览器打开.

* 图片

    image

        <img src="https://example.com/example.jpg" alt="example" />

        alt属性: 描述图像信息

* 换行

    line breaks

        aaa?<br/>bbb

* 注释

    <!-- comments -->

***

### CSS

CSS是网页开发人员用来在网页上设计HTML内容的语言.

在html文件中编写css代码

在head元素中加入style元素

        <head>
          <style>
            h2 {
              font-family: Arial;
            }
          </style>
        </head>

在css文件中编写css代码
在html文件链接css文件，放在html文件开头
使用link元素 
    * href属性 css文件地址
    * type属性 描述文件类型
    * rel属性  描述css和html文件的关系

        link href="https://www.codecademy.com/stylesheets/style.css" type="text/css" rel="stylesheet">




