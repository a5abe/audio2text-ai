# 🎹 audio2text-ai

## 🧠 Motivation

**An experiment: "Letting ChatGPT (which has no ears) listen to my piano performance."**

As a hobby pianist, I often record short sessions of improvised or meditative playing.  
This time, I wanted to share those musical moments with ChatGPT and my internal thought framework — a multi-voice dialogue system I call "Asabe Brain Symposium."

The question was:  
**"How can I let an AI *understand* my music without hearing it?"**

## 🛠️ What this project does

- Converts `.m4a` audio into `.wav` using `ffmpeg`  
- Uses `librosa` to extract pitch and visualize it over time  
- Generates a frequency vs. time graph to represent the music  
- (Planned) Translate pitch features into a human-readable musical story

## 📦 Requirements

Set up with `uv`:

```bash
uv venv
uv pip install numpy scipy matplotlib librosa
````

Or install with regular `pip`.

## ▶️ How to run

```bash
uv run :main.py
```

You’ll need:

* `input.m4a` (audio file)
* `ffmpeg` installed

## 💻 Environment

* OS: Windows 10
* Python: 3.11
* Tool: [uv](https://github.com/astral-sh/uv) for lightweight environment management
* Audio tools: ffmpeg

## 🙏 Final words

If you're curious about AI, music, or how to make machines "feel" human intention — welcome aboard.
This is just a first step. Let's keep experimenting.

---

## 🎹 audio2text-ai（日本語）

## 🧠 動機

**耳のないChatGPTに、自分のピアノ演奏を“聴かせてみる”実験。**

趣味でピアノを弾いていて、瞑想的に音を出して録音することがあります。
今回はそれを、「耳のないChatGPT」と「自分の頭の中にある多声的な思考メンバーたち（あさべ脳シンポジウム）」に聴かせたいと思いました。

問いはこうです：
**「AIに、音を“聴かずに”音楽を届けるにはどうしたらいい？」**

## 🛠️ プロジェクト内容

* `ffmpeg`で `.m4a` を `.wav` に変換
* `librosa`で音のピッチを分析し、時間軸で可視化
* 「音楽っぽさ」をプロットで表現
* （今後）ChatGPTと語れるような“音のストーリー”に変換したい

## 📦 必要環境

`uv` でセットアップする場合：

```bash
uv venv
uv pip install numpy scipy matplotlib librosa
```

`pip` でもOK。

## ▶️ 実行方法

```bash
uv run :main.py
```

事前に必要なのは：

* `input.m4a`（音声ファイル）
* `ffmpeg` のインストール

## 💻 動作環境（参考）

* OS: Windows 10
* Python: 3.11
* 環境管理ツール: [uv](https://github.com/astral-sh/uv)
* 音声処理: ffmpeg

## 🙏 最後に

AIや音楽、人間の思いを“機械に感じさせる”方法に興味があるなら、ぜひようこそ。
これはまだ第一歩。これからも遊んでいこう。