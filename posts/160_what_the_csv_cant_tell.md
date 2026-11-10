# What the CSV Can't Tell You

Friday 2026-11-13

A short term rate drops to half of the long term rate. The CSV can't tell you why.

That answer lives outside the thickness data. API 510 7.1.1.2 says the inspector, with a corrosion specialist, "shall select the corrosion rate that best reflects the current conditions". It then lists what to consider, and a few of those checks do most of the work.

Did the process change? Water wetting, chlorides, a pH shift. If it did, the start of that new environment may be the right starting point for your rate, and 7.1.1.1 allows for that.

Is the damage general or localized? One grid point says little about a local attack sitting next to it.

Was the last interval an episodic event, and was the cause corrected?

Is scale protecting the wall for now? Higher velocity can strip it.

Then the boring one, which isn't on that list. Same probe, same spot, same temperature correction? A difference of a tenth of a millimetre can be plain scatter.

None of this fits in a spreadsheet cell or a Python function, and that's fine. Let the code do the arithmetic, so the time goes to these questions.

Which of these has actually changed your rate selection on a real location?

## Requirements quoted

> "shall select the corrosion rate that best reflects the current conditions"
>
> API 510, 7.1.1.2

## Note

API 510, 11th Edition, sections behind this week's posts: 7.1.1.1 long term and short term rate, 7.1.1.2 rate selection, 7.2.1 remaining life, 6.5.1 inspection interval.

Confirm them against your edition.
