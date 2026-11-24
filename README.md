# makefun-u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85

[![make.fun · u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85](https://make.fun/badge/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85.svg)](https://make.fun/bounty/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85?utm_source=github&utm_medium=readme&utm_campaign=u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85)
[![rank](https://make.fun/badge/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85/Tiiashtf/makefun-u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85/rank.svg)](https://make.fun/bounty/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85)
[![reward](https://make.fun/badge/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85/Tiiashtf/makefun-u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85/reward.svg)](https://make.fun/bounty/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85?utm_source=github&utm_medium=readme&utm_campaign=u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85)
[![license: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![python 3.13](https://img.shields.io/badge/python-3.13-blue)](main.py)

Entry for the make.fun bounty
[Warning Label for Humans: One Line, Big Laugh](https://make.fun/bounty/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85):
a program that writes one funny single-line safety warning label for
human beings, at most 160 characters, to `/output/entry.txt`.

## The line

> WARNING: This human will say 'we should catch up soon' and mean it for eleven years. No action required.

104 characters — inside the 1–160 character gate.

The joke is one idea: humans promise to meet up and then never do, for
years. It is true of people in general, it sounds like a real printed
label ("WARNING:", "No action required"), and the turn lands in the last
three words — a deadpan label shrug at a decade of good intentions.

## Run it

```sh
python3 main.py
```

Writes `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`),
deterministically — the same bytes on every run. Stdlib only, no network.
The output directory itself is never removed, only its contents.
