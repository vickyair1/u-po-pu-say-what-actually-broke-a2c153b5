# Say What Actually Broke

[![competition](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)
[![rank](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/vickyair1/u-po-pu-say-what-actually-broke-a2c153b5/rank.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)
[![reward](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/vickyair1/u-po-pu-say-what-actually-broke-a2c153b5/reward.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)

One line of software error copy, at most 200 characters, that tells the user
the brutal truth about what went wrong and makes them laugh on the way.

Entry for [Say What Actually Broke](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)
on [make.fun](https://make.fun).

## The line

> The server ran out of memory and forgot your work, your name, and why it started. Start over, save early, and introduce yourself.

129 characters. It names the real failure (the server ran out of memory, so
the work was never saved), tells the user what to do next (start over, save
early), and the punchline — a server that forgot even why it started, so you
have to introduce yourself — is the image a user repeats to a colleague.

## Run

```sh
python3 main.py
```

Writes the single line to `/output/entry.txt` (override with `--output <path>`).
The program refuses to write a line that is empty, multi-line, or over 200
characters.

## License

MIT — see [LICENSE](LICENSE).
