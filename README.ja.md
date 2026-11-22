# Netheretヘルプデスク ステップ02：レイアウト

[English](README.md) | [Français](README.fr.md) | [Español](README.es.md) | [日本語](README.ja.md) | [Deutsch](README.de.md)

授業のための作例です。16のステップで、小さな会社のITを支える架空の会社Netheretのために、ヘルプデスクのWebアプリを作っていきます。 このステップでは、すべてのページに同じレイアウトを用意します。Jinjaのベーステンプレート、スタイルシート、メニューを、誰でも使えるように作ります。

## このステップで加わるもの

- `helpdesk/templates/base.html`：すべてのページが共有するレイアウト。各ページは
  これを `extend` して、`title` と `content` のブロックを埋めます。
- `helpdesk/templates/home.html`：テンプレートになったトップページ。
- `helpdesk/static/css/style.css`：色を変数にした、シンプルなCSS。
- 最初からアクセシブルな構造：`lang="en-GB"`、スキップリンク、
  `header`、`nav`、`main`、`footer` のランドマーク、いま見ているページのメニューリンクに付けた
  `aria-current`、太い黄色のフォーカスリング。

## 動かしてみる

```
python -m venv .venv
source .venv/bin/activate        # on Windows: .venv\Scripts\activate
pip install -r requirements.txt
flask --app helpdesk run --debug
```

http://127.0.0.1:5000 を開きます。Tabキーを1回押すと、「Skip to main content」のリンクが
現れます。Enterキーを押すと、フォーカスがメニューを飛び越えます。

## 注目するところ

- `home.html` の `{% extends "base.html" %}` と `{% block content %}`。
- `base.html` の `nav_link` マクロ：メニューのリンクを書く場所を1か所にまとめています。
- `url_for('static', ...)`：CSSファイルのアドレスをFlaskが組み立ててくれます。
- `style.css` の `:focus-visible` のルールと `.skip-link`。

## このステップを学ぶ

これは **Task 2. Developing the solution** の16ステップ中のステップ2です。T Level Digital Software Developmentの無料レッスン（英語）のシリーズで、PythonとFlaskを使い、アジャイルのスプリントでNetheretのヘルプデスクを作ります。このステップのレッスンはこちらです：
[JinjaテンプレートとCSSによるページレイアウト](https://mitsurutech.co.uk/resources/t-level/dsd-t2-02-layout)。

- 前のステップ：[ステップ01「Flaskプロジェクトの準備」](https://github.com/mitsurutech/netheret-helpdesk-01-setup)
- 次のステップ：[ステップ03「Flask-SQLAlchemyによるデータベース」](https://github.com/mitsurutech/netheret-helpdesk-03-database)
- [T Level Digitalの無料レッスン一覧](https://mitsurutech.co.uk/resources/t-level)
- [これらのレッスンをMitsuruTechでクラスに教える](https://mitsurutech.co.uk/ja/learning)、[料金を見る](https://mitsurutech.co.uk/ja/pricing)、
  [学校で無料の1年を始める](https://mitsurutech.co.uk/ja/signup)

## この作例について

T Level Digital Software Developmentの授業のための作例として、[Mitsuru Technologies](https://mitsurutech.co.uk/ja)（MitsuruTech）が書きました。
Netheret IT Support Solutionsの課題文はPearsonのサンプル評価資料によるものです。このコードと解説は私たち自身のもので、
PearsonやDepartment for Educationが公開、推奨、承認したものではありません。
「T Level」はDepartment for Educationの登録商標です。
