# Scheduler

### Issueの使い方
1. todoのラベルが貼られているタスク（Issue）から好きなものを取る
1. とったら`assign`を自分に変更する
1. ラベルを`doing`に変更する（todoのラベルは剥がす）
1. タスクを取ったら`master`ブランチを元に「Issue番号 + "-"」の`branch`を作る(例：1-)[参考](https://qiita.com/sue738/items/7b979c554a03441901c6)

### branchの使い方
1. 上記で作成したブランチを自分の作業ブランチとする(以後、`1-`を例とする)
1. ローカルの開発環境に`1-`ブランチをチェックアウトしてくる[参考](https://qiita.com/naoki85/items/c7660d70347e9e70b201)
1. 作業が一区切りついた段階で、リモートの`1-`ラベルを`doing`に変更する（todoのラベルは剥がす）
1. タスクを取ったら「Issue番号 + "-"」の`branch`を作る[参考](https://qiita.com/sue738/items/7b979c554a03441901c6)
