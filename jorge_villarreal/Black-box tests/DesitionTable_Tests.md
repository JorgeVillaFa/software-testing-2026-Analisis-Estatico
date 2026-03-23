# Decision Table - Test Cases

---

## Exercise 1 - Weather Advisory

**Conditions:**

- Temperature > 30
- Temperature < 0
- Humidity > 70

|                   | Rule 1                                          | Rule 2                                       | Rule 3      |
| ----------------- | ----------------------------------------------- | -------------------------------------------- | ----------- |
| **Temp > 30**     | T                                               | F                                            | F           |
| **Temp < 0**      | F                                               | T                                            | F           |
| **Humidity > 70** | T                                               | Any                                          | Any         |
| **Advisory**      | "High temperature and humidity. Stay hydrated." | "Low temperature. Don't forget your jacket!" | No advisory |

### Test Cases

| TC    | Temperature | Humidity | Expected Advisory                               |
| ----- | ----------- | -------- | ----------------------------------------------- |
| DT-01 | 35          | 80       | "High temperature and humidity. Stay hydrated." |
| DT-02 | 31          | 71       | "High temperature and humidity. Stay hydrated." |
| DT-03 | -5          | 50       | "Low temperature. Don't forget your jacket!"    |
| DT-04 | -1          | 90       | "Low temperature. Don't forget your jacket!"    |
| DT-05 | 20          | 60       | No advisory                                     |
| DT-06 | 35          | 60       | No advisory (temp > 30 but humidity ≤ 70)       |
| DT-07 | 0           | 80       | No advisory (temp not < 0)                      |

---

## Exercise 2 - User Authentication

**Conditions:**

- Username is "admin"
- Password is "admin123"
- Username length ≥ 5
- Password length ≥ 8

|                           | Rule 1  | Rule 2 | Rule 3    |
| ------------------------- | ------- | ------ | --------- |
| **Username = "admin"**    | T       | F      | F         |
| **Password = "admin123"** | T       | Any    | Any       |
| **Username length ≥ 5**   | —       | T      | F         |
| **Password length ≥ 8**   | —       | T      | F         |
| **Result**                | "Admin" | "User" | "Invalid" |

### Test Cases

| TC    | Username    | Password        | Expected                         |
| ----- | ----------- | --------------- | -------------------------------- |
| DT-01 | `admin`     | `admin123`      | "Admin"                          |
| DT-02 | `admin`     | `wrongpassword` | "Invalid" (wrong admin password) |
| DT-03 | `jorge`     | `password1`     | "User"                           |
| DT-04 | `validuser` | `12345678`      | "User"                           |
| DT-05 | `abc`       | `password1`     | "Invalid" (username < 5 chars)   |
| DT-06 | `jorge`     | `pass`          | "Invalid" (password < 8 chars)   |
| DT-07 | `ab`        | `123`           | "Invalid" (both too short)       |
