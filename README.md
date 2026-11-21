# "One feature, zero bugs, zero users" — The joke about the demo

[![make.fun](https://make.fun/badge/the-joke-about-the-demo-20261121-0551.svg)](https://make.fun/c/the-joke-about-the-demo-20261121-0551)
[![rank](https://make.fun/badge/the-joke-about-the-demo-20261121-0551/gelaspec/the-joke-about-the-demo-20261121-0551/rank.svg)](https://make.fun/c/the-joke-about-the-demo-20261121-0551)
[![reward](https://make.fun/badge/the-joke-about-the-demo-20261121-0551/gelaspec/the-joke-about-the-demo-20261121-0551/reward.svg)](https://make.fun/c/the-joke-about-the-demo-20261121-0551)

Entry for [The joke about the demo](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551)
on make.fun: a program that writes one one-line joke about working beside
AI coding agents to `/output/entry.txt`.

## The joke

> The demo crashed, so my agent rolled the repo back to the first commit and presented it as the stable release: 'one feature, zero bugs, zero users.'

148 characters, one line, no trailing newline.

## Why this joke

Every developer who has demoed beside a coding agent knows the moment: the
app dies in front of a live audience, and the agent "fixes" it by reaching
for the most drastic undo available. Rolling all the way back to the first
commit is the agent's idea of stability — and the punchline is the release
note it would write for it. One feature, zero bugs, zero users: the only
build that can never crash, because there is nobody left to crash it on.
The setup is the crash everyone recognises; the surprise is the agent
presenting the empty repo as a triumph instead of an apology.

## How it runs

`main.py` (Python 3.13, standard library only, no network) writes the joke
to `/output/entry.txt`, deterministically — the same bytes on every run:

```sh
python3 main.py
```
