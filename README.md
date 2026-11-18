# 曾泽璀个人学术主页

纯静态GitHub Pages主页。无需安装前端依赖。中文介绍、响应式布局、论文筛选与搜索、视频播放、专利清单和产业应用关联。

## 本地预览

在本目录运行：

```bash
python3 scripts/build.py
python3 -m http.server 8000
```

打开 http://localhost:8000 。直接打开index.html也可浏览主要内容，但视频最好通过HTTP预览。

## 快速更新

打开 `editor.html` 修改资料，点击下载 `content.json`，用下载的文件替换本目录同名文件。也可直接编辑JSON。

- `profile`：个人简介、公开联系方式（留空不展示）。
- `papers`：论文题名、作者角色、发表状态、领域、结果口径、外部论文链接、视频和图片路径。
- `patents`：名称、专利号、授权公告号、授权日、发明人角色和专利权人，以及image、imageCaption、imageSource和summary。
- `standards`：行业影响力中的标准名称、编号、起草角色、状态、发布日期、技术主题及证据链接。
- `applications`：场景、成熟度、相关论文ID、证据来源与验证边界。
- 视频支持本地MP4、远程MP4和youtube-nocookie.com嵌入地址。添加本地文件后填写相对路径，如`assets/videos/demo.mp4`。
- 修改JSON后运行 `python3 scripts/build.py` 生成content.js和dist；GitHub Actions会自动执行。

编辑页不在dist部署产物中。它不会直接写入GitHub，也不要求输入任何令牌。当前网页不使用访问分析、广告或第三方脚本。

## 发布到GitHub Pages

1. 在你的GitHub账号创建仓库。账号主页可用`你的用户名.github.io`，也支持普通项目仓库。
2. **仅把本目录内容作为仓库根目录上传**，包括`.github/workflows/pages.yml`。不要上传父目录中的简历素材、审稿意见、其他项目和内部资料。
3. 仓库`Settings → Pages → Build and deployment → Source`选择`GitHub Actions`。
4. 将源码提交到`main`，或在Actions中手动执行`Deploy personal homepage`。
5. 成功后从部署任务或Pages设置中取得实际URL。本交付尚未绑定GitHub账号，也没有生成真实在线地址。

若现有仓库默认分支不是main，请相应修改workflow触发分支。所有站内路径均为相对路径，可部署在用户名站点根目录或项目子路径。

部署参考：https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages

## 素材与状态

- EToT本地视频来自用户提供的论文补充材料，转码为1280宽H.264/AAC MP4，约7.5MB，保留完整时长。
- ViTaMIn-B使用本人提供的本地视频转码版（720p H.264/AAC，约4.6MB，完整74秒）；图1由署名论文首页提取，右栏占图文区域的2/5，支持点击放大。原始项目页保留为来源。此前使用的远程视频已替换。DexSim2Real²按作者项目页的YouTube地址嵌入。远程源的可用性取决于作者托管和网络，可通过来源链接回退观看。
- 全部论文统一采用左侧3/5文字、右侧2/5原文方法展示，两栏间距14像素，支持点击放大，手机端上下排列。BRMData展示任务总览，PAO-DP展示原文核心算法；其余展示方法或框架图。来源见content.json中的methodSource及methodCaption。
- 图形封面是研究流程示意，不是实测仿真画面。论文视频和图像另有明确来源。
- 默认展示16项具有署名或公开作者证据的成果。其中Max-Former已核实NeurIPS 2025正式发表；DexSim2Real²通过IEEE提交的Crossref DOI元数据核实T-RO 2025发表；EToT依据本地接收稿；其余为预印本。
- 不将未确认匿名稿、审稿意见、原始专利交底书、来源不明视频加入网页。
- 论文和专利PDF没有整包公开；论文以原始来源链接引用，简历仅提供本人已要求制作的公开介绍版本。
- 全部论文图像、视频和文本的原权利归对应作者与权利人。网站代码和研究素材的权利应分别处理，未套用统一开源许可。

详细成果、视频对应关系及待补充事实见交付目录中的《成果与产业应用整理.md》。

## 专利附图与行业影响力（2026-11-17补充）

- 3项专利均展示原文图1。双足机器人使用CN116252885B授权公告文本；轮足式三栖机器人与解耦双足机器人分别使用同一申请对应的CN115503408A、CN116968843A公开文本附图，图注明确版本。授权信息仍依授权证书展示。
- T/BICA 156—2026：主要起草人署名经本地标准前言与国家标准馆核对。公开目录实施日与本地文本不一致，仅展示一致的发布日期。
- T/NMRJ 139—2026：起草人署名经国家标准馆核对。最新详情页标注废止，页面作为历史标准参与经历展示。
- 标准申请表仅作本地核验；原始表格及其中个人联系方式、身份证号码等不进入网站或发布包。
- 标准信息可在editor.html的“行业影响力 / 标准起草”栏目修改。

## 新增论文（2026-11-17）
新增ForeAct、Kimodo-Policy、DexAC-WM、HumanoidArena、MV-SAM3D、RoboBPP，Dream2Reward合并既有记录，现共16项。新增条目保留用户提供的Scholar链接，主论文链接使用可核验的arXiv地址。RoboBPP按作者项目页IJRR接收公告标注；其余新增项按预印本展示。Kimodo-Policy与RoboBPP嵌入作者托管视频，网络不可用时可通过项目来源链接观看。方法图来源保存在methodSource字段。

## 研究框架介绍
研究方向新增Real2Sim2Real闭环、Agent Harness模块与智能码垛示例。content.json中的researchOverview、researchStages、harnessModules分别控制总述、闭环阶段与编排模块；editor.html提供对应编辑入口。框架定位为已有成果的综合组织与系统集成方向，未宣称统一产品已经部署。
