# Remaining life: the rate decision

[![CI](https://github.com/felipearocha/integrity-weekly-00-remaining-life-the-rate-decision/actions/workflows/ci.yml/badge.svg)](https://github.com/felipearocha/integrity-weekly-00-remaining-life-the-rate-decision/actions/workflows/ci.yml)

Week of 2026-11-10 to 2026-11-13. Working notes on one integrity engineering problem: the posts, the code behind the numbers, and tests that hold the code to a hand calculation.

## Run it

```
pip install -r requirements-dev.txt
pytest -q
python code/two_rates.py
```

Python 3.11 or newer.

## Code

| File | What it computes |
|---|---|
| [`code/two_rates.py`](code/two_rates.py) | Remaining life of one thickness monitoring location from two corrosion rates. |

Each script states its basis in the docstring, runs on synthetic data, and checks its own result against a hand calculation. The tests also confirm the printed output is the one published.

## Posts

| Day | Post | Format |
|---|---|---|
| Tuesday | [The Line That Doubles Your Remaining Life](posts/157_two_rates_code.md) | single image |
| Wednesday | [Wet H2S Damage Is Four Problems, Not One](posts/158_wet_h2s_damage.md) | single image |
| Thursday | [One P&ID Sheet In, a Line List Out](posts/159_pid_to_line_list.md) | single image |
| Friday | [What the CSV Can't Tell You](posts/160_what_the_csv_cant_tell.md) | text-only |

## Scope and limits

- All data and drawings are synthetic. No plant, tag or operating data from any facility.
- The code is a worked example for engineers, not a certified calculation. Confirm every requirement against the edition of the standard that governs your equipment.
- Short quotations from standards are identified with their section. Standards are the property of their publishers and are not reproduced here.

## License

MIT for the code. See [LICENSE](LICENSE).
