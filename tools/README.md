# 저장소 관리용 메모 (GitHub에 올라가지 않음)

`tools/`는 `.gitignore`에 들어 있어 저장소에는 올라가지 않습니다. 소개 페이지와 README를 다시 만들 때만 씁니다.

## 저장소 구조

```
README.md            한국어 (GitHub 첫 화면)
README.en.md         English
README.zh-CN.md      简体中文
README.ja.md         日本語
LICENSE              프리웨어 라이선스 (영어 원문)
LICENSE.ko.md        한국어 번역
docs/                GitHub Pages 소개 페이지
  index.html         한국어 (기본)
  en/ zh/ ja/        언어별 페이지
  assets/            아이콘, 스크린샷, style.css
  sitemap.xml  robots.txt  .nojekyll
tools/build.py       페이지·README 생성 스크립트 (로컬 전용)
```

소스 코드는 이 저장소에 넣지 않습니다. 앱은 Releases에 `Zipper.app.zip`으로만 올립니다.

## 문구를 고칠 때

HTML이나 README를 직접 고치지 말고 `tools/build.py`를 고친 뒤 다시 만듭니다.
네 언어의 소개 페이지, README, 사이트맵이 한 번에 갱신됩니다(LICENSE는 직접 고칩니다).

```sh
cd ~/Develop/zipper-doc
python3 tools/build.py
```

버전을 올릴 때는 스크립트 맨 위의 `VERSION`만 바꾸면 됩니다.

## 처음 배포

1. GitHub에 공개 저장소 `Zipper`를 만듭니다.
2. 이 폴더를 올립니다.
   ```sh
   cd ~/Develop/zipper-doc
   git init -b main && git add . && git commit -m "Zipper 소개 페이지와 라이선스"
   git remote add origin https://github.com/jayusop/Zipper.git
   git push -u origin main
   ```
3. 저장소 **Settings → Pages**: Source **Deploy from a branch**, 브랜치 `main`, 폴더 **`/docs`**.
4. 1~2분 뒤 https://jayusop.github.io/Zipper/ 에서 열립니다.

## 새 버전 올리기

1. 앱을 Release로 빌드합니다.
   ```sh
   cd ~/Develop/zipper
   xcodebuild -project Zipper.xcodeproj -scheme Zipper -configuration Release build
   ```
2. 빌드된 `Zipper.app`을 압축합니다(빌드 위치는 Xcode › Product › Show Build Folder).
   ```sh
   ditto -c -k --keepParent Zipper.app Zipper.app.zip
   ```
3. GitHub **Releases → Draft a new release**에서 태그(예: `v0.1.0`)를 만들고 `Zipper.app.zip`을 첨부해 게시합니다.
   소개 페이지와 README의 다운로드 버튼은 `releases/latest`로 연결되므로 고칠 필요가 없습니다.

## 검색엔진 등록

- Google [Search Console](https://search.google.com/search-console), 네이버 [서치어드바이저](https://searchadvisor.naver.com)에 `https://jayusop.github.io/Zipper/`를 등록하고 `sitemap.xml`을 제출합니다.
- 소유 확인용 HTML 파일은 `docs/`에, 메타 태그는 `tools/build.py`의 `<head>`에 넣습니다.
