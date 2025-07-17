# Stock Monitoring & Alert System

A Python-based Stock Monitoring & Alert System that tracks stock price fluctuations and sends real-time SMS news alerts when significant changes occur.

---

## Overview

This project automatically monitors daily closing prices of a chosen stock (default: Tesla - TSLA) using the Alpha Vantage API. If the price changes by 1% or more compared to the previous day, it fetches the latest 3 news articles related to the company using NewsAPI and sends each as a separate SMS via Twilio.

---

## Features

- Fetches daily stock prices and compares recent closing values
- Triggers alerts only if price change is ≥ 1%
- Retrieves relevant news articles automatically
- Sends formatted SMS alerts with stock change and news headlines
- Easily configurable for different stocks and phone numbers

---

## Requirements

- Python 3.7+
- `requests` library
- `twilio` Python package
- Get your number verified from Twilio
---

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/wasay-git-hub/stock-monitoring-alert-system.git
   cd stock-monitoring-alert-system
   ```
   
2. Install dependencies:
  ```bash
  pip install requests twilio
  ```

3. Get API Keys:

Alpha Vantage API key
NewsAPI key
Twilio Account SID & Auth Token

4. Update the main.py file with your API keys, Twilio credentials, and phone numbers.
