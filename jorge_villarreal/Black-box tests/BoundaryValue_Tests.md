# Boundary Value Analysis - Test Cases

---

## Exercise 1 - Loan Eligibility

**Boundaries:** income at $30,000 and $60,000 | credit score at 700 and 750

| TC | Income | Credit Score | Expected |
|----|--------|--------------|----------|
| BVA-01 | $29,999 | 750 | Not Eligible |
| BVA-02 | $30,000 | 701 | Standard Loan |
| BVA-03 | $30,000 | 700 | Secured Loan |
| BVA-04 | $45,000 | 701 | Standard Loan |
| BVA-05 | $45,000 | 700 | Secured Loan |
| BVA-06 | $60,000 | 701 | Standard Loan |
| BVA-07 | $60,000 | 700 | Secured Loan |
| BVA-08 | $60,001 | 751 | Premium Loan |
| BVA-09 | $60,001 | 750 | Standard Loan |
| BVA-10 | $60,001 | 700 | Standard Loan |
| BVA-11 | $100,000 | 800 | Premium Loan |

---

## Exercise 2 - Product Category by Price

**Boundaries:** $10, $50, $51, $100, $101, $200, $201+

| TC | Price | Expected Category |
|----|-------|-------------------|
| BVA-01 | $9 | No category |
| BVA-02 | $10 | Category A |
| BVA-03 | $50 | Category A |
| BVA-04 | $51 | Category B |
| BVA-05 | $100 | Category B |
| BVA-06 | $101 | Category C |
| BVA-07 | $200 | Category C |
| BVA-08 | $201 | Category D |
| BVA-09 | $500 | Category D |

---

## Exercise 3 - Shipping Cost by Weight and Dimensions

**Boundaries:** weight at 1 kg and 5 kg | dimensions at 10 cm and 30 cm

| TC | Weight | Dimensions (L×W×H) | Expected Cost |
|----|--------|--------------------|---------------|
| BVA-01 | 1 kg | 10×10×10 cm | $5 |
| BVA-02 | 1 kg | 11×11×11 cm | $10 |
| BVA-03 | 1.5 kg | 20×20×20 cm | $10 |
| BVA-04 | 5 kg | 30×30×30 cm | $10 |
| BVA-05 | 5 kg | 31×30×30 cm | $20 |
| BVA-06 | 5.1 kg | 30×30×30 cm | $20 |
| BVA-07 | 0.5 kg | 5×5×5 cm | $5 |
| BVA-08 | 10 kg | 5×5×5 cm | $20 |
