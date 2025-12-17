# Algotrading-Projects
Algo Trading Projects

## Overview
This repository contains algorithmic trading tools and strategies for automated trading with TradingView.

## Components

### 1. Flask Webhook Receiver (`First_program.py`)
A Flask web application that receives trading alerts from TradingView via webhooks and displays them on a dashboard.

**Features:**
- Real-time alert reception from TradingView
- Web dashboard to view alerts with timestamps
- JSON webhook endpoint at `/webhook`
- Easy integration with TradingView alert system

**Usage:**
```bash
python First_program.py
```
Access the dashboard at: `http://localhost:5000`

### 2. Adaptive Multi-Timeframe Momentum Strategy (`adaptive_momentum_strategy.pine`)
A sophisticated Pine Script strategy for TradingView that adapts to market conditions.

**Key Features:**
- **Multi-Timeframe Analysis**: Works on 15min, 1H, and 4H charts simultaneously
- **Market Regime Detection**: Automatically identifies trending vs choppy markets using ADX
- **Adaptive Logic**: Uses different strategies for different market conditions
  - Trending Markets: EMA crossovers with MACD confirmation
  - Choppy Markets: RSI mean-reversion signals
- **Multiple Technical Indicators**:
  - EMA (9, 21, 50, 200) for trend identification
  - MACD (12, 26, 9) for momentum confirmation
  - RSI (14) for overbought/oversold conditions
  - ADX (14) for market regime detection
- **Signal Filtering**: Multiple confirmation system to reduce noise
- **Volatility Filter**: Blocks trades during extreme volatility
- **Real-time Dashboard**: Shows market regime, indicator values, and confirmations
- **Webhook Alerts**: JSON-formatted alerts ready for webhook integration

**Quick Start:**
1. Open TradingView Pine Editor
2. Copy content from `adaptive_momentum_strategy.pine`
3. Add to chart
4. Configure parameters in Settings
5. Set up alerts with webhook URL pointing to your Flask app

See [STRATEGY_GUIDE.md](STRATEGY_GUIDE.md) for complete documentation.

## Installation

### Prerequisites
- Python 3.7+
- TradingView account (for strategy)

### Setup
```bash
# Install Python dependencies
pip install -r requirements.txt

# Run the Flask webhook receiver
python First_program.py
```

## Strategy Configuration

### Recommended Settings

**Conservative Trading:**
- Minimum Confirmations: 3
- Multi-Timeframe: Enabled
- ADX Threshold: 30

**Moderate Trading:**
- Minimum Confirmations: 2
- Multi-Timeframe: Enabled
- ADX Threshold: 25

**Aggressive Trading:**
- Minimum Confirmations: 1
- Multi-Timeframe: Disabled
- ADX Threshold: 20

## TradingView Alert Setup

1. Add the strategy to your chart
2. Right-click → Add Alert
3. Choose alert condition (Long Entry, Short Entry, etc.)
4. Set webhook URL: `http://your-server:5000/webhook`
5. The strategy automatically formats alerts as JSON

**Alert Format:**
```json
{
  "action": "buy",
  "symbol": "BTCUSD",
  "price": 45000.50,
  "regime": "trending",
  "confirmations": 4
}
```

## Files

- `First_program.py` - Flask webhook receiver application
- `adaptive_momentum_strategy.pine` - TradingView Pine Script strategy
- `STRATEGY_GUIDE.md` - Complete strategy documentation
- `requirements.txt` - Python dependencies
- `templates/index.html` - Dashboard HTML template
- `Dockerfile` - Docker configuration
- `compose.yaml` - Docker Compose configuration

## Docker Deployment

```bash
# Build and run with Docker Compose
docker-compose up -d

# Access the dashboard
# http://localhost:5000
```

## Features Comparison

| Feature | Trending Market | Choppy Market |
|---------|----------------|---------------|
| Primary Indicator | EMA Crossover | RSI Mean-Reversion |
| Confirmation | MACD + ADX | Extra confirmations required |
| Risk Level | Moderate | Higher (tight stops) |
| Signal Frequency | Lower | Higher |
| Best Timeframe | 1H, 4H, Daily | 15min, 1H |

## Risk Management

Always implement proper risk management:
- Position sizing (1-2% per trade)
- Stop losses based on ATR
- Maximum daily loss limits
- Diversification across symbols
- Regular performance monitoring

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is open source and available for educational purposes.

## Disclaimer

This software is for educational purposes only. Trading involves risk. Always test strategies thoroughly on demo accounts before live trading. Past performance does not guarantee future results.
