# SARIMA

import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

data = pd.read_csv("AirPassengers.csv")

df = pd.Series(data["#Passengers"])
df.index = pd.to_datetime(data["Month"])

train_data = df[0:-12]
test_data = df[-12:-1]

dec = sm.tsa.seasonal_decompose(train_data)

plt.plot(dec.seasonal)

plt.plot(dec.trend)

plt.plot(dec.resid)

sarima = sm.tsa.SARIMAX(
    train_data,
    order=(3, 1, 2),
    seasonal_order=(1, 1, 1, 12),
    enforce_stationarity=False,
    enforce_invertibility=False,
).fit()

print(sarima.aic)

pred = sarima.predict("1960-01-01", "1960-12-01")
plt.plot(df)
plt.plot(pred, "red")
