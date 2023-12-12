 # 一个简易的验证码识别工具
 
***

作为一个只会挖验证码可识别、用户名遍历这种垃圾洞的底层安服🌞，在换MAC之后发现之前的验证码识别工具只有exe的用不了，花了一个下午手搓了一个出来

<img src="./img/IMG_7938.png">

在mac下支持根据系统设定的外观变化白色和黑色 <del>，我也不知道怎么实现的，应该是PYQT6自带</del>

识别引擎使用[ddddocr](https://github.com/sml2h3/ddddocr)

欢迎使用并指出bug

***

### F&Q
#### 1、运行源代码出现报错
```
AttributeError: module 'PIL.Image' has no attribute 'ANTIALIAS'
```
原因：在pillow的10.0.0版本中，ANTIALIAS方法被删除了

方法一：进入ddddocr的_init_.py，把ANTIALIAS替换为新方法：

```
# image = image.resize((int(image.size[0] * (64 / image.size[1])), 64), Image.ANTIALIAS).convert('L')

image = image.resize((int(image.size[0] * (64 / image.size[1])), 64), Image.LANCZOS).convert('L')
```

方法二：降低pillow版本（不是很推荐）

#### 2、命令行打开，在命令行中有广告
不是我的广告，是ddddocr的，同样在在_init_.py文件中可以修改