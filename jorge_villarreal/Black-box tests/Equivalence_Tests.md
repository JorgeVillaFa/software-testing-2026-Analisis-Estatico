# Equivalence Partitioning - Test Cases

---

## Exercise 1 - Credit Card Number Validation

**Valid partition:** length 13–16, only digits
**Invalid partitions:** too short (<13), too long (>16), non-numeric characters

| TC | Input | Expected |
|----|-------|----------|
| EP-01 | `4111111111111` (13 digits) | Valid |
| EP-02 | `4111111111111111` (16 digits) | Valid |
| EP-03 | `41111111111` (11 digits) | Invalid |
| EP-04 | `41111111111111111` (17 digits) | Invalid |
| EP-05 | `4111abcd11111` (letters) | Invalid |
| EP-06 | `4111-1111-1111` (special chars) | Invalid |
| EP-07 | `` (empty) | Invalid |

---

## Exercise 2 - Date Validation

**Valid partitions:** year 1900–2100, month 1–12, day 1–31
**Invalid partitions:** out of range for each field

| TC | Year | Month | Day | Expected |
|----|------|-------|-----|----------|
| EP-01 | 2000 | 6 | 15 | Valid |
| EP-02 | 1899 | 6 | 15 | Invalid (year too low) |
| EP-03 | 2101 | 6 | 15 | Invalid (year too high) |
| EP-04 | 2000 | 0 | 15 | Invalid (month too low) |
| EP-05 | 2000 | 13 | 15 | Invalid (month too high) |
| EP-06 | 2000 | 6 | 0 | Invalid (day too low) |
| EP-07 | 2000 | 6 | 32 | Invalid (day too high) |

---

## Exercise 3 - Flight Booking Eligibility

**Valid partitions:** age 18–65, frequent_flyer true/false
**Invalid partitions:** age <18, age >65

| TC | Age | Frequent Flyer | Expected |
|----|-----|----------------|----------|
| EP-01 | 30 | True | Eligible |
| EP-02 | 30 | False | Eligible |
| EP-03 | 17 | True | Not Eligible |
| EP-04 | 66 | True | Not Eligible |
| EP-05 | 17 | False | Not Eligible |

---

## Exercise 4 - URL Validation

**Valid partition:** starts with `http://` or `https://`, length ≤ 255
**Invalid partitions:** wrong prefix, length > 255

| TC | Input | Expected |
|----|-------|----------|
| EP-01 | `http://example.com` | Valid |
| EP-02 | `https://example.com` | Valid |
| EP-03 | `ftp://example.com` | Invalid (wrong prefix) |
| EP-04 | `example.com` | Invalid (no prefix) |
| EP-05 | `https://` + `a` × 249 (256 chars total) | Invalid (too long) |
| EP-06 | `https://` + `a` × 247 (255 chars total) | Valid |
| EP-07 | `` (empty) | Invalid |
