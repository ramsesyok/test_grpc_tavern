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

### テスト用 Python 環境

Tavern による gRPC テストを実行するには Python と tavern-grpc プラグインが必要です。tavern-grpc は古い pytest に依存するため、Python 3.11 以前を推奨します。

```bash
python -m pip install tavern-grpc
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

サーバーを起動した状態で別ターミナルからテストを実行します。

```bash
# 1つ目のターミナル
go run main.go

# 2つ目のターミナル
pytest tests/calculator.tavern.yaml
```

Tavern テストでは `tests/` 配下の YAML 定義に従い gRPC 経由で計算結果を検証します。
