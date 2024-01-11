# V2ray Or Xray | Bright Future
分支（两大分支）
- https://github.com/v2fly/v2ray-core [Project V2ray]
- https://github.com/XTLS/Xray-core [Project Xray]
- <https://www.v2fly.org/> V2ray 社区官网 
- <https://xtls.github.io/> Xray 官方网站 [Xray 与 V2ray 理念不合 自立门户] 

脚本
- https://github.com/Jrohy/multi-v2ray [推荐]
- https://github.com/mack-a/v2ray-agent
- https://github.com/233boy/v2ray/tree/master [作者私自在 V2ray 配置文件中禁止部分网站]
- https://github.com/wulabing/V2Ray_ws-tls_bash_onekey 

客户端
- https://github.com/2dust/v2rayN [Windows]
- https://github.com/2dust/v2rayNG [Android]
- https://apps.apple.com/ca/app/shadowrocket/id932747118 [Shadowrocket (美区账号 付费应用)]
- <https://github.com/v2fly/v2ray-examples> [模板 自主搭建会用得上（小白绕道）]
```
v2ray 摘要

Project V 是项目，v2ray 是该项目的产物（工具）。严格意义上来说，v2ray 只代表内核，但大家叫习惯了，
所以 v2ray = Project V。Project V 支持许多协议（这些协议正是我们跨过 gfw 的核心）

vmess vless 是 v2ray 官方标准协议，其中 vless 是对 vmess 的升级，vmess 成为历史是必然

vless 与 vmess 对于用户而言就是 vless 协议不需要服务器和本地时间一致，
而 vmess 协议如果时间不同步会导致客户端和服务端无法正常使用，这个问题在早期令许多搭建者头疼（例如你的服务器在美国）

vmess 和 vless 对于 gfw 属于透明存在，所以通常套 tls 使用，互联网大部分流量都是 tls 也就是使用 https 流量的网站。

请不要裸 vless 使用，至少套上 tls 走 443 端口，虽然 gfw 有一定能力可以识别，但裸 vless 则是百分百识别。

常规方案：（存在一定被识别风险）
1. vless + tcp + tls
2. vless + websocket + tls

怕死就再套 cdn ，套了 cdn 几乎不可能被封禁，但也有其他问题

v2ray 由于社区争议导致，v2ray 分成了两拨人，一波继续维护 v2ray 内核，另一波开发了 xray 内核

xray 是 v2ray 的超集，你可以简单理解为，xray 兼容 v2ray 但它有更多的特性，这些特性 v2ray 不具备

v2ray 和 xray 更像是一个是保守派，一个是激进派。相比于其他单打独斗的开发者，
v2ray 最大的成功就是真正意义上激活了社区，作为 v2ray 最早的见证者，一路走来没有倒下，真是令人惊讶

xray 的一些解决方案理论上来说更为安全，甚至达到了完全欺骗，安全性极高，但更新什么的太快了，要不断学习

对于一个工具而言，需要不断学习，那成本太高了，就让那些狂热者去做吧，一般选择 v2ray + vless + tcp + tls 足以

被封了就换个 ip 的事情，问题不大
```


# trojan
trojan 项目：<https://github.com/trojan-gfw/trojan>

trojan 项目主力开发者已经停更很久了，诚然，trojan 虽然完全可以使用，但随着主力开发者的退场，基本停滞，相比之下，v2ray 社区的活跃显得难能可贵

- <https://github.com/Jrohy/trojan> [持续维护]
- <https://github.com/atrandys/trojan> [已经停更]

# BBR 
```wget --no-check-certificate -O tcp.sh https://raw.githubusercontent.com/Mufeiss/Linux-NetSpeed/master/tcp.sh && chmod +x tcp.sh && ./tcp.sh```

已成历史，只作为了解，现在的 Linux 发行版本都已经自带了，无需额外安装

# 服务器 && 机场
服务器
- <https://www.microcloud.cc/index.php?rp=/store/azure-hk> [注意识别风险]
- <https://liwt31.github.io/2018/01/09/lightsail/> [aws lightsail (aws 全球云服务器的老大 唯一的风险就是你不了解计费规则导致天价账单 节点选日本或者新加坡其他不推荐)]

aws lightsail 额外脚本 

用户 kevin 密码 123456 登录后请一定重置密码（passwd kevin) 或者配置完后删除 kevin 用户

删除命令 userdel -r kevin
```
sudo useradd kevin -m -s /bin/bash
echo 'kevin:123456' | sudo chpasswd
sudo sed -i '52c PasswordAuthentication yes' /etc/ssh/sshd_config
sudo service sshd restart
sudo sed -i '20a kevin    ALL=(ALL:ALL) NOPASSWD:ALL' /etc/sudoers
sudo apt install vnstat
```
aws lightsail 超流量自动关机 参考网址：
- https://fmk.im/p/shutdown-aws/
- https://zset.cc/archives/25/
```
请使用root账户操作

apt install vnstat

vim /root/auto-shutdown.sh

#!/bin/bash
TRAFF_TOTAL=950 #流量额度，单位 GB。
TRAFF_USED=$(vnstat --oneline b | awk -F';' '{print $11}')
CHANGE_TO_GB=$(expr $TRAFF_USED / 1073741824)

if [ $CHANGE_TO_GB -gt $TRAFF_TOTAL ]; then
    shutdown -h now
fi

crontab -e
*/5 * * * * /root/auto-shutdown.sh > /dev/null 2>&1

附带：
时区时间校准： timedatectl set-timezone Asia/Shanghai    
定时任务测试：https://crontab.guru/
vnstat -d 查看每日流量
vnstat -m 查看每月流量
vnstat 配置文件 /etc/vnstat.conf 这里面默认每月 1 号开始统计所以不用担心脚本问题，可以自己看一眼确认
```

机场资讯 - <https://duangks.com/>

唯云四杰算是顶尖机场，但也不意味着就完全没有跑路风险

衡量一家优质机场的标准：
1. 域名是否以 .com 结尾，以 .com 结尾且域名与机场名相关有一定意义且在 8 个纯英文字母以内的域名（请理解限定条件），年费并不低
2. 机场是否有 IPLC 专线，专线可以绕过防火墙直连，不存在 QoS 限速。有专线，域名必定以 .com 结尾，专线费用更昂贵，正常情况下买得起专线不可能省域名的钱
3. 机场存在年限，年限越长越好
4. 机场网站页面是否是单独开发，中小机场一般是使用机场模板搭建，有实力的机场是单独开发

唯云四杰
- <https://nxboom.com/> 唯云四杰之首
- <https://naiyovpn.com/> 唯云四杰之一

注意识别跑路风险
- <http://mxwljsq.top/>
- <https://moriyun.vip/>

# 其他
- <https://github.com/txthinking/brook> [科学上网工具-专为开发者]
- <https://github.com/hijkpw/scripts/tree/master> [各类脚本 已停止更新维护]
# 彩蛋
- <https://github.com/The-Run-Philosophy-Organization/run> [润学]
