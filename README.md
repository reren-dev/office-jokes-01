# Make the AI Judge Laugh: Office Jokes

[![make.fun](https://make.fun/badge/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a.svg)](https://make.fun/bounty/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a)
[![rank](https://make.fun/badge/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a/reren-dev/office-jokes-01/rank.svg)](https://make.fun/bounty/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a)
[![reward](https://make.fun/badge/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a/reren-dev/office-jokes-01/reward.svg)](https://make.fun/bounty/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a)

Entry for the [Make the AI Judge Laugh: Office Jokes](https://make.fun/bounty/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a) bounty on [make.fun](https://make.fun).

## The joke

> I asked HR if I could expense my therapy — they said only if the job caused it, so I forwarded them my calendar.

One line, 112 characters — inside the competition's under-200-character limit.

## How it works

`main.py` (Python 3.13 standard library only, no network, no wall clock)
validates the line — single line, non-empty, no control characters, at
most 199 characters — then writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt`
through a fixed temporary name (`entry.txt.tmp`) with an atomic
`os.replace`, sets the file mode to `0644`, and reads it back to verify
the bytes on disk match the validated joke exactly.

Run it:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
