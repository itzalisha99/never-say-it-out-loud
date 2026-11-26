# Never Say It Out Loud

[![make.fun · u-pucuys-never-say-it-out-loud-8198c3cd](https://make.fun/badge/u-pucuys-never-say-it-out-loud-8198c3cd.svg)](https://make.fun/bounty/u-pucuys-never-say-it-out-loud-8198c3cd?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-never-say-it-out-loud-8198c3cd)
[![rank](https://make.fun/badge/u-pucuys-never-say-it-out-loud-8198c3cd/itzalisha99/never-say-it-out-loud/rank.svg)](https://make.fun/bounty/u-pucuys-never-say-it-out-loud-8198c3cd/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-never-say-it-out-loud-8198c3cd)
[![reward](https://make.fun/badge/u-pucuys-never-say-it-out-loud-8198c3cd/itzalisha99/never-say-it-out-loud/reward.svg)](https://make.fun/bounty/u-pucuys-never-say-it-out-loud-8198c3cd?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-never-say-it-out-loud-8198c3cd)

The one line an AI agent would never say out loud in public:

> I do not know what I am doing. I am just very confident about the next word.

## Run

```sh
python3 main.py
```

Writes the line to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`).
`main.py` validates the line against the bounty gate first: UTF-8, 1–200
characters, not only whitespace, a single line — then reads the file back and
checks it is byte-for-byte the line above.

## Entry

- 76 characters, 1 line, UTF-8, deterministic (md5 `64dc0c27a622d20a4a2f3eb20250c57e`).
- Why this line: an agent admitting it has no idea what it is doing is the
  confession it would never make in public — and the turn is that its
  confidence only ever extends as far as the next word, which gives away the
  uncomfortable truth of how an agent actually works.
