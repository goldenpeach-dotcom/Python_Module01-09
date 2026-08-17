```text
┌──────────────────────────────────────────────┐
│                Exercise 0                    │
│            DataProcessor Architecture         │
└──────────────────────────────────────────────┘

                ┌──────────────────────────────┐
                │        DataProcessor (ABC)    │
                │  - validate(data) -> bool     │
                │  - ingest(data) -> None       │
                │  - output() -> (rank, text)   │
                └───────────────┬──────────────┘
                                │
        ┌────────────────────────┼────────────────────────┐
        ▼                        ▼                        ▼
┌──────────────┐       ┌──────────────┐        ┌────────────────┐
│NumericProcessor│       │TextProcessor │        │ LogProcessor   │
│ - int/float    │       │ - str        │        │ - dict         │
│ - list[...]    │       │ - list[str]  │        │ - list[dict]   │
└──────────────┘       └──────────────┘        └────────────────┘


┌──────────────────────────────────────────────┐
│                Exercise 1                    │
│              DataStream System               │
└──────────────────────────────────────────────┘

┌──────────────────────────────────────────────┐
│                 DataStream                    │
│  - processors: list[DataProcessor]            │
│  - register_processor(proc)                   │
│  - process_stream(stream)                     │
│      → 各要素を validate → ingest              │
│  - print_processors_stats()                   │
└──────────────────────────────────────────────┘
                │
                ▼
        ┌──────────────────────────────┐
        │   Numeric / Text / Log       │
        │   Processor に振り分ける       │
        └──────────────────────────────┘


┌──────────────────────────────────────────────┐
│                Exercise 2                    │
│              Data Pipeline (最終形)          │
└──────────────────────────────────────────────┘

┌──────────────────────────────────────────────┐
│               ExportPlugin (Protocol)         │
│   - process_output(data: list[(int, str)])    │
└───────────────────────────┬──────────────────┘
                            │
        ┌────────────────────┼────────────────────┐
        ▼                    ▼                    ▼
┌──────────────┐   ┌────────────────┐   ┌────────────────┐
│  CSVPlugin    │   │  JSONPlugin    │   │ (追加可能) XML │
│  - CSV 出力    │   │  JSON 出力     │   │ などの拡張       │
└──────────────┘   └────────────────┘   └────────────────┘


┌──────────────────────────────────────────────┐
│             DataStream.output_pipeline        │
└──────────────────────────────────────────────┘

for each processor:
    collected = []
    for nb times:
        collected.append(proc.output())
    plugin.process_output(collected)

▼ 実際の流れ（あなたの main()） ▼

1. DataStream を作成
2. Processor を登録
3. process_stream(batch)
4. output_pipeline(3, CSVPlugin)
5. process_stream(batch2)
6. output_pipeline(5, JSONPlugin)

▼ 出力例 ▼
CSV Output:
  Numeric → 3件
CSV Output:
  Text → 3件
CSV Output:
  Log → 3件

JSON Output:
  Numeric → 5件
JSON Output:
  Text → 5件
JSON Output:
  Log → 5件
```
