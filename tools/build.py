#!/usr/bin/env python3
"""Generates the Zipper intro page (ko default at /, en/zh/ja in subfolders)."""
import html, json, os, sys

ROOT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
OUT = os.path.join(ROOT, "docs")
GITHUB_USER = "jayusop"
REPO = "Zipper"
SITE = f"https://{GITHUB_USER}.github.io/{REPO}/"
REPO_URL = f"https://github.com/{GITHUB_USER}/{REPO}"
DOWNLOAD = f"{REPO_URL}/releases/latest"
VERSION = "0.1.0"

WRITE = ["ZIP", "7Z", "TAR", "TGZ", "TBZ", "TXZ", "GZ"]
READ = ["RAR / RAR5", "EGG", "ALZ", "ISO", "UDF", "BIN", "IMG (FAT)", "CAB", "MSI", "LZH / LHA",
        "ARJ", "ACE", "ARC", "ZOO", "HA", "BZ2", "XZ", "ZST", "LZMA", "LZ", "Z", "AES",
        "TZST", "TLZ", "TAZ", "EXE (SFX)", "JAR / APK / IPA / EPUB"]

LANGS = ["ko", "en", "zh", "ja"]
NATIVE = {"ko": "한국어", "en": "English", "zh": "中文", "ja": "日本語"}
HTML_LANG = {"ko": "ko", "en": "en", "zh": "zh-Hans", "ja": "ja"}
OG_LOCALE = {"ko": "ko_KR", "en": "en_US", "zh": "zh_CN", "ja": "ja_JP"}

T = {
"ko": dict(
  title="Zipper — Mac용 무료 압축 프로그램 (ZIP·7Z·RAR·EGG·ALZ 지원)",
  desc="Zipper는 macOS용 무료 압축·해제 프로그램입니다. ZIP, 7Z, TAR를 만들고 RAR, EGG, ALZ, ISO 등 30여 가지 형식을 풉니다. 한글 파일명 깨짐 없이 Windows와 주고받을 수 있습니다.",
  keywords="맥 압축 프로그램, Mac 압축 해제, 알집 맥, EGG 압축 풀기 맥, ALZ 맥, RAR 맥, 7z 맥, 한글 파일명 깨짐, Zipper",
  nav=["기능", "지원 형식", "설치", "자주 묻는 질문"],
  h1='Mac에서 압축은<br><span class="accent">Zipper</span> 하나로',
  lead="ZIP·7Z를 만들고, RAR·EGG·ALZ까지 그대로 풉니다. 한글 파일명이 깨지지 않아 Windows 사용자와 주고받기에도 걱정 없습니다.",
  dl="무료 다운로드", gh="GitHub에서 보기",
  meta=f"버전 {VERSION} · macOS 12 Monterey 이상 · Apple Silicon / Intel",
  f_h="주요 기능", f_sub="자주 쓰는 일은 한 번의 클릭으로, 세세한 설정은 필요할 때만.",
  features=[
    ("🗜️", "만들고 풀고 편집하기", "ZIP, 7Z, TAR, GZ 압축 파일을 만들고 풉니다. ZIP은 풀지 않고도 파일 추가·삭제·이름 바꾸기가 가능합니다."),
    ("📂", "30여 가지 형식 열기", "RAR, EGG, ALZ, ISO, CAB, LZH 등 오래된 형식과 국내 형식까지, 받은 압축 파일을 대부분 바로 엽니다."),
    ("🇰🇷", "한글 파일명 깨짐 방지", "Mac의 분리된 자모(NFD)를 합쳐서(NFC) 저장하고, CP949 등 코드페이지를 자동 감지해 Windows 압축 파일도 올바르게 보여줍니다."),
    ("🔒", "AES-256 암호화", "ZIP과 7Z에 AES-256 암호를 걸 수 있고, 7Z는 파일 이름까지 숨길 수 있습니다. 암호화된 EGG(AES/LEA)·ALZ도 풉니다."),
    ("✨", "스마트 풀기", "내용이 한 폴더에 들어 있으면 그 자리에, 아니면 압축 파일 이름의 새 폴더에 풀어 파일이 흩어지지 않습니다."),
    ("✂️", "분할 압축", "메일 첨부(25MB), CD, DVD, FAT32(4GB) 등 원하는 크기로 나눠 압축하고, 분할된 파일도 그대로 엽니다."),
    ("🧪", "무결성 테스트 · 체크섬", "압축 파일이 손상되지 않았는지 테스트하고, 어떤 파일이든 CRC32·MD5·SHA-1·SHA-256 값을 확인합니다."),
    ("🧹", "깔끔한 압축", ".DS_Store, __MACOSX, 리소스 포크 같은 Mac 전용 파일을 빼고 압축해 Windows에서도 깔끔하게 보입니다."),
    ("🌐", "4개 언어 · 다크 모드", "한국어, 영어, 중국어, 일본어를 지원하며 시스템 언어를 따릅니다. 라이트/다크 테마를 고를 수 있습니다."),
  ],
  s_cap="시작 화면 — 압축 파일 열기, 바로 압축하기, 도움말을 한곳에서",
  fm_h="지원 형식", fm_sub="만들기와 풀기를 모두 지원하는 형식, 열고 풀 수 있는 형식으로 나뉩니다.",
  fm_w="만들기 · 풀기 · 테스트", fm_r="열기 · 풀기 · 테스트",
  fm_note="ZIP 파일은 압축을 풀지 않고 바로 편집할 수 있습니다. 분할 압축(.001, .z01, .a00, .vol1.egg, RAR 볼륨)과 EXE 자동 풀림 파일 안의 ZIP/7Z/RAR/ALZ/EGG도 열 수 있습니다.",
  in_h="설치 방법", in_sub="다운로드한 앱을 응용 프로그램 폴더로 옮기기만 하면 됩니다.",
  req=["macOS 12 이상", "Apple Silicon · Intel 유니버설", "무료"],
  steps=[
    ("다운로드", f'<a href="{DOWNLOAD}">GitHub 릴리스 페이지</a>에서 최신 <code>Zipper.app.zip</code>을 내려받아 압축을 풉니다.'),
    ("응용 프로그램 폴더로 옮기기", "<code>Zipper.app</code>을 <code>응용 프로그램</code> 폴더로 드래그합니다."),
    ("처음 한 번 열기", "Apple 공증을 받지 않은 개인 배포 앱이라 처음 열 때 보안 경고가 뜹니다. <strong>휴지통으로 이동</strong>은 누르지 말고 <strong>완료</strong>(macOS 14 이하는 <strong>취소</strong>)로 닫은 뒤, <code>시스템 설정 → 개인정보 보호 및 보안</code> 아래쪽의 <strong>그래도 열기</strong>를 클릭하세요."),
  ],
  term="터미널을 쓴다면 다음 명령 한 줄로도 됩니다.",
  faq_h="자주 묻는 질문",
  faq=[
    ("정말 무료인가요?", "네. 개인과 회사 모두 무료로 사용할 수 있습니다."),
    ("알집(ALZ), EGG 파일도 풀 수 있나요?", "네. 분할된 ALZ(.a00, .a01…), 암호가 걸린 파일, EGG의 AES/LEA 암호화·솔리드·분할 압축도 풉니다. ALZ와 EGG는 만들기는 지원하지 않습니다."),
    ("Windows에서 압축을 풀면 한글 이름이 깨지지 않나요?", "Zipper는 파일 이름을 Windows가 읽는 방식(NFC, UTF-8 표시)으로 저장하므로 Windows 탐색기에서도 한글 이름이 정상으로 보입니다."),
    ("RAR 파일을 만들 수 있나요?", "RAR는 열고 풀기만 지원합니다. 만들 때는 ZIP이나 7Z를 사용하세요."),
    ("인터넷에 연결하거나 파일을 어딘가로 보내나요?", "아니요. 모든 작업은 Mac 안에서만 이루어집니다."),
    ("언어는 어떻게 바꾸나요?", "기본은 시스템 언어를 따릅니다. 환경설정 → 일반 → 언어에서 바꾸면 바로 적용됩니다."),
  ],
  oss="Zipper에는 오픈 소스 소프트웨어가 포함되어 있습니다. 라이센스 고지는 앱의 환경설정 → 라이센스에서 볼 수 있습니다.",
  issues="문제 신고", releases="릴리스",
),
"en": dict(
  title="Zipper — Free archive utility for Mac (ZIP, 7Z, RAR, EGG, ALZ)",
  desc="Zipper is a free archive utility for macOS. Create ZIP, 7Z and TAR archives and extract RAR, EGG, ALZ, ISO and 30+ other formats, with file names that stay intact on Windows.",
  keywords="mac archive utility, unzip mac, rar mac, 7z mac, egg mac, alz mac, free zip app mac, Zipper",
  nav=["Features", "Formats", "Install", "FAQ"],
  h1='Every archive on your Mac,<br>handled by <span class="accent">Zipper</span>',
  lead="Create ZIP and 7Z, open RAR, EGG, ALZ and more. File names stay intact, so archives you share with Windows users just work.",
  dl="Download free", gh="View on GitHub",
  meta=f"Version {VERSION} · macOS 12 Monterey or later · Apple Silicon / Intel",
  f_h="Features", f_sub="Everyday tasks in one click; detailed settings only when you need them.",
  features=[
    ("🗜️", "Create, extract, edit", "Create and extract ZIP, 7Z, TAR and GZ archives. Add, delete and rename files inside a ZIP without unpacking it."),
    ("📂", "Opens 30+ formats", "RAR, EGG, ALZ, ISO, CAB, LZH and many legacy formats — most archives you receive open right away."),
    ("🔤", "No garbled file names", "Names are stored in composed Unicode (NFC) and code pages such as CP949 or Shift-JIS are detected automatically, so Windows archives read correctly."),
    ("🔒", "AES-256 encryption", "Protect ZIP and 7Z archives with AES-256; 7Z can hide file names too. Encrypted EGG (AES/LEA) and ALZ archives extract as well."),
    ("✨", "Smart extract", "If everything sits in one folder it is extracted in place; otherwise a folder named after the archive is created, so files never spill out."),
    ("✂️", "Split archives", "Split into parts for e-mail (25 MB), CD, DVD or FAT32 (4 GB), and open multi-part archives directly."),
    ("🧪", "Test & checksums", "Verify an archive is intact, and see CRC32, MD5, SHA-1 and SHA-256 of any file."),
    ("🧹", "Clean archives", "Leaves out .DS_Store, __MACOSX and resource forks, so your archives look tidy on Windows."),
    ("🌐", "4 languages · Dark mode", "Korean, English, Chinese and Japanese, following your system language. Light and dark themes."),
  ],
  s_cap="Start screen — open an archive, compress in one click, and quick help",
  fm_h="Supported formats", fm_sub="Formats Zipper can create, and formats it can open and extract.",
  fm_w="Create · Extract · Test", fm_r="Open · Extract · Test",
  fm_note="ZIP archives can be edited in place. Split archives (.001, .z01, .a00, .vol1.egg, RAR volumes) and ZIP/7Z/RAR/ALZ/EGG inside EXE self-extractors also open.",
  in_h="Installation", in_sub="Just move the app into your Applications folder.",
  req=["macOS 12 or later", "Universal: Apple Silicon · Intel", "Free"],
  steps=[
    ("Download", f'Get the latest <code>Zipper.app.zip</code> from the <a href="{DOWNLOAD}">GitHub Releases page</a> and unzip it.'),
    ("Move to Applications", "Drag <code>Zipper.app</code> into the <code>Applications</code> folder."),
    ("Open it the first time", "Zipper is an independently distributed app that is not notarized by Apple, so macOS shows a warning the first time. Don't click <strong>Move to Trash</strong> — close it with <strong>Done</strong> (<strong>Cancel</strong> on macOS 14 and earlier), then click <strong>Open Anyway</strong> at the bottom of <code>System Settings → Privacy &amp; Security</code>."),
  ],
  term="If you prefer Terminal, this one line does the same:",
  faq_h="FAQ",
  faq=[
    ("Is it really free?", "Yes. Free for personal and business use."),
    ("Can it extract ALZ and EGG archives?", "Yes — including split ALZ (.a00, .a01…), password-protected files, and EGG with AES/LEA encryption, solid mode and volumes. Creating ALZ or EGG is not supported."),
    ("Will file names break when extracted on Windows?", "No. Zipper stores names the way Windows expects (NFC with the UTF-8 flag), so they display correctly in File Explorer."),
    ("Can it create RAR archives?", "RAR is open and extract only. Use ZIP or 7Z to create archives."),
    ("Does it connect to the internet or upload my files?", "No. Everything happens on your Mac."),
    ("How do I change the language?", "It follows your system language by default. Change it in Preferences → General → Language; it applies immediately."),
  ],
  oss="Zipper includes open-source software. License notices are shown in the app under Preferences → Licenses.",
  issues="Report an issue", releases="Releases",
),
"zh": dict(
  title="Zipper — 免费的 Mac 压缩软件（支持 ZIP、7Z、RAR、EGG、ALZ）",
  desc="Zipper 是一款免费的 macOS 压缩/解压软件。可创建 ZIP、7Z、TAR，并解压 RAR、EGG、ALZ、ISO 等 30 多种格式，文件名在 Windows 上也不会乱码。",
  keywords="Mac 压缩软件, Mac 解压, Mac RAR, Mac 7z, 文件名乱码, 免费 解压 Mac, Zipper",
  nav=["功能", "支持格式", "安装", "常见问题"],
  h1='Mac 上的压缩与解压，<br>交给 <span class="accent">Zipper</span>',
  lead="创建 ZIP 和 7Z，打开 RAR、EGG、ALZ 等格式。文件名不会乱码，与 Windows 用户互传也毫无顾虑。",
  dl="免费下载", gh="在 GitHub 上查看",
  meta=f"版本 {VERSION} · macOS 12 Monterey 或更高版本 · Apple Silicon / Intel",
  f_h="主要功能", f_sub="常用操作一键完成，详细设置按需使用。",
  features=[
    ("🗜️", "创建、解压与编辑", "创建和解压 ZIP、7Z、TAR、GZ 压缩文件。无需解压即可在 ZIP 中添加、删除和重命名文件。"),
    ("📂", "支持 30 多种格式", "RAR、EGG、ALZ、ISO、CAB、LZH 以及许多旧格式，收到的压缩文件大多可以直接打开。"),
    ("🔤", "文件名不乱码", "文件名以合成形式（NFC）保存，并自动识别 GBK、CP949、Shift-JIS 等代码页，Windows 压缩文件也能正确显示。"),
    ("🔒", "AES-256 加密", "可为 ZIP 和 7Z 设置 AES-256 密码，7Z 还能隐藏文件名。也可解压加密的 EGG（AES/LEA）和 ALZ。"),
    ("✨", "智能解压", "如果内容都在一个文件夹内则就地解压，否则先创建以压缩文件命名的文件夹，避免文件散落。"),
    ("✂️", "分卷压缩", "可按邮件附件（25MB）、CD、DVD、FAT32（4GB）等大小分卷，分卷文件也能直接打开。"),
    ("🧪", "完整性测试与校验和", "检测压缩文件是否损坏，并查看任意文件的 CRC32、MD5、SHA-1、SHA-256。"),
    ("🧹", "干净的压缩包", "自动排除 .DS_Store、__MACOSX 和资源分支，压缩包在 Windows 上也干净整洁。"),
    ("🌐", "4 种语言 · 深色模式", "支持韩语、英语、中文和日语，默认跟随系统语言。可选浅色/深色主题。"),
  ],
  s_cap="开始界面 — 打开压缩文件、一键压缩和帮助集中在一处",
  fm_h="支持格式", fm_sub="分为可创建的格式和可打开、解压的格式。",
  fm_w="创建 · 解压 · 测试", fm_r="打开 · 解压 · 测试",
  fm_note="ZIP 文件可直接编辑而无需解压。也可打开分卷压缩（.001、.z01、.a00、.vol1.egg、RAR 分卷）以及 EXE 自解压文件中的 ZIP/7Z/RAR/ALZ/EGG。",
  in_h="安装方法", in_sub="只需将应用移到“应用程序”文件夹。",
  req=["macOS 12 或更高版本", "通用版：Apple Silicon · Intel", "免费"],
  steps=[
    ("下载", f'从 <a href="{DOWNLOAD}">GitHub Releases 页面</a>下载最新的 <code>Zipper.app.zip</code> 并解压。'),
    ("移到“应用程序”", "将 <code>Zipper.app</code> 拖到“应用程序”文件夹。"),
    ("首次打开", "这是未经 Apple 公证的个人发布应用，首次打开时会出现安全提示。请不要点按 <strong>移到废纸篓</strong>，点按 <strong>完成</strong>（macOS 14 及更早版本为 <strong>取消</strong>）关闭，然后在 <code>系统设置 → 隐私与安全性</code> 底部点按 <strong>仍要打开</strong>。"),
  ],
  term="如果使用终端，也可以运行这一行命令：",
  faq_h="常见问题",
  faq=[
    ("真的免费吗？", "是的。个人和企业均可免费使用。"),
    ("能解压 ALZ 和 EGG 吗？", "可以，包括分卷 ALZ（.a00、.a01…）、加密文件，以及采用 AES/LEA 加密、固实压缩和分卷的 EGG。不支持创建 ALZ 或 EGG。"),
    ("在 Windows 上解压时文件名会乱码吗？", "不会。Zipper 按 Windows 期望的方式（NFC 并带 UTF-8 标志）保存文件名，在文件资源管理器中可正确显示。"),
    ("能创建 RAR 吗？", "RAR 仅支持打开和解压。创建时请使用 ZIP 或 7Z。"),
    ("会联网或上传我的文件吗？", "不会。所有操作都在你的 Mac 上完成。"),
    ("如何切换语言？", "默认跟随系统语言。可在 偏好设置 → 通用 → 语言 中更改，立即生效。"),
  ],
  oss="Zipper 包含开源软件。许可证声明可在应用的 偏好设置 → 许可证 中查看。",
  issues="报告问题", releases="版本发布",
),
"ja": dict(
  title="Zipper — Mac 用の無料圧縮・解凍ソフト（ZIP・7Z・RAR・EGG・ALZ 対応）",
  desc="Zipper は macOS 用の無料圧縮・解凍ソフトです。ZIP、7Z、TAR を作成し、RAR、EGG、ALZ、ISO など 30 以上の形式を展開できます。Windows でもファイル名が文字化けしません。",
  keywords="Mac 圧縮 ソフト, Mac 解凍, Mac RAR, Mac 7z, 文字化け, 無料 解凍 Mac, Zipper",
  nav=["機能", "対応形式", "インストール", "よくある質問"],
  h1='Mac の圧縮・解凍は<br><span class="accent">Zipper</span> ひとつで',
  lead="ZIP・7Z を作成し、RAR・EGG・ALZ などもそのまま展開。ファイル名が文字化けしないので、Windows ユーザーとのやり取りも安心です。",
  dl="無料ダウンロード", gh="GitHub で見る",
  meta=f"バージョン {VERSION} · macOS 12 Monterey 以降 · Apple Silicon / Intel",
  f_h="主な機能", f_sub="よく使う操作はワンクリックで、細かい設定は必要なときだけ。",
  features=[
    ("🗜️", "作成・展開・編集", "ZIP、7Z、TAR、GZ アーカイブを作成・展開できます。ZIP は展開せずにファイルの追加・削除・名前変更ができます。"),
    ("📂", "30 以上の形式に対応", "RAR、EGG、ALZ、ISO、CAB、LZH など古い形式まで、受け取ったアーカイブのほとんどをすぐに開けます。"),
    ("🔤", "文字化けしないファイル名", "ファイル名を合成済み Unicode（NFC）で保存し、Shift-JIS や CP949 などのコードページを自動検出。Windows のアーカイブも正しく表示します。"),
    ("🔒", "AES-256 暗号化", "ZIP と 7Z に AES-256 のパスワードを設定でき、7Z ではファイル名も隠せます。暗号化された EGG（AES/LEA）や ALZ も展開できます。"),
    ("✨", "スマート展開", "中身が 1 つのフォルダに入っていればその場に、そうでなければアーカイブ名のフォルダを作って展開するので、ファイルが散らばりません。"),
    ("✂️", "分割圧縮", "メール添付（25MB）、CD、DVD、FAT32（4GB）など好きなサイズで分割でき、分割ファイルもそのまま開けます。"),
    ("🧪", "テストとチェックサム", "アーカイブの破損をテストし、任意のファイルの CRC32・MD5・SHA-1・SHA-256 を確認できます。"),
    ("🧹", "きれいなアーカイブ", ".DS_Store、__MACOSX、リソースフォークを除いて圧縮するので、Windows でもすっきり表示されます。"),
    ("🌐", "4 言語・ダークモード", "日本語、英語、韓国語、中国語に対応し、システムの言語に従います。ライト／ダークテーマを選べます。"),
  ],
  s_cap="スタート画面 — アーカイブを開く、ワンクリック圧縮、ヘルプをひとまとめに",
  fm_h="対応形式", fm_sub="作成できる形式と、開いて展開できる形式があります。",
  fm_w="作成・展開・テスト", fm_r="開く・展開・テスト",
  fm_note="ZIP は展開せずにその場で編集できます。分割アーカイブ（.001、.z01、.a00、.vol1.egg、RAR ボリューム）や、EXE 自己解凍ファイル内の ZIP/7Z/RAR/ALZ/EGG も開けます。",
  in_h="インストール", in_sub="アプリを「アプリケーション」フォルダに移すだけです。",
  req=["macOS 12 以降", "ユニバーサル：Apple Silicon · Intel", "無料"],
  steps=[
    ("ダウンロード", f'<a href="{DOWNLOAD}">GitHub のリリースページ</a>から最新の <code>Zipper.app.zip</code> をダウンロードして展開します。'),
    ("「アプリケーション」へ移動", "<code>Zipper.app</code> を「アプリケーション」フォルダにドラッグします。"),
    ("初回の起動", "Apple の公証を受けていない個人配布アプリのため、初回起動時に警告が表示されます。<strong>ゴミ箱に入れる</strong> は押さずに <strong>完了</strong>（macOS 14 以前は <strong>キャンセル</strong>）で閉じ、<code>システム設定 → プライバシーとセキュリティ</code> の下部にある <strong>このまま開く</strong> をクリックします。"),
  ],
  term="ターミナルを使う場合は、次の 1 行でも同じです。",
  faq_h="よくある質問",
  faq=[
    ("本当に無料ですか？", "はい。個人・法人を問わず無料で使えます。"),
    ("ALZ や EGG を展開できますか？", "はい。分割 ALZ（.a00、.a01…）、パスワード付きファイル、AES/LEA 暗号化・ソリッド・分割の EGG にも対応しています。ALZ と EGG の作成には対応していません。"),
    ("Windows で展開するとファイル名が文字化けしませんか？", "しません。Zipper は Windows が想定する形式（NFC と UTF-8 フラグ）でファイル名を保存するため、エクスプローラーでも正しく表示されます。"),
    ("RAR を作成できますか？", "RAR は開く・展開のみです。作成には ZIP か 7Z をお使いください。"),
    ("インターネットに接続したり、ファイルを送信したりしますか？", "いいえ。すべての処理は Mac の中だけで行われます。"),
    ("言語はどう変更しますか？", "既定ではシステムの言語に従います。環境設定 → 一般 → 言語 で変更するとすぐに反映されます。"),
  ],
  oss="Zipper にはオープンソースソフトウェアが含まれています。ライセンス表示はアプリの 環境設定 → ライセンス で確認できます。",
  issues="問題を報告", releases="リリース",
),
}

EXTRA = {
"ko": dict(
  nav5="라이선스",
  faq_more=[("소스 코드도 공개하나요?", "아니요. Zipper는 실행 파일(앱)만 배포하는 프리웨어입니다. 소스 코드는 공개하지 않습니다.")],
  lic_h="라이선스", lic_sub="개인·기업 모두 완전 무료인 프리웨어입니다. 요금, 등록, 라이선스 키가 필요 없습니다.",
  lic_items=[
    ("✅", "누구나 무료", "개인·가정은 물론 회사·기관·학교 등 업무용·상업적 사용 모두 가능합니다(대수 제한 없음)."),
    ("📦", "재배포 가능", "수정하지 않은 원본을 라이선스와 함께 무료로 재배포할 수 있습니다."),
    ("🚫", "리버스 엔지니어링 금지", "유일한 제한입니다. 디컴파일·디스어셈블, 실행 파일 수정·패치를 금지합니다(법이 허용하는 예외는 제외)."),
    ("🛡️", "개인정보 수집 없음", "인터넷에 연결하지 않으며 어떤 정보도 수집·전송하지 않습니다. \"있는 그대로\" 제공되며 보증하지 않습니다."),
  ],
  lic_full="라이선스 전문 보기", lic_ko="한국어 번역",
  # README
  r_tag="macOS 압축 프로그램 · ZIP·7Z 만들기 · RAR·EGG·ALZ 풀기 · 한글 파일명 깨짐 방지",
  r_dl="⬇ 최신 버전 다운로드", r_page="소개 페이지", r_free="개인·기업 모두 무료",
  r_intro="ZIP, 7Z, TAR를 만들고 RAR, EGG, ALZ, ISO 등 30여 가지 형식을 푸는 macOS용 압축 프로그램입니다. 파일 이름을 Windows가 읽는 방식으로 저장해 한글 이름이 깨지지 않습니다.",
  r_req="요구 사항: macOS 12 이상 (Apple Silicon / Intel 유니버설)",
  r_lang="🌐 앱 언어는 macOS 시스템 언어를 따릅니다: 한국어, 영어, 중국어(간체), 일본어. 그 외 언어에서는 영어로 표시됩니다.",
  r_install="설치", r_features="기능", r_formats="지원 형식", r_area="영역", r_feat="기능",
  r_rows=[("압축", "ZIP·7Z·TAR·TGZ·TBZ·TXZ·GZ 만들기, 압축 수준(저장/빠르게/보통/최대), 분할 압축(25MB·CD·DVD·FAT32 등), 제외 필터"),
          ("풀기", "30여 가지 형식, 스마트 풀기, 분할 파일·EXE 자동 풀림 파일 열기, 코드페이지 자동 감지"),
          ("편집", "ZIP을 풀지 않고 파일 추가·삭제·이름 바꾸기, 새 폴더"),
          ("보안", "ZIP·7Z AES-256 암호화, 7Z 파일 이름 암호화, 암호화된 EGG(AES/LEA)·ALZ·RAR 풀기"),
          ("도구", "무결성 테스트, 파일 체크섬(CRC32·MD5·SHA-1·SHA-256)"),
          ("기타", "한글 파일명 NFC 저장, .DS_Store·__MACOSX 제외, 라이트/다크 테마, 한국어·영어·중국어·일본어 UI")],
  r_safe="안심하고 쓰세요",
  r_safe_items=["**인터넷에 연결하지 않습니다**: 모든 작업은 Mac 안에서만 이루어지며 파일이나 정보를 외부로 보내지 않습니다.",
                "**Windows와 호환**: 한글 등 비영어 파일 이름이 Windows 탐색기에서도 그대로 보입니다."],
  r_lic_body="**개인·기업 모두 완전 무료**인 프리웨어입니다. 요금, 등록, 라이선스 키가 필요 없습니다.",
  r_lic_list=["개인·가정은 물론 회사·기관·학교 등 업무용·상업적 사용 모두 가능합니다 (대수 제한 없음).",
              "수정하지 않은 원본을 라이선스와 함께 무료로 재배포할 수 있습니다.",
              "**유일하게 금지되는 것은 리버스 엔지니어링입니다** — 디컴파일·디스어셈블, 실행 파일 수정·패치 금지 (법이 계약으로 제한할 수 없다고 정한 범위는 예외).",
              "\"있는 그대로\" 제공되며 어떠한 보증도 하지 않습니다. 개인정보를 수집하지 않습니다.",
              "앱에 포함된 오픈 소스 구성 요소는 각자의 라이선스를 따르며, 고지 내용은 앱의 환경설정 › 라이센스에서 볼 수 있습니다."],
  r_full="전문", r_en_orig="영어 원문", r_credit="크레딧 & 문의",
  r_credit_items=["ALZ 형식 해석: [unalz](https://github.com/kippler/unalz) (kippler, zlib 라이선스) 참고",
                  "RAR 풀기: UnRAR 소스 코드 (Alexander Roshal) — RAR 압축 알고리즘을 재현하는 데 사용할 수 없습니다",
                  "버그 신고: [Issues](https://github.com/jayusop/Zipper/issues) · 메일 jayusop@gmail.com"],
),
"en": dict(
  nav5="License",
  faq_more=[("Is the source code available?", "No. Zipper is freeware distributed as a compiled app only; the source code is not published.")],
  lic_h="License", lic_sub="Completely free freeware for individuals and businesses. No fee, registration or license key.",
  lic_items=[
    ("✅", "Free for everyone", "Personal, home, business, government and school use — any number of Macs."),
    ("📦", "Redistribution allowed", "You may share the unmodified original for free, together with the license."),
    ("🚫", "No reverse engineering", "The only restriction: no decompiling, disassembling, modifying or patching the app (except where law grants that right)."),
    ("🛡️", "No data collection", "Zipper never connects to the internet and collects nothing. Provided \"as is\", without warranty."),
  ],
  lic_full="Read the full license", lic_ko="Korean translation",
  r_tag="Archive utility for macOS · Create ZIP & 7Z · Extract RAR, EGG, ALZ · File names that stay intact",
  r_dl="⬇ Download the latest version", r_page="Website", r_free="free for personal & business use",
  r_intro="A macOS archive utility that creates ZIP, 7Z and TAR archives and extracts RAR, EGG, ALZ, ISO and 30+ other formats. File names are stored the way Windows expects, so they never come out garbled.",
  r_req="Requirements: macOS 12 or later (Universal: Apple Silicon / Intel)",
  r_lang="🌐 The app follows your macOS language: Korean, English, Chinese (Simplified) or Japanese; English otherwise.",
  r_install="Installation", r_features="Features", r_formats="Supported formats", r_area="Area", r_feat="Features",
  r_rows=[("Compress", "Create ZIP, 7Z, TAR, TGZ, TBZ, TXZ, GZ; levels Store/Fast/Normal/Maximum; split into parts (25 MB, CD, DVD, FAT32 …); exclude filter"),
          ("Extract", "30+ formats, Smart extract, multi-part and EXE self-extracting archives, automatic code-page detection"),
          ("Edit", "Add, delete and rename files inside a ZIP without unpacking; new folder"),
          ("Security", "AES-256 for ZIP and 7Z, encrypted 7Z file names, extract encrypted EGG (AES/LEA), ALZ and RAR"),
          ("Tools", "Integrity test, file checksums (CRC32, MD5, SHA-1, SHA-256)"),
          ("Other", "NFC file names, leaves out .DS_Store and __MACOSX, light/dark theme, Korean/English/Chinese/Japanese UI")],
  r_safe="Use it with confidence",
  r_safe_items=["**No internet connection**: everything happens on your Mac; no files or data ever leave it.",
                "**Windows-friendly**: non-English file names display correctly in File Explorer."],
  r_lic_body="Zipper is **completely free freeware for individuals and businesses**. No fee, registration or license key.",
  r_lic_list=["Personal, home, business, government and school use are all allowed (any number of computers).",
              "You may redistribute the unmodified original for free, together with the license.",
              "**The only restriction is reverse engineering** — no decompiling, disassembling, modifying or patching the app (except where law grants a right that cannot be waived).",
              "Provided \"as is\" without warranty. No personal data is collected.",
              "Open-source components included in the app remain under their own licenses; notices are in Preferences › Licenses."],
  r_full="Full text", r_en_orig="English original", r_credit="Credits & contact",
  r_credit_items=["ALZ format: based on [unalz](https://github.com/kippler/unalz) (kippler, zlib license)",
                  "RAR extraction: UnRAR source code (Alexander Roshal) — may not be used to re-create the RAR compression algorithm",
                  "Bug reports: [Issues](https://github.com/jayusop/Zipper/issues) · jayusop@gmail.com"],
),
"zh": dict(
  nav5="许可证",
  faq_more=[("会公开源代码吗？", "不会。Zipper 是只发布可执行应用的免费软件，不公开源代码。")],
  lic_h="许可证", lic_sub="个人和企业均可完全免费使用的免费软件。无需付费、注册或许可证密钥。",
  lic_items=[
    ("✅", "人人免费", "个人、家庭以及公司、机构、学校等商业用途均可使用，不限台数。"),
    ("📦", "允许再分发", "可将未经修改的原版连同许可证一起免费再分发。"),
    ("🚫", "禁止逆向工程", "唯一的限制：禁止反编译、反汇编、修改或修补应用（法律允许的情形除外）。"),
    ("🛡️", "不收集数据", "Zipper 不联网，不收集任何信息。按“原样”提供，不作任何保证。"),
  ],
  lic_full="查看许可证全文", lic_ko="韩语译本",
  r_tag="macOS 压缩软件 · 创建 ZIP、7Z · 解压 RAR、EGG、ALZ · 文件名不乱码",
  r_dl="⬇ 下载最新版本", r_page="介绍页面", r_free="个人与企业均免费",
  r_intro="一款 macOS 压缩软件，可创建 ZIP、7Z、TAR，并解压 RAR、EGG、ALZ、ISO 等 30 多种格式。文件名按 Windows 期望的方式保存，不会乱码。",
  r_req="系统要求：macOS 12 或更高版本（通用版：Apple Silicon / Intel）",
  r_lang="🌐 应用语言跟随 macOS 系统语言：韩语、英语、简体中文、日语；其他语言显示为英语。",
  r_install="安装", r_features="功能", r_formats="支持格式", r_area="类别", r_feat="功能",
  r_rows=[("压缩", "创建 ZIP、7Z、TAR、TGZ、TBZ、TXZ、GZ；压缩级别（存储/快速/标准/最大）；分卷（25MB、CD、DVD、FAT32 等）；排除过滤"),
          ("解压", "30 多种格式、智能解压、分卷与 EXE 自解压文件、自动识别代码页"),
          ("编辑", "无需解压即可在 ZIP 中添加、删除、重命名文件，新建文件夹"),
          ("安全", "ZIP、7Z 的 AES-256 加密，7Z 文件名加密，解压加密的 EGG（AES/LEA）、ALZ、RAR"),
          ("工具", "完整性测试、文件校验和（CRC32、MD5、SHA-1、SHA-256）"),
          ("其他", "NFC 文件名、排除 .DS_Store 和 __MACOSX、浅色/深色主题、韩英中日界面")],
  r_safe="放心使用",
  r_safe_items=["**不联网**：所有操作都在你的 Mac 上完成，文件和数据不会外传。",
                "**兼容 Windows**：非英文文件名在文件资源管理器中正常显示。"],
  r_lic_body="Zipper 是**个人和企业均可完全免费使用**的免费软件。无需付费、注册或许可证密钥。",
  r_lic_list=["个人、家庭以及公司、机构、学校等业务和商业用途均可使用（不限台数）。",
              "可将未经修改的原版连同许可证一起免费再分发。",
              "**唯一禁止的是逆向工程** —— 禁止反编译、反汇编、修改或修补应用（法律规定不可通过合同限制的情形除外）。",
              "按“原样”提供，不作任何保证。不收集个人信息。",
              "应用中包含的开源组件遵循各自的许可证，声明可在 偏好设置 › 许可证 中查看。"],
  r_full="全文", r_en_orig="英文原文", r_credit="致谢与联系",
  r_credit_items=["ALZ 格式：参考 [unalz](https://github.com/kippler/unalz)（kippler，zlib 许可证）",
                  "RAR 解压：UnRAR 源代码（Alexander Roshal）—— 不得用于重现 RAR 压缩算法",
                  "问题反馈：[Issues](https://github.com/jayusop/Zipper/issues) · jayusop@gmail.com"],
),
"ja": dict(
  nav5="ライセンス",
  faq_more=[("ソースコードは公開されていますか？", "いいえ。Zipper は実行ファイル（アプリ）のみを配布するフリーウェアで、ソースコードは公開していません。")],
  lic_h="ライセンス", lic_sub="個人・法人を問わず完全無料のフリーウェアです。料金、登録、ライセンスキーは不要です。",
  lic_items=[
    ("✅", "誰でも無料", "個人・家庭はもちろん、会社・団体・学校などの業務・商用利用も可能です（台数制限なし）。"),
    ("📦", "再配布可", "改変していないオリジナルをライセンスとともに無料で再配布できます。"),
    ("🚫", "リバースエンジニアリング禁止", "唯一の制限です。逆コンパイル・逆アセンブル、実行ファイルの改変・パッチを禁止します（法律で認められる場合を除く）。"),
    ("🛡️", "データ収集なし", "インターネットに接続せず、情報を一切収集しません。「現状のまま」提供され、保証はありません。"),
  ],
  lic_full="ライセンス全文を見る", lic_ko="韓国語訳",
  r_tag="macOS 用圧縮ソフト · ZIP・7Z 作成 · RAR・EGG・ALZ 展開 · 文字化けしないファイル名",
  r_dl="⬇ 最新版をダウンロード", r_page="紹介ページ", r_free="個人・法人とも無料",
  r_intro="ZIP、7Z、TAR を作成し、RAR、EGG、ALZ、ISO など 30 以上の形式を展開できる macOS 用圧縮ソフトです。ファイル名を Windows が想定する形式で保存するため、文字化けしません。",
  r_req="動作環境：macOS 12 以降（ユニバーサル：Apple Silicon / Intel）",
  r_lang="🌐 アプリの言語は macOS のシステム言語に従います：韓国語、英語、簡体字中国語、日本語。それ以外は英語で表示されます。",
  r_install="インストール", r_features="機能", r_formats="対応形式", r_area="分類", r_feat="機能",
  r_rows=[("圧縮", "ZIP・7Z・TAR・TGZ・TBZ・TXZ・GZ の作成、圧縮レベル（無圧縮/高速/標準/最大）、分割圧縮（25MB・CD・DVD・FAT32 など）、除外フィルタ"),
          ("展開", "30 以上の形式、スマート展開、分割ファイル・EXE 自己解凍ファイル、コードページ自動検出"),
          ("編集", "ZIP を展開せずにファイルの追加・削除・名前変更、新規フォルダ"),
          ("セキュリティ", "ZIP・7Z の AES-256 暗号化、7Z のファイル名暗号化、暗号化 EGG（AES/LEA）・ALZ・RAR の展開"),
          ("ツール", "整合性テスト、ファイルチェックサム（CRC32・MD5・SHA-1・SHA-256）"),
          ("その他", "NFC ファイル名、.DS_Store・__MACOSX の除外、ライト/ダークテーマ、日英韓中 UI")],
  r_safe="安心してお使いください",
  r_safe_items=["**インターネットに接続しません**：すべての処理は Mac の中だけで行われ、ファイルや情報を外部に送りません。",
                "**Windows と互換**：日本語などのファイル名がエクスプローラーでも正しく表示されます。"],
  r_lic_body="Zipper は**個人・法人を問わず完全無料**のフリーウェアです。料金、登録、ライセンスキーは不要です。",
  r_lic_list=["個人・家庭はもちろん、会社・団体・学校などの業務・商用利用も可能です（台数制限なし）。",
              "改変していないオリジナルをライセンスとともに無料で再配布できます。",
              "**唯一禁止されているのはリバースエンジニアリングです** — 逆コンパイル・逆アセンブル、実行ファイルの改変・パッチは禁止です（法律が契約で制限できないと定める範囲は除く）。",
              "「現状のまま」提供され、いかなる保証もしません。個人情報は収集しません。",
              "アプリに含まれるオープンソースコンポーネントはそれぞれのライセンスに従い、表示は 環境設定 › ライセンス で確認できます。"],
  r_full="全文", r_en_orig="英語原文", r_credit="クレジット & お問い合わせ",
  r_credit_items=["ALZ 形式：[unalz](https://github.com/kippler/unalz)（kippler、zlib ライセンス）を参考",
                  "RAR 展開：UnRAR ソースコード（Alexander Roshal）— RAR 圧縮アルゴリズムの再現には使用できません",
                  "不具合報告：[Issues](https://github.com/jayusop/Zipper/issues) · jayusop@gmail.com"],
),
}

for _l in EXTRA: T[_l].update(EXTRA[_l]); T[_l]["faq"] = T[_l]["faq"] + T[_l]["faq_more"]

def url(lang):
    return SITE if lang == "ko" else f"{SITE}{lang}/"

def page(lang):
    t = T[lang]
    p = "" if lang == "ko" else "../"
    e = html.escape
    alts = "\n".join(f'<link rel="alternate" hreflang="{HTML_LANG[l]}" href="{url(l)}">' for l in LANGS)
    alts += f'\n<link rel="alternate" hreflang="x-default" href="{url("ko")}">'
    cur = ' aria-current="page"'
    langnav = "".join(
        '<a href="{}{}" hreflang="{}"{}>{}</a>'.format(p, "" if l == "ko" else l + "/", HTML_LANG[l], cur if l == lang else "", NATIVE[l])
        for l in LANGS)
    feats = "".join(f'<div class="card"><div class="ico">{i}</div><h3>{e(h)}</h3><p>{e(d)}</p></div>' for i, h, d in t["features"])
    steps = "".join(f"<li><strong>{e(h)}</strong>{d}</li>" for h, d in t["steps"])
    faqs = "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in t["faq"])
    lics = "".join(f'<div class="card"><div class="ico">{i}</div><h3>{e(h)}</h3><p>{e(d)}</p></div>' for i, h, d in t["lic_items"])
    reqs = "".join(f"<span>{e(r)}</span>" for r in t["req"])
    w = "".join(f'<span class="chip w">{f}</span>' for f in WRITE)
    r = "".join(f'<span class="chip">{e(f)}</span>' for f in READ)
    ld = {
        "@context": "https://schema.org", "@type": "SoftwareApplication", "name": "Zipper",
        "operatingSystem": "macOS 12+", "applicationCategory": "UtilitiesApplication",
        "softwareVersion": VERSION, "description": t["desc"], "url": url(lang),
        "downloadUrl": DOWNLOAD, "image": SITE + "assets/icon.png", "inLanguage": HTML_LANG[lang],
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
        "mainEntity": None,
    }
    ld.pop("mainEntity")
    faq_ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in t["faq"]]}
    n = t["nav"]
    return f"""<!DOCTYPE html>
<html lang="{HTML_LANG[lang]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(t["title"])}</title>
<meta name="description" content="{e(t["desc"])}">
<meta name="keywords" content="{e(t["keywords"])}">
<link rel="canonical" href="{url(lang)}">
{alts}
<meta property="og:type" content="website">
<meta property="og:site_name" content="Zipper">
<meta property="og:title" content="{e(t["title"])}">
<meta property="og:description" content="{e(t["desc"])}">
<meta property="og:url" content="{url(lang)}">
<meta property="og:image" content="{SITE}assets/icon.png">
<meta property="og:locale" content="{OG_LOCALE[lang]}">
<meta name="twitter:card" content="summary">
<meta name="theme-color" content="#14204a">
<link rel="icon" type="image/png" sizes="32x32" href="{p}assets/favicon-32.png">
<link rel="apple-touch-icon" href="{p}assets/apple-touch-icon.png">
<link rel="stylesheet" href="{p}assets/style.css">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
<script type="application/ld+json">{json.dumps(faq_ld, ensure_ascii=False)}</script>
</head>
<body>
<header class="topbar"><div class="wrap">
  <a class="brand" href="#top"><img src="{p}assets/favicon-32.png" alt="" width="30" height="30">Zipper</a>
  <nav><a href="#features">{e(n[0])}</a><a href="#formats">{e(n[1])}</a><a href="#install">{e(n[2])}</a><a href="#faq">{e(n[3])}</a><a href="#license">{e(t["nav5"])}</a></nav>
  <div class="lang">{langnav}</div>
</div></header>

<main id="top">
<div class="hero"><div class="wrap">
  <div>
    <h1>{t["h1"]}</h1>
    <p class="lead">{e(t["lead"])}</p>
    <div class="cta">
      <a class="btn btn-primary" href="{DOWNLOAD}">⬇ {e(t["dl"])}</a>
      <a class="btn btn-ghost" href="{REPO_URL}">{e(t["gh"])}</a>
    </div>
    <div class="meta">{e(t["meta"])}</div>
  </div>
  <img class="icon" src="{p}assets/icon.png" alt="Zipper" width="512" height="512">
</div></div>

<section id="features"><div class="wrap">
  <h2>{e(t["f_h"])}</h2>
  <p class="sub">{e(t["f_sub"])}</p>
  <div class="grid">{feats}</div>
</div></section>

<section class="alt"><div class="wrap">
  <figure class="shot" style="margin:0 auto"><div class="bar"><i></i><i></i><i></i></div>
    <img src="{p}assets/screenshot-start.png" alt="{e(t["s_cap"])}" width="1402" height="1048" loading="lazy"></figure>
  <p class="caption">{e(t["s_cap"])}</p>
</div></section>

<section id="formats"><div class="wrap">
  <h2>{e(t["fm_h"])}</h2>
  <p class="sub">{e(t["fm_sub"])}</p>
  <div class="formats">
    <div class="card"><h3>{e(t["fm_w"])}</h3><div class="chips">{w}</div></div>
    <div class="card"><h3>{e(t["fm_r"])}</h3><div class="chips">{r}</div></div>
  </div>
  <p class="note">{e(t["fm_note"])}</p>
</div></section>

<section id="install" class="alt"><div class="wrap">
  <h2>{e(t["in_h"])}</h2>
  <p class="sub">{e(t["in_sub"])}</p>
  <div class="req">{reqs}</div>
  <ol class="steps">{steps}</ol>
  <p class="note">{e(t["term"])}</p>
  <pre>xattr -dr com.apple.quarantine /Applications/Zipper.app</pre>
</div></section>

<section id="faq"><div class="wrap">
  <h2>{e(t["faq_h"])}</h2>
  {faqs}
</div></section>
<section id="license" class="alt"><div class="wrap">
  <h2>{e(t["lic_h"])}</h2>
  <p class="sub">{e(t["lic_sub"])}</p>
  <div class="grid grid-4">{lics}</div>
  <p class="note"><a href="{REPO_URL}/blob/main/LICENSE">{e(t["lic_full"])}</a> · <a href="{REPO_URL}/blob/main/LICENSE.ko.md">{e(t["lic_ko"])}</a></p>
</div></section>
</main>

<footer><div class="wrap">
  <span>© 2026 jayusop · Freeware</span>
  <span>{e(t["oss"])}</span>
  <span class="right"><a href="{REPO_URL}/blob/main/LICENSE">{e(t["nav5"])}</a><a href="{REPO_URL}/releases">{e(t["releases"])}</a><a href="{REPO_URL}/issues">{e(t["issues"])}</a></span>
</div></footer>
</body>
</html>
"""

for lang in LANGS:
    d = OUT if lang == "ko" else os.path.join(OUT, lang)
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(page(lang))

links = "".join(f'<xhtml:link rel="alternate" hreflang="{HTML_LANG[l]}" href="{url(l)}"/>' for l in LANGS)
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
sm += "".join(f"  <url><loc>{url(l)}</loc>{links}</url>\n" for l in LANGS) + "</urlset>\n"
open(os.path.join(OUT, "sitemap.xml"), "w").write(sm)
open(os.path.join(OUT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\nSitemap: {SITE}sitemap.xml\n")
open(os.path.join(OUT, ".nojekyll"), "w").write("")
print("ok")

# ---------------------------------------------------------------- GitHub READMEs (repo root)
import re as _re
README_FILE = {"ko": "README.md", "en": "README.en.md", "zh": "README.zh-CN.md", "ja": "README.ja.md"}

def md(h):
    h = _re.sub(r'<a href="([^"]+)">(.*?)</a>', r'[\2](\1)', h)
    h = h.replace("<code>", "`").replace("</code>", "`").replace("<strong>", "**").replace("</strong>", "**")
    return h.replace("&amp;", "&")

def readme(lang):
    t = T[lang]
    nav = " · ".join(f"<b>{NATIVE[l]}</b>" if l == lang else f'<a href="{README_FILE[l]}">{NATIVE[l]}</a>' for l in LANGS)
    badge_free = t["r_free"].replace(" ", "%20").replace("&", "%26")
    steps = "\n".join(f"{i}. **{h}** — {md(d)}" for i, (h, d) in enumerate(t["steps"], 1))
    rows = "\n".join(f"| {a} | {b} |" for a, b in t["r_rows"])
    safe = "\n".join(f"- {x}" for x in t["r_safe_items"])
    lic = "\n".join(f"- {x}" for x in t["r_lic_list"])
    cred = "\n".join(f"- {x}" for x in t["r_credit_items"])
    w = " · ".join(WRITE); r = " · ".join(READ)
    return f"""<p align="center">
  {nav}
</p>

<p align="center">
  <img src="docs/assets/icon.png" width="128" alt="Zipper">
</p>

<h1 align="center">Zipper</h1>

<p align="center">
  {t["r_tag"]}<br>
  <a href="{DOWNLOAD}"><b>{t["r_dl"]}</b></a> ·
  <a href="{url(lang)}">{t["r_page"]}</a>
</p>

<p align="center">
  <img alt="macOS 12+" src="https://img.shields.io/badge/macOS-12%2B-1d2c5e">
  <img alt="Apple Silicon / Intel" src="https://img.shields.io/badge/Apple%20Silicon%20%2F%20Intel-universal-d9a93a">
  <img alt="{t["r_free"]}" src="https://img.shields.io/badge/license-freeware-3fb950">
  <img alt="Release" src="https://img.shields.io/github/v/release/{GITHUB_USER}/{REPO}?color=3fd6e0">
</p>

---

{t["r_intro"]}

> {t["r_req"]}<br>
> {t["r_lang"]}

<p align="center"><img src="docs/assets/screenshot-start.png" width="640" alt="Zipper"></p>

## {t["r_install"]}

{steps}

   {t["term"]}
   ```bash
   xattr -dr com.apple.quarantine /Applications/Zipper.app
   ```

## {t["r_features"]}

| {t["r_area"]} | {t["r_feat"]} |
|---|---|
{rows}

## {t["r_formats"]}

- **{t["fm_w"]}**: {w}
- **{t["fm_r"]}**: {r}

{t["fm_note"]}

## {t["r_safe"]}

{safe}

## {t["lic_h"]}

{t["r_lic_body"]}

{lic}

{t["r_full"]}: [LICENSE](LICENSE) ({t["r_en_orig"]}) · [LICENSE.ko.md](LICENSE.ko.md) ({t["lic_ko"] if lang != "ko" else "한국어 번역"})

## {t["r_credit"]}

{cred}
"""

for lang in LANGS:
    open(os.path.join(ROOT, README_FILE[lang]), "w", encoding="utf-8").write(readme(lang))
print("readmes ok")
