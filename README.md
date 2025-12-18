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

### 2. Adaptive Multi-Timeframe Momentum Strategy v2.0 (`adaptive_momentum_strategy.pine`)
A sophisticated Pine Script strategy for TradingView that adapts to market conditions with professional-grade risk management.

**Core Features:**
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

**NEW in v2.0 - Professional Risk Management:**
- **Trade Direction Control**: Long Only, Short Only, or Both
- **Position Sizing & Pyramiding**: Scale into winning positions with configurable entry sizes
- **Advanced Stop Loss System**: 
  - ATR-based stops (adapts to volatility)
  - Fixed percentage stops
  - Previous swing stops
  - Trailing stops with breakeven protection
- **Multi-Level Take Profits**: 
  - 3 configurable TP levels
  - Partial position closing (50%, 30%, 20%)
  - ATR-based, Risk-Reward, or Fixed % methods
- **Enhanced Dashboard**: Real-time P&L, position info, stop/target levels
- **Comprehensive Alerts**: JSON alerts with full trade details for automation
- **Scale-In Triggers**: Automatic position additions based on:
  - Confirmation increases
  - Trend strengthening (ADX)
  - Favorable price movement

See [RISK_MANAGEMENT_GUIDE.md](RISK_MANAGEMENT_GUIDE.md) for complete risk management documentation.

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

### Core Strategy Files
- `adaptive_momentum_strategy.pine` - TradingView Pine Script strategy v2.0
- `strategy_configs.json` - Pre-configured strategy profiles with risk management settings

### Documentation
- `README.md` - This file (overview and quick start)
- `STRATEGY_GUIDE.md` - Complete strategy documentation and technical details
- `RISK_MANAGEMENT_GUIDE.md` - **NEW** Comprehensive risk management guide
- `QUICK_START.md` - 5-minute setup guide for beginners
- `VALIDATION_CHECKLIST.md` - Testing and validation procedures
- `IMPLEMENTATION_SUMMARY.md` - Technical implementation details

### Integration
- `First_program.py` - Flask webhook receiver application
- `requirements.txt` - Python dependencies
- `templates/index.html` - Dashboard HTML template

### Deployment
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

## Risk Management (v2.0)

The strategy now includes built-in professional risk management:

### Configurable Features
- **Position Sizing**: Initial position and scale-in percentages
- **Stop Loss**: ATR-based, Fixed %, or Previous Swing
- **Take Profit**: Multi-level targets (TP1, TP2, TP3)
- **Trailing Stops**: Automatic profit protection
- **Pyramiding**: Scale into winning positions
- **Trade Direction**: Long Only, Short Only, or Both

### Risk Management Presets
Choose from 6 pre-configured profiles in `strategy_configs.json`:
1. **Conservative**: 33% position, 2.5 ATR stops, 2:1 RR targets
2. **Moderate**: 50% position, 2.0 ATR stops, pyramiding enabled
3. **Aggressive**: 60% position, 1.5 ATR stops, 3x scale-ins
4. **Crypto Volatile**: 40% position, 3.0 ATR stops for high volatility
5. **Forex Stable**: 50% position, optimized for forex pairs
6. **Stocks Daily**: Long-only, optimized for stock markets

### Best Practices
- Never risk more than 1-2% of account per trade
- Use ATR-based stops in volatile markets
- Always take partial profits at TP1 (50%)
- Enable trailing stops to protect gains
- Test thoroughly on demo before live trading

See [RISK_MANAGEMENT_GUIDE.md](RISK_MANAGEMENT_GUIDE.md) for detailed instructions.

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is open source and available for educational purposes.

## Disclaimer

This software is for educational purposes only. Trading involves risk. Always test strategies thoroughly on demo accounts before live trading. Past performance does not guarantee future results.
