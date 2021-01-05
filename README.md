# video_capturer.py



## ChangeLog

- 2021-01-04 nabetaka READMEの作成・リリース
- 2021-01-05 nabetaka READMEの更新: 「Description」，「Usage」の追記



## Overview

Webカメラの映像のフレームを一定間隔で保存するプログラム．



## Description

実行ディレクトリ内に画像保存用ディレクトリ「images/yyyymmdd/」を作成する．



## Requirement

以下の環境で動作環境済み．

- Apple mac OS Big Sur Version 11.1
- Python 3.9.1
- OpenCV-Python 4.5.1.48



## Usage

1. 以下のコマンドを実行．

```shell
> python video_capturer.py
```

2. フレームの保存間隔を入力（1〜60[秒]のうち60の約数）．
3. 'q'キーを押すことで撮影終了．

