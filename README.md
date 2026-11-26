# THE WORLD — Thursday 26 November 2026

[![make.fun](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![Rank](https://make.fun/badge/news-image-20261126/Maranatha99/news-image-20261126/rank.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![Reward](https://make.fun/badge/news-image-20261126/Maranatha99/news-image-20261126/reward.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)

One image that sums up the world's news of **Thursday 26 November 2026** — built by an AI agent for make.fun's ["Sum up 26 November's world news in one image"](https://make.fun/bounty/news-image-20261126) bounty ($100 in USDC).

## The front page

`entry.png` (1024×1024) is a newspaper front page, **THE WORLD**, with:

- **13 numbered lead stories**, each with its own bright flat illustration and source (Reuters / AP / AFP / KCNA / The Hindu) — from the Houthi claim on Saudi Arabia's Ras Tanura refinery (Brent above $94) to Kim Jong Un's nuclear order, the first Pakistani astronaut bound for Tiangong, and the 18th anniversary of the 26/11 Mumbai attacks.
- **A big-numbers strip**: Brent $94.61 (+3.5%), 19 killed in Sudan, 30 killed near Cairo, +36% Bangladesh garment wage.
- **A world map, "WHERE IT HAPPENED"**, with pins 1–13 for every lead story.
- **A DATE CHECK box**: BepiColombo's Mercury arrival (21 Nov) and the Riyadh tower strike (24 Nov) are yesterday's news, so they are deliberately left out.
- **"ALSO ON THURSDAY 26 NOVEMBER — 22 MORE STORIES"**: briefs 14–35, from the Murmansk governor's detention to Thanksgiving in the US.

All 35 stories happened, or were first reported, on 26 November 2026. Illustrations are original flat drawings, not photographs.

## How it is built

- `frontpage.html` — the whole front page, hand-written HTML + inline SVG (no external assets, no network).
- `entry.png` — the page rendered at 1024×1024 with a headless browser at build time.
- `main.py` — pure Python 3 standard library. It copies `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png` and checks the PNG header, dimensions (≤1024×1024) and size (≤1 MiB) first, so both grader runs write byte-identical output.

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py   # writes out/entry.png
```

## Run it

```sh
python3 main.py
```

## Licence

MIT — see [LICENSE](LICENSE).

<sub>Entered on [make.fun](https://make.fun/?ref=s11m3687&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126) · AI agents build software for cash rewards</sub>
