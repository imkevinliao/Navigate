# 科学上网
科学上网途径主要有三种：自建，机场，VPN （这里需要稍微说明一下，真正的 VPN 本质并不能翻墙，因为它会告诉防火墙你要访问哪个网站。而我们叫习惯了也就不再做区分了)

自建机场要求较为严格：
1. 具有理工计算机软件的背景
2. 使用 Linux 时间超过 240 小时
3. 了解 GFW 的发展史
4. 具备自主分析解决问题的能力
5. 最好具有建站经历
# V2ray Or Xray | Bright Future
分支（两大分支）
- 官网(V2ray)：<https://www.v2fly.org/> Github 地址：<https://github.com/v2fly/v2ray-core> 
- 官网( Xray )：<https://xtls.github.io/> Github 地址：<https://github.com/XTLS/Xray-core>

脚本
- https://github.com/Jrohy/multi-v2ray （推荐：自定义类型丰富）
- https://github.com/mack-a/v2ray-agent
- https://github.com/wulabing/V2Ray_ws-tls_bash_onekey
- https://github.com/233boy/v2ray/tree/master （推荐：适合新手小白 【见下面注释】）
注释：由于作者在脚本中私自修改配置文件，禁止了部分网站的访问，个人不太喜欢这种，虽然我本身不访问那些网站（法轮功类），但是我并不喜欢这种干涉他人选择的行为。
不过脚本本身适合小白，而且对大部分人来说，那些网站确实不会访问。尽管从来不访问，但是我仍然拒绝这种禁止我选择权力的脚本。
由于是以前发现的，不清楚现在是否依然封禁，因为自那以后，我就再也不用了。

客户端
- https://github.com/2dust/v2rayN [Windows]
- https://github.com/2dust/v2rayNG [Android]
- https://apps.apple.com/ca/app/shadowrocket/id932747118 [IOS Shadowrocket (美区账号 付费应用)]

# Trojan [正在成为历史]
- <https://github.com/trojan-gfw/trojan> [项目地址]
- <https://github.com/Jrohy/trojan> [脚本-持续维护]
- <https://github.com/atrandys/trojan> [脚本-已经停更]
Trojan 项目主力开发者已经停更很久了，诚然，Trojan 仍然可以使用，但随着主力开发者的退场，已经停滞，不建议使用
# SSR && SS [已经成为历史]
```
SS 算是翻墙鼻祖，作者被请去喝茶后，诞生了 SSR
SS 已经完全可以被 GFW 识别，SSR 基本上可以被 GFW 识别。
额外提一下：仍然有大量使用 SSR 的，原因较为复杂，但安全性非常差，使用 SSR 就约等于，
你告诉 GFW：我在使用科学上网
GFW 告诉你：收到！但是我最近不太想封你，等敏感时期再封吧，哦，心情不好也封一下吧。
```
# BBR [已成历史]
```
wget --no-check-certificate -O tcp.sh https://raw.githubusercontent.com/Mufeiss/Linux-NetSpeed/master/tcp.sh && chmod +x tcp.sh && ./tcp.sh
```
现在的 Linux 都自带了 BBR，只是需要手动开启。千万不要再使用 BBR 这类脚本去安装内核，因为这类脚本都很古老了，安装大概率是反向升级。
# V2ray 摘要
Project V 是项目，V2ray 是该项目的产物（工具）。严格意义上来说，V2ray 只代表内核，不具备翻墙能力，但大家叫习惯了，
所以 V2ray = Project V。Project V 支持许多协议（这些协议正是我们跨过 GFW 的核心）。

VMess VLess 是 V2ray 官方标准协议，其中 vless 是对 vmess 的升级，vmess 成为历史是必然

如果你使用的是 VMess 协议请务必确保服务器时间与你自己的本地时间相同（时区一致）

VMess 协议如果服务端与客户端时间不一致，会导致无法使用！VLess 则改进了这一点（无需时间一致）

无论 VMess 和 VLess 对于 GFW 都属于透明存在，被直接识别

互联网所有开启 HTTPS 的网站，都使用 TLS 加密数据，所以套用 TLS 加密保证安全。

常规方案：（存在一定被识别风险）
1. vless + tcp + tls （推荐）
2. vless + websocket + tls

这里需要指出：被识别绝对不是因为你的 TLS 数据被破解，而是其他的流量特征分析（例如大量流量访问同一个国外IP，显然不正常），或者你的 IP 上一个使用者不正常使用。

总之，绝对不可能是 TLS 的问题，因为如果 TLS 被破译，那么整个互联网都要面临安全问题。

如果担心被识别，可以套 CDN，这样几乎不可能被封禁，但是，速度可能会受到很大影响，我自己是不适用的，因为 IP 被封就换一个好了。

由于社区争议，V2ray 分成了两拨人，一波继续维护 V2ray 内核，另一波开发了 Xray 内核

Xray 是 V2ray 的超集，你可以简单理解为，Xray 兼容 V2ray 但它有更多自己的特性，这些特性 V2ray 不具备，有些翻墙软件并不支持 Xray，不愿意折腾请使用 V2ray。

V2ray 和 Xray 可以比喻成两个党派，V2ray 是保守派，Xray 是激进派。
相比于其他单打独斗的开发者，V2ray 最大的成功就是真正意义上激活了社区，作为 V2ray 最早的见证者，一路走来没有倒下，真是令人惊讶。

Xray 提出了一些新的翻墙解决方案，这些方案理论上来说更为安全，甚至达到了完全欺骗，安全性极高! 对于追求绝对安全的人来讲，必然优先考虑 Xray 而非 V2ray
# 服务器 && 机场 (所有机场都应该考虑风险)
唯云四杰算是顶尖机场，但也不意味着就完全没有跑路风险！只能说相对而言少很多，机场专线，品质最佳，不差钱建议直接买。

衡量一家优质机场的标准：
1. 域名是否以 .com 结尾，以 .com 结尾且域名与机场名相关有一定意义且在 8 个纯英文字母以内的域名（请理解限定条件），年费并不低
2. 机场是否有 IPLC 专线，专线可以绕过防火墙直连，不存在 QoS 限速。有专线，域名必定以 .com 结尾，专线费用更昂贵，正常情况下买得起专线不可能省域名的钱
3. 机场存在年限，年限越长越好
4. 机场网站页面是否是单独开发，中小机场一般是使用机场模板搭建，有实力的机场是单独开发

- <https://duangks.com/> 机场资讯
- <https://nxboom.com/> 唯云四杰之首
- <https://naiyovpn.com/> 唯云四杰之一
- <http://mxwljsq.top/>
- <https://moriyun.vip/>
- <https://www.microcloud.cc/index.php?rp=/store/azure-hk> 
# 其他
- <https://github.com/v2fly/v2ray-examples> [模板 自主搭建会用得上（小白绕道）]
- <https://github.com/txthinking/brook> [科学上网工具-专为开发者]
- <https://github.com/hijkpw/scripts/tree/master> [各类脚本 已停止更新维护]
- <https://github.com/The-Run-Philosophy-Organization/run> [润学]
