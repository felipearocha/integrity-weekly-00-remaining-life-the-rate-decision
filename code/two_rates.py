"""Remaining life of one thickness monitoring location from two corrosion rates.

Basis: API 510, 11th Edition. Long term and short term corrosion rate per 7.1.1.1, remaining
life per 7.2.1. Rate selection is the inspector's call under 7.1.1.2; max() here is only a
conservative screening default.

Units: thickness in mm, time in years, rate in mm/yr.
Limits: thinning only, one location, needs at least two readings on different dates. The
readings are synthetic: a steady rate plus measurement scatter.
"""
from datetime import date

THICKNESS_MM = [11.80, 11.60, 11.35, 11.03, 10.79, 10.53, 10.32, 10.05, 9.83, 9.48, 9.36]
readings = [(date(2015 + k, 3, 15), t) for k, t in enumerate(THICKNESS_MM)]
T_REQUIRED = 6.40  # mm


def rate(earlier, later):
    years = (later[0] - earlier[0]).days / 365.25
    return (earlier[1] - later[1]) / years


last = readings[-1]
long_term = rate(readings[0], last)
short_term = rate(readings[-2], last)
governing = max(long_term, short_term)  # a default, not a rule

rates = {"long term": long_term, "short term": short_term}
for name, r in rates.items():
    life = (last[1] - T_REQUIRED) / r
    print(f"{name:<11}{r:.3f} mm/yr  {life:5.1f} years")
assert len(readings) == 11
assert abs(long_term - (11.80 - 9.36) / 10.0) < 1e-3
assert abs((last[1] - T_REQUIRED) / long_term - 12.1) < 0.05
assert abs((last[1] - T_REQUIRED) / short_term - 24.6) < 0.05
assert governing == long_term
