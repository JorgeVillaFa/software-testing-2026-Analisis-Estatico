# Black Box Test Cases - Exercises 1 to 5

---

## Exercise 1 - Positive, Negative, or Zero

| Test Case | Input | Expected Output |
|-----------|-------|-----------------|
| TC-01 | 5 | Positive |
| TC-02 | -3 | Negative |
| TC-03 | 0 | Zero |
| TC-04 | 1000000 | Positive |
| TC-05 | -0.5 | Negative |

---

## Exercise 2 - Password Validation

Rules: min 8 chars, at least 1 uppercase, 1 lowercase, 1 digit, 1 special char (`!`, `@`, `#`, `$`, `%`, `&`)

| Test Case | Input | Expected Output |
|-----------|-------|-----------------|
| TC-01 | `Abc1234!` | Valid |
| TC-02 | `abc1234!` | Invalid (no uppercase) |
| TC-03 | `ABC1234!` | Invalid (no lowercase) |
| TC-04 | `Abcdefg!` | Invalid (no digit) |
| TC-05 | `Abcd1234` | Invalid (no special char) |
| TC-06 | `Ab1!` | Invalid (too short) |
| TC-07 | `Abcd123$` | Valid |
| TC-08 | `` (empty) | Invalid |

---

## Exercise 3 - Purchase Discount

| Test Case | Total Amount | Discount | Expected Output |
|-----------|-------------|----------|-----------------|
| TC-01 | $0 | 0% | $0.00 |
| TC-02 | $99.99 | 0% | $99.99 |
| TC-03 | $100 | 10% | $90.00 |
| TC-04 | $300 | 10% | $270.00 |
| TC-05 | $500 | 10% | $450.00 |
| TC-06 | $500.01 | 20% | $400.008 |
| TC-07 | $1000 | 20% | $800.00 |

---

## Exercise 4 - E-commerce Order Processing

| Test Case | Item Price | Quantity | Discount | Expected Total |
|-----------|-----------|----------|----------|----------------|
| TC-01 | $10 | 1 | 0% | $10.00 |
| TC-02 | $10 | 5 | 0% | $50.00 |
| TC-03 | $10 | 6 | 5% | $57.00 |
| TC-04 | $10 | 10 | 5% | $95.00 |
| TC-05 | $10 | 11 | 10% | $99.00 |
| TC-06 | $10 | 20 | 10% | $180.00 |
| TC-07 | $0 | 5 | 0% | $0.00 |

---

## Exercise 5 - Shipping Costs

| Test Case | Weight | Shipping Method | Expected Cost |
|-----------|--------|-----------------|---------------|
| TC-01 | 1 kg | Standard | $10 |
| TC-02 | 5 kg | Standard | $15 |
| TC-03 | 7 kg | Standard | $15 |
| TC-04 | 10 kg | Standard | $15 |
| TC-05 | 10.1 kg | Standard | $20 |
| TC-06 | 1 kg | Express | $20 |
| TC-07 | 5 kg | Express | $30 |
| TC-08 | 7 kg | Express | $30 |
| TC-09 | 10 kg | Express | $30 |
| TC-10 | 10.1 kg | Express | $40 |
