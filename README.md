# test_grpc_tavern

シンプルな gRPC の計算サーバーです。

## 環境構築

### Go

- Go 1.24 以上
- Protocol Buffers コンパイラ `protoc` 3.x 以上
- gRPC 用コード生成プラグイン

```bash
go install google.golang.org/protobuf/cmd/protoc-gen-go@latest
go install google.golang.org/grpc/cmd/protoc-gen-go-grpc@latest
```

- 依存パッケージの取得

```bash
go mod tidy
```

#### `.proto` の再生成
`proto/calculator.proto` を編集した場合は次でコードを再生成します。

```bash
protoc --go_out=. --go-grpc_out=. proto/calculator.proto
```

## ビルド

```bash
go build
```

実行ファイル `test_grpc_tavern` が生成されます。すぐにサーバーを起動する場合は次のように実行します。

```bash
go run main.go
```

## テスト

[gRPC ベンチマークツール ghz](https://github.com/bojand/ghz) を利用した設定ファイルが用意されています。サーバーを起動した状態で次を実行すると `Add` メソッドの正常系と `Divide` メソッドの異常系をテストできます。`Add` のテストではリクエストからレスポンスまでの時間 (ms) を計測します。

```bash
# 1つ目のターミナル
go run main.go

# 2つ目のターミナル: 正常系
ghz --config tests/ghz_add.json --format json | jq '.details[0].latency / 1000000'

# 2つ目のターミナル: 異常系
ghz --config tests/ghz_divide_error.json
```

GitHub Actions でもこれらのテストが自動で実行されます。
