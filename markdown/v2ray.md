# 科学上网
跨越长城

# V2ray Or Xray | Bright Future
分支（两大分支）
- 官网(V2ray)：<https://www.v2fly.org/> Github 地址：<https://github.com/v2fly/v2ray-core> 
- 官网( Xray )：<https://xtls.github.io/> Github 地址：<https://github.com/XTLS/Xray-core>

## 脚本
- https://github.com/Jrohy/multi-v2ray （自定义丰富）
- https://github.com/mack-a/v2ray-agent （推荐）
- https://github.com/wulabing/V2Ray_ws-tls_bash_onekey
- https://github.com/233boy/v2ray/tree/master （推荐：适合新手小白 ）
- https://github.com/wulabing/Xray_onekey

## 客户端
- https://github.com/2dust/v2rayN [Windows]
- https://github.com/2dust/v2rayNG [Android]
- https://apps.apple.com/ca/app/shadowrocket/id932747118 [IOS Shadowrocket (美区账号 付费应用)]

# Trojan [正在成为历史]
- <https://github.com/trojan-gfw/trojan> [项目地址]
- <https://github.com/Jrohy/trojan> [脚本-持续维护]
- <https://github.com/atrandys/trojan> [脚本-已经停更]
Trojan 项目主力开发者已经停更很久了，诚然，Trojan 仍然可以使用，但随着主力开发者的退场，已经停滞，不建议使用
# SSR && SS [已经成为历史]

# BBR
```
wget --no-check-certificate -O tcp.sh https://raw.githubusercontent.com/Mufeiss/Linux-NetSpeed/master/tcp.sh && chmod +x tcp.sh && ./tcp.sh
```
现在的 Linux 都自带了 BBR，只是需要手动开启，如果是脚本也只需要开启，不要安装内核。

# X-UI 面板
注意不要使用 http 裸奔（安装面板后第一时间 启用https域名访问）

- X-UI 科学上网 https://github.com/vaxilu/x-ui
- X-UI 继任者(3x-ui) https://github.com/MHSanaei/3x-ui
- X-UI 继任者(x-ui) https://github.com/qist/xray-ui 

# 流媒体
- 流媒体检测 https://github.com/lmc999/RegionRestrictionCheck.git
- warp 解锁流媒体 https://github.com/yonggekkk/warp-yg.git
```shell
bash <(curl -L -s check.unlock.media)
```
# IP质量检测
- https://github.com/xykt/IPQuality
```shell
bash <(curl -sL IP.Check.Place)
```

# 路由检测
- https://github.com/zhanghanyun/backtrace
- https://github.com/nxtrace/NTrace-core?tab=readme-ov-file
```shell
curl nxtrace.org/nt | bash
# 本地测试：nexttrace --table ip[服务器ip地址]
# 服务器测试回程路由：nexttrace --fast-trace
```
```shell
curl https://raw.githubusercontent.com/zhanghanyun/backtrace/main/install.sh -sSf | sh
```

# 服务器测速
- https://github.com/spiritLHLS/ecs  (推荐 融合怪)
- https://github.com/i-abc/Speedtest
```shell
bash <(wget -qO- bash.spiritlhl.net/ecs)
```
```shell
bash <(curl -sL bash.icu/speedtest)
```
```shell
bash <(curl -Lso- https://bench.im/hyperspeed)
```
## 测速说明
对于单个用户，服务器单线程测速才有实际意义，多线程实际上没有用，科学上网之类的看的是单线程

# 服务器 && 机场 (所有机场都应该考虑风险)
唯云四杰算是顶尖机场，但也不意味着就完全没有跑路风险！只能说相对而言少很多，机场专线，品质最佳，不差钱建议直接买。

衡量一家优质机场的标准：
1. 域名是否以 .com 结尾，以 .com 结尾且域名与机场名相关有一定意义且在 8 个纯英文字母以内的域名（请理解限定条件），年费并不低。垃圾域名年费也就几十块钱，随时跑路。
2. 机场是否有 IPLC 专线，专线可以绕过防火墙直连，不存在 QoS 限速。有专线，域名必定以 .com 结尾，专线费用更昂贵，正常情况下买得起专线不可能省域名的钱
3. 机场存在年限，年限越长越好
4. 机场网站页面是否是单独开发，中小机场一般是使用机场模板搭建，有实力的机场是单独开发

# 其他
- <https://github.com/v2fly/v2ray-examples> [模板 自主搭建会用得上（小白绕道）]
- <https://github.com/txthinking/brook> [科学上网工具-专为开发者]
- <https://github.com/hijkpw/scripts/tree/master> [各类脚本 已停止更新维护]
- <https://github.com/The-Run-Philosophy-Organization/run> [润学]
