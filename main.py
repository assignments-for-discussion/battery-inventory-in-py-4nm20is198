def count_batteries_by_health(present_capacities):
  SOH = []
  h = f = e = 0
  for i in present_capacities:
    s = 100 * (int(i)/120)
    SOH.append(s)
  for j in SOH:
    if j>80:
      h = h + 1
    if j<62:
      f = f + 1
    else:
      e = e + 1
  return {
    "healthy": h,
    "exchange": e,
    "failed": f
  }


def test_bucketing_by_health():
  print("Counting batteries by SoH...\n")
  present_capacities = [113, 116, 80, 95, 92, 70]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 2)
  assert(counts["exchange"] == 3)
  assert(counts["failed"] == 1)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_health()
