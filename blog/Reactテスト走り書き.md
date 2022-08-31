# テスト
## ライブラリ
<span style="color: #95c7a4">Jest</span> or <span style="color: #95c7a4">React-Testing-Library(RTL)</span> or <span style="color: #95c7a4">Mock Service Worker(MSW)</span>
(ちなみにCreateReactAppでプロジェクトを作った際には最初から入っている)

### Jest
一般的なjavascriptのテストに利用

### RTL
React用のテスティングライブラリでReactの機能のテストで利用

### react-dom/test-utils
None Content

### MSW
APIなどを利用したり非同期のテストをする際に利用

### mock-require
None Content

### cypress
E2Eテストに利用する。

## 提供されている機能
- セットアップ/後処理
beforeEach, afterEachを使う例ではdomのマウントとアンマウントをしている。
-  act
レンダー、ユーザイベント、データの取得といったタスクをする。
これらのタスクに関連する更新がすべて処理され、DOM に反映されていることを保証します。
- render
Componentの描画に使う。
- APIのモック, モジュールのモック、イベントコール、タイマー
多分実際のサンプルを見た方が簡単に理解できる


## 一般的にテストすべきこと
### 静的テスト
NoContent
### Unit test
NoContent
### 結合テスト
NoContent
### E2E test
NoContent
## その他メモ
トレードオフ
テストツールを選定する時、いくつかのトレードオフを考慮することは価値があります。

実行速度 vs 環境の現実度： 変更を加えてから結果を見るまでのフィードバックが早いツールは、ブラウザでの動作を正確に模倣しません。一方実際のブラウザ環境を使うようなツールは、イテレーションの速度が落ちる上 CI サーバでは壊れやすいです。
モックの粒度 コンポーネントのテストでは、ユニットテストとインテグレーションテストの区別は曖昧です。フォームをテストする時、そのテストはフォーム内のボタンもテストすべきでしょうか。それともボタンコンポーネント自体が自身のテストを持つべきでしょうか。ボタンのリファクタリングはフォームのテストを壊さないべきでしょうか。
チームやプロダクトに応じて、答えは違ってきます。

推奨ツール
Jest は jsdom を通じて DOM にアクセスできる JavaScript のテストランナーです。jsdom はブラウザの模倣環境にすぎませんが、React コンポーネントをテストするのには十分なことが多いです。Jest は モジュール や タイマー のモックのような機能を組み合わせて、高速にイテレーションを回すことができ、コードをどう実行するかをよりコントロールできます。

React Testing Library は実装の詳細に依存せずに React コンポーネントをテストすることができるツールセットです。このアプローチはリファクタリングを容易にし、さらにアクセシビリティのベスト・プラクティスへと手向けてくれます。コンポーネントを children 抜きに「浅く」レンダーする方法は提供していませんが、Jest のようなテストランナーで モック することで可能です。

一般的には、スナップショットを使うよりもより個別的なアサーションを行う方がベターです。

# toHogeでの比較では関数を伴ったオブジェクトの比較はできない。

# プロパティの受け渡しテスト。
```
expect(mockChildComponent).toHaveBeenCalledWith(
    expect.objectContaining({
      open: true,
      data: "some data",
    })
  );
// 一回しか呼ばれない時

expect(mockFn.mock.calls).toEqual([
  [arg1, arg2, ...], // First call
  [arg1, arg2, ...]  // Second call
]);
// 内部で複数回呼ばれる場合(リストアイテムとか)
```

```

```