# Scheduler

### 事前準備
- ZenHubのインストール[参考](https://qiita.com/suzuki-hoge/items/f02b6752d8876ba6e114)
- ZenHubの使い方[参考](http://phiary.me/chrome-extension-zenhub/)

### Gitの使い方（作業の流れ）

#### 作業準備
1. todoのラベルが貼られているタスク（Issue）から好きなものを取る
1. とったら`assign`を自分に変更する
1. ラベルを`doing`に変更する（todoのラベルは剥がす）
1. タスクを取ったら`master`ブランチを元に「Issue番号 + "-"」の`branch`を作る(例：1-)[参考](https://qiita.com/sue738/items/7b979c554a03441901c6)
1. 上記で作成したブランチを自分の作業ブランチとする(以後、`1-`を例とする)

#### 作業開始
1. ローカルの開発環境に`1-`ブランチをチェックアウトしてくる[参考](https://qiita.com/naoki85/items/c7660d70347e9e70b201)
1. 作業が一区切りついた段階で、リモートの`1-`ブランチにコミット&プッシュを行う
1. 担当していたタスクの`Issue`に作業時間を記録する[参考](http://takuya-1st.hatenablog.jp/entry/2018/05/16/010110)
1. 実装が完了した段階でリモートの`1-`ブランチにコミット&プッシュを行う
1. ラベルを`complete`にする
1. 自分が実装した差分の`pull request`を作成する（`assign`を山田にする？）

#### 作業完了
1. 全員で`pull request`の内容を確認（レビュー）する
1. 問題なければ`master`ブランチへマージを実施する（山田がマージする？）
1. プルリクがマージされたら担当Issueを`close`する
