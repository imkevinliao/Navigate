# V2ray 不止于 V2ray
分支（两大分支）
- https://github.com/v2fly/v2ray-core [社区版]
- https://github.com/XTLS/Xray-core [因社区理念争议而生]

V2ray 社区官网 <https://www.v2fly.org/>

脚本
- https://github.com/Jrohy/multi-v2ray [推荐]
- https://github.com/mack-a/v2ray-agent
- https://github.com/233boy/v2ray/tree/master [作者私自在 V2ray 配置文件中禁止部分网站]
- https://github.com/wulabing/V2Ray_ws-tls_bash_onekey 

客户端
- https://github.com/2dust/v2rayN [Windows]
- https://github.com/2dust/v2rayNG [Android]
- https://apps.apple.com/ca/app/shadowrocket/id932747118 [Shadowrocket (美区账号 付费应用)]

模板 <https://github.com/v2fly/v2ray-examples> 自主搭建会用得上（小白绕道）

# trojan
trojan 项目：<https://github.com/trojan-gfw/trojan>

trojan 项目主力开发者已经停更很久了，诚然，trojan 虽然完全可以使用，但随着主力开发者的退场，基本停滞，相比之下，v2ray 社区的活跃显得难能可贵

- <https://github.com/Jrohy/trojan> [持续维护]
- <https://github.com/atrandys/trojan> [已经停更]


# BBR 
使用原生 BBR 加速就好，魔改锐速之类的建议慎用

```wget --no-check-certificate -O tcp.sh https://raw.githubusercontent.com/Mufeiss/Linux-NetSpeed/master/tcp.sh && chmod +x tcp.sh && ./tcp.sh```

# 服务器 && 机场
服务器
- <https://www.microcloud.cc/index.php?rp=/store/azure-hk> [注意识别风险]
- <https://liwt31.github.io/2018/01/09/lightsail/> [aws lightsail (aws 全球云服务器的老大 唯一的风险就是你不了解计费规则导致天价账单 节点选日本或者新加坡其他不推荐)]

aws lightsail 额外脚本 用户 kevin 密码 123456 登录后请一定重置密码（passwd kevin) 或者配置完后删除 kevin 用户
```
sudo useradd kevin -m -s /bin/bash
echo 'kevin:123456' | sudo chpasswd
sudo sed -i '52c PasswordAuthentication yes' /etc/ssh/sshd_config
sudo service sshd restart
sudo sed -i '20a kevin    ALL=(ALL:ALL) NOPASSWD:ALL' /etc/sudoers
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
- <https://mxwljsq.top/>
- <https://moriyun.vip/>

# 其他
- <https://github.com/txthinking/brook> [科学上网工具-专为开发者]
- <https://github.com/hijkpw/scripts/tree/master> [各类脚本 已停止更新维护]
