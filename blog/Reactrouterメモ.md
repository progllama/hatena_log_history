- BrowserRouter(ブラウザとの連携)
- Routes(ルートの定義領域)
- Route(ルートの定義)
- Link(リンクの定義)
- NavLink(リンクのパスと現在のパスが同じならActiveとなるリンクの定義)
- Outlet(ネストしたときに現在のルートに対応したこ要素を取得)
- useParams(パスパラメータの取得)
- useSearchParams(クエリパラメータの取得)
- useLocation(現在のロケーションの取得)
- useNavigate(イベント発生時などLinkを使わない方法で遷移をする際に使う)
- index(ネスト時のデフォルトのこ要素を定義、to=のところに代わりに入れる)
ざっとこのあたりがわかれば使える？

# テスト
- MemoryRouter(テストに使う。というのもreact-routerの機能はrouter内でしか使えないから)