Title: 图书馆专用Chrome浏览器下载
Tags: Chrome, 浏览器
Authors: 刘东华
Summary: 这篇文章主要提供图书馆专用Chrome浏览器下载
Lang: zh

目前Chrome浏览器基本上是被大众认可的现代高效浏览器，对Web标准支持的较好，相比IE、360等浏览器简洁易用、高效速度快。

由于我们学校图书馆购买的文献数据库都需要从教务网出口出去，目前校内网和运营商合作导致出口不能统一，所以有一些数据库资源之前可以访问，但现在无法访问。由于这些原因，我们信息技术中心定制了绿色版Chrome浏览器，方便大家不需要经过配置就可以自由访问文献数据库。

如果是其他操作系统平台或浏览器，主要有两种配置方式

1. `全局配置`，会影响所有使用全局配置的浏览器，可参考[Windows如何配置使用pac脚本][Windows如何配置使用pac脚本]，最后一步修改自动使用配置脚本的地址为：[https://raw.githubusercontent.com/liudonghua123/ynu_lib_pac/master/proxy.pac](https://raw.githubusercontent.com/liudonghua123/ynu_lib_pac/master/proxy.pac)
2. `浏览器自身设置`，一般需要安装`插件`或`扩展`才支持，例如Firefox浏览器可以配合使用[FoxyProxy Standard][FoxyProxy Standard]扩展，本文制作的绿色版Chrome就是安装配置了`SwitchyOmega`扩展以实现此功能，可参考相关插件的使用说明文档，最重要的就是设置PAC地址为：[https://raw.githubusercontent.com/liudonghua123/ynu_lib_pac/master/proxy.pac](https://raw.githubusercontent.com/liudonghua123/ynu_lib_pac/master/proxy.pac)

附件说明

- [ChromePortable][ChromePortable]，针对Win7及以上操作系统
- [ChromePortableXP][ChromePortableXP]，针对Windows XP操作系统
- [SwitchyOmega][SwitchyOmega]，Chrome的代理扩展
- [FoxyProxy Standard][FoxyProxy Standard]，Firefox的代理扩展

[ChromePortable]: http://resources.ynu.edu.cn/chrome/ChromePortable.zip
[ChromePortableXP]: http://resources.ynu.edu.cn/chrome/ChromePortableXP.zip
[Windows如何配置使用pac脚本]: http://jingyan.baidu.com/article/a948d6511057c20a2dcd2e0d.html
[SwitchyOmega]: https://github.com/FelisCatus/SwitchyOmega
[FoxyProxy Standard]: https://addons.mozilla.org/en-US/firefox/addon/foxyproxy-standard/

