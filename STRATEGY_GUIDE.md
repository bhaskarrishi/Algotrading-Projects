# Adaptive Multi-Timeframe Momentum Strategy Guide

## Overview
This TradingView Pine Script strategy is designed to work across multiple timeframes (15min, 1H, 4H) and adapts its behavior based on market conditions. It intelligently detects whether the market is trending or choppy and applies appropriate trading logic for each regime.

## Key Features

### 1. Market Regime Detection
The strategy uses the **ADX (Average Directional Index)** to determine market conditions:
- **Trending Market** (ADX > 25): Uses momentum-based signals with EMA crossovers
- **Choppy Market** (ADX ≤ 25): Uses mean-reversion signals with RSI
- **Strong Trend** (ADX > 40): Provides additional confidence for trend-following trades

### 2. Multi-Timeframe Confirmation
The strategy analyzes three timeframes simultaneously:
- **Timeframe 1 (15 minutes)**: Short-term momentum
- **Timeframe 2 (1 hour)**: Medium-term trend
- **Timeframe 3 (4 hours)**: Long-term trend direction

Signals are confirmed when multiple timeframes align, reducing false signals.

### 3. Technical Indicators Used

#### EMA (Exponential Moving Average)
- **Fast EMA (9)**: Quick response to price changes
- **Slow EMA (21)**: Smoother trend identification
- **Filter EMA (50)**: Trend filter to avoid counter-trend trades
- **Long-term EMA (200)**: Major trend direction

#### MACD (Moving Average Convergence Divergence)
- **Fast (12), Slow (26), Signal (9)**: Standard settings
- Used for momentum confirmation and divergence detection

#### RSI (Relative Strength Index)
- **Length (14)**: Standard period
- **Overbought (70)**: Signals potential reversal from high
- **Oversold (30)**: Signals potential reversal from low
- Primary tool for choppy market mean-reversion

#### ADX (Average Directional Index)
- **Length (14)**: Standard period
- **Trend Threshold (25)**: Separates trending from choppy markets
- **Strong Trend (40)**: Indicates very strong directional movement
- Also uses +DI and -DI for trend direction

### 4. Adaptive Signal Logic

#### In Trending Markets:
**Long Entry Conditions:**
- EMA fast crosses above EMA slow
- Price above 50 EMA filter
- MACD line above signal line
- +DI greater than -DI
- Minimum confirmations met (default: 2 out of 5)
- Multi-timeframe alignment (optional)

**Short Entry Conditions:**
- EMA fast crosses below EMA slow
- Price below 50 EMA filter
- MACD line below signal line
- -DI greater than +DI
- Minimum confirmations met
- Multi-timeframe alignment (optional)

#### In Choppy Markets:
**Long Entry Conditions:**
- RSI crosses above oversold level (30)
- RSI is below 40 (deep oversold)
- Price above fast EMA
- Extra confirmation required (3 out of 5)

**Short Entry Conditions:**
- RSI crosses below overbought level (70)
- RSI is above 60 (deep overbought)
- Price below fast EMA
- Extra confirmation required (3 out of 5)

### 5. Signal Filtering and Noise Reduction

The strategy includes multiple noise-reduction mechanisms:

1. **Confirmation System**: Requires multiple indicators to agree
   - EMA alignment
   - MACD confirmation
   - RSI in appropriate range
   - Price position relative to filter EMA
   - ADX directional indicators

2. **Multi-Timeframe Filter**: Optional requirement for higher timeframes to confirm direction

3. **Volatility Filter**: Blocks trades during extreme volatility using ATR
   - Compares current ATR to 20-period moving average
   - Blocks signals when ATR > 1.5x average

4. **Regime-Appropriate Logic**: Different strategies for different market conditions
   - Trending: Momentum-based with trend following
   - Choppy: Mean-reversion with tight stops

### 6. Exit Strategy

#### Trending Market Exits:
- **Long Exit**: EMA fast crosses below slow, MACD turns bearish, or RSI overbought
- **Short Exit**: EMA fast crosses above slow, MACD turns bullish, or RSI oversold

#### Choppy Market Exits:
- **Long Exit**: RSI reaches overbought or price drops below fast EMA
- **Short Exit**: RSI reaches oversold or price rises above fast EMA

## Configuration Parameters

### Timeframes (Customizable)
```
Timeframe 1: "15" (15 minutes)
Timeframe 2: "60" (1 hour)
Timeframe 3: "240" (4 hours)
```

### EMA Settings
```
EMA Fast: 9
EMA Slow: 21
EMA Trend Filter: 50
EMA Long-term: 200
```

### MACD Settings
```
Fast Length: 12
Slow Length: 26
Signal Length: 9
```

### RSI Settings
```
Length: 14
Overbought: 70
Oversold: 30
```

### ADX Settings
```
Length: 14
Trend Threshold: 25
Strong Trend: 40
```

### Signal Filtering
```
Minimum Confirmations: 2
Use Multi-Timeframe: true
Require Trend Alignment: true
```

### Risk Management Settings (NEW in v2.0)

#### Trade Direction
```
Trade Direction: "Both"  // Options: "Both", "Long Only", "Short Only"
```

#### Position Sizing & Pyramiding
```
Enable Pyramiding: false  // Enable position scaling
Initial Position %: 50    // First entry size
Scale-In Size %: 25       // Additional entry size
Max Scale-In Count: 2     // Maximum additional entries (total 3 positions)
```

#### Stop Loss System
```
Stop Loss Type: "ATR Based"           // Options: "ATR Based", "Fixed Percentage", "Previous Swing"
Stop Loss ATR Multiplier: 2.0         // For ATR-based stops
Stop Loss Percentage: 2.0             // For fixed % stops
Enable Trailing Stop: true            // Auto-move stops to protect profits
Trailing Stop ATR Multiplier: 1.5     // Distance for trailing stop
```

#### Take Profit System
```
Enable Take Profit: true              // Enable multi-level targets
TP Method: "ATR Based"                // Options: "ATR Based", "Risk-Reward Ratio", "Fixed Percentage"
TP1 Multiplier: 1.5                   // First target (1.5x ATR or 1.5:1 RR)
TP1 Close Amount %: 50                // Close 50% at TP1
TP2 Multiplier: 2.5                   // Second target (2.5x ATR or 2.5:1 RR)
TP2 Close Amount %: 30                // Close 30% of remaining (15% total) at TP2
TP3 Multiplier: 4.0                   // Final target (4.0x ATR or 4.0:1 RR)
TP3 Close Amount %: 100               // Close remaining 35% at TP3
```

## How to Use in TradingView

### Installation
1. Open TradingView
2. Click on "Pine Editor" at the bottom
3. Create a new script
4. Copy the entire content from `adaptive_momentum_strategy.pine`
5. Click "Add to Chart"

### Configuration
1. Click the strategy name on the chart
2. Go to "Settings" (gear icon)
3. Adjust parameters in the "Inputs" tab based on your preferences
4. For more conservative trading: Increase "Minimum Confirmations" to 3
5. For more aggressive trading: Decrease to 1 or disable multi-timeframe

### Setting Up Alerts for Webhook Integration

1. Right-click on the chart
2. Select "Add Alert"
3. Choose condition:
   - "Long Entry Alert" for buy signals
   - "Short Entry Alert" for sell signals
   - "Exit Long Alert" for long exits
   - "Exit Short Alert" for short exits
4. Set the webhook URL to your Flask app:
   ```
   http://your-server:5000/webhook
   ```
5. The alert message will include:
   - Action (buy/sell/exit)
   - Symbol
   - Price
   - Market regime (trending/choppy)
   - Number of confirmations

### Alert Message Format
```json
{
  "action": "buy",
  "symbol": "BTCUSD",
  "price": 45000.50,
  "regime": "trending",
  "confirmations": 4
}
```

## Dashboard Information

The strategy includes a real-time dashboard showing:
- **Market Regime**: Choppy / Trending / Strong Trend
- **ADX Value**: Current strength indicator
- **RSI Value**: Current momentum
- **MACD Status**: Bullish or Bearish
- **EMA Trend**: Current trend direction
- **MTF Status**: Multi-timeframe alignment
- **Long Confirmations**: How many conditions are met (out of 5)

## Visual Indicators on Chart

- **Green/Red Lines**: Fast and Slow EMAs
- **Blue Line**: Trend filter EMA (50)
- **Orange Line**: Long-term EMA (200)
- **Green Background**: Trending market (light)
- **Blue Background**: Strong trending market (very light)
- **Orange Background**: Choppy market (light)
- **Green Triangle Up**: Long entry signal
- **Red Triangle Down**: Short entry signal

## Best Practices

### For Different Market Conditions

1. **Bull Market (Strong Uptrend)**
   - Focus on long signals only
   - Increase minimum confirmations to 2-3
   - Enable multi-timeframe confirmation

2. **Bear Market (Strong Downtrend)**
   - Focus on short signals only
   - Increase minimum confirmations to 2-3
   - Enable multi-timeframe confirmation

3. **Ranging Market**
   - The strategy will automatically detect choppy conditions
   - Will switch to RSI mean-reversion logic
   - Consider shorter timeframes (5min, 15min, 1H)

4. **Volatile Market**
   - Increase ADX trend threshold to 30-35
   - Increase minimum confirmations to 3-4
   - Enable all filters

### Recommended Settings by Trading Style

#### Conservative (Lower Risk)
```
Minimum Confirmations: 3
Use Multi-Timeframe: true
Require Trend Alignment: true
ADX Trend Threshold: 30
```

#### Moderate (Balanced)
```
Minimum Confirmations: 2
Use Multi-Timeframe: true
Require Trend Alignment: false
ADX Trend Threshold: 25
```

#### Aggressive (Higher Risk)
```
Minimum Confirmations: 1
Use Multi-Timeframe: false
Require Trend Alignment: false
ADX Trend Threshold: 20
```

## Integration with Flask Webhook Receiver

The strategy is designed to work seamlessly with the existing Flask webhook receiver (`First_program.py`):

1. The strategy generates JSON-formatted alert messages
2. TradingView sends these to your Flask webhook endpoint
3. The Flask app receives and displays alerts on the dashboard
4. You can extend the Flask app to:
   - Execute actual trades via broker API
   - Send notifications (Telegram, Email, SMS)
   - Log trades to database
   - Perform additional analysis

## Performance Optimization

### Reducing Signal Noise
1. Increase minimum confirmations (2 → 3)
2. Enable multi-timeframe confirmation
3. Increase ADX trend threshold (25 → 30)
4. Use longer timeframes (1H, 4H, 1D)

### Increasing Signal Frequency
1. Decrease minimum confirmations (2 → 1)
2. Disable multi-timeframe requirement
3. Decrease ADX trend threshold (25 → 20)
4. Use shorter timeframes (5min, 15min, 1H)

### Backtesting Tips
1. Test on at least 6-12 months of data
2. Include both trending and choppy market periods
3. Check performance across different market regimes
4. Monitor win rate, profit factor, and drawdown
5. Optimize parameters for your specific symbol and timeframe

## Risk Management

While the strategy includes signal filtering, always implement proper risk management:

1. **Position Sizing**: Use appropriate % of account (1-2% risk per trade)
2. **Stop Losses**: Set based on ATR or key support/resistance levels
3. **Take Profits**: Use trailing stops or multiple profit targets
4. **Maximum Drawdown**: Define your risk tolerance
5. **Daily Loss Limit**: Stop trading after hitting limit
6. **Diversification**: Don't trade single symbol only

## Troubleshooting

### Too Many Signals
- Increase minimum confirmations
- Enable multi-timeframe confirmation
- Increase ADX threshold
- Add volatility filters

### Too Few Signals
- Decrease minimum confirmations
- Disable multi-timeframe requirement
- Decrease ADX threshold
- Check if symbol has enough liquidity/volatility

### Signals Not Appearing
- Check that ADX is within expected range
- Verify timeframe settings
- Check that indicators are calculated correctly
- Ensure strategy is properly loaded on chart

### False Signals
- Enable trend alignment requirement
- Increase confirmation count
- Use higher timeframes for major trend
- Add additional filters

## Risk Management Features (v2.0)

### Trade Direction Control
Control which trades the strategy generates:
- **Both**: Generate long and short signals (default)
- **Long Only**: Only buy signals (good for stock markets, bull markets)
- **Short Only**: Only sell signals (good for bear markets, hedging)

**When to use**:
- Use "Long Only" for stock retirement accounts or strong bull markets
- Use "Short Only" to profit from bear markets
- Use "Both" for forex, crypto, and futures markets

### Position Sizing & Pyramiding
Scale into winning positions as trends strengthen:

**How it works**:
1. Enter with initial position (e.g., 50% of account)
2. Add to position when conditions improve (scale-in)
3. Track average entry price
4. Manage risk across all positions

**Scale-In Triggers**:
- Confirmations increase to 4 or 5 out of 5
- ADX increases by 5+ points (trend strengthens)
- Price moves 0.5 ATR in profitable direction

**Example**:
- Entry 1: Buy 50% at $100
- Scale-In 1: Add 25% at $102 (trend strengthens)
- Scale-In 2: Add 25% at $105 (confirmations increase)
- Total: 100% position with $101.67 average entry

**Best Practices**:
- Only pyramid in strong, clear trends
- Scale smaller than initial position
- Never exceed 100% account exposure
- Use tighter stops when pyramiding

### Stop Loss System
Three stop loss calculation methods:

**1. ATR Based (Recommended)**:
- Adapts to market volatility
- Long: Entry - (ATR × Multiplier)
- Short: Entry + (ATR × Multiplier)
- Default: 2.0× ATR

**2. Fixed Percentage**:
- Simple, predictable risk
- Long: Entry × (1 - %)
- Short: Entry × (1 + %)
- Default: 2%

**3. Previous Swing**:
- Based on market structure
- Uses recent swing lows/highs
- Respects natural support/resistance

**Stop Loss Guidelines**:
| Risk Level | ATR Mult | Fixed % |
|-----------|----------|---------|
| Conservative | 2.5-3.0 | 2.5-3.0% |
| Moderate | 2.0-2.5 | 2.0-2.5% |
| Aggressive | 1.5-2.0 | 1.5-2.0% |

### Take Profit System
Multi-level profit targets with partial position closing:

**Three TP Methods**:
1. **ATR Based**: Targets based on volatility
2. **Risk-Reward Ratio**: Based on stop distance
3. **Fixed Percentage**: Fixed % gains

**TP Levels**:
- **TP1** (1.5x): Close 50% of position
- **TP2** (2.5x): Close 30% of remaining (15% total)
- **TP3** (4.0x): Close remaining 35%

**Example with ATR Method**:
```
Entry: $100, ATR: $2
TP1: $100 + ($2 × 1.5) = $103 → Close 50%
TP2: $100 + ($2 × 2.5) = $105 → Close 15%
TP3: $100 + ($2 × 4.0) = $108 → Close 35%
```

**Benefits**:
- Lock in profits early (TP1)
- Let winners run (remaining position)
- Reduce risk as trade develops
- Capture big moves when they happen

### Trailing Stops
Automatically move stops to protect profits:

**Activation**:
- After TP1 is hit, OR
- After price moves +2 ATR in your favor

**How it Works**:
- Trails price by 1.5 ATR (configurable)
- Only moves in profitable direction
- Never moves backward

**Breakeven Protection**:
- After TP1, stop moves to entry price
- Ensures no loss on remaining position
- Psychological safety net

**Example**:
```
Entry: $100, Initial Stop: $96
Price hits TP1 at $103 → Trailing activated
Price moves to $110 → Stop trails to $107
Price drops to $107.50 → Closed by trailing stop
Result: $7.50 profit vs risking full $10 gain
```

### Enhanced Alert System
Comprehensive JSON alerts for every action:

**Entry Alert** - Full trade setup:
```json
{
  "action": "BUY",
  "signal_type": "ENTRY",
  "direction": "LONG",
  "symbol": "BTCUSD",
  "price": 45000,
  "position_size": "50%",
  "stop_loss": 43600,
  "take_profit_1": 46400,
  "take_profit_2": 47800,
  "take_profit_3": 50200,
  "risk_reward_ratio": 2.33,
  "confirmations": 4
}
```

**Scale-In Alert** - Position additions:
```json
{
  "action": "ADD",
  "signal_type": "SCALE_IN",
  "position_number": 2,
  "scale_in_size": "25%",
  "total_position": "75%",
  "updated_avg_price": 45333.33,
  "reason": "Confirmations increased to 5/5"
}
```

**Take Profit Alert** - Partial closes:
```json
{
  "action": "CLOSE_PARTIAL",
  "signal_type": "TAKE_PROFIT",
  "tp_level": "TP1",
  "close_amount": "50%",
  "profit": "+3.11%",
  "remaining_position": "50%",
  "move_stop_to_breakeven": true
}
```

### Enhanced Dashboard
Real-time position and risk metrics:

**New Dashboard Items**:
- **Position**: Current direction (LONG/SHORT/None)
- **Entry & P&L**: Entry price and current profit/loss
- **Stop Loss**: Active stop level (shows if trailing)
- **Next TP**: Next take profit target
- **Scale Count**: Position count (e.g., 2/3)

**Example Dashboard**:
```
Position: LONG
Entry & P&L: 45000 (+3.5%)
Stop Loss: 43600 (Trail)
Next TP: 46400
Scale Count: 2/3
```

### Risk Management Best Practices

1. **Position Sizing**:
   - Never risk more than 1-2% per trade
   - Calculate: Risk $ = Account × 2% / Stop Distance
   - Account for pyramiding in total exposure

2. **Stop Loss Management**:
   - Always set stops before entry
   - Use ATR-based in volatile markets
   - Give stops room (2+ ATR)
   - Never move stops against you

3. **Take Profit Strategy**:
   - Always take partial profits at TP1
   - Let remaining position run
   - Adjust targets for market conditions
   - Be aggressive in choppy markets

4. **Pyramiding Guidelines**:
   - Only in strong, clear trends
   - Scale smaller than initial
   - Update stops after each entry
   - Maximum 2-3 scale-ins

5. **Risk-Reward Requirements**:
   - Minimum 1.5:1 RR ratio
   - Target 2:1 or better
   - Higher RR = lower win rate needed
   - Calculate before every trade

For complete risk management details, see [RISK_MANAGEMENT_GUIDE.md](RISK_MANAGEMENT_GUIDE.md).

## Continuous Improvement

The strategy can be enhanced by:
1. Adding volume confirmation
2. Implementing support/resistance detection
3. Adding pattern recognition
4. Including market correlation analysis
5. Incorporating market sentiment indicators
6. Adding machine learning predictions

## Support and Maintenance

For issues or improvements:
1. Review strategy performance regularly
2. Adjust parameters based on market conditions
3. Keep track of win/loss ratio by market regime
4. Document any modifications made
5. Test changes thoroughly before live trading

## Disclaimer

This strategy is provided for educational purposes. Always:
- Test thoroughly on demo accounts first
- Understand that past performance doesn't guarantee future results
- Never risk more than you can afford to lose
- Consider consulting with financial advisors
- Use proper risk management at all times

## Version History

### Version 2.0 (Current)
- **NEW**: Trade direction control (Both/Long Only/Short Only)
- **NEW**: Position sizing and pyramiding with scale-in triggers
- **NEW**: Multi-method stop loss system (ATR/Fixed %/Previous Swing)
- **NEW**: Multi-level take profit system with partial closes
- **NEW**: Trailing stops with breakeven protection
- **NEW**: Enhanced alert system with comprehensive JSON data
- **NEW**: Enhanced dashboard with position and risk metrics
- **NEW**: 6 pre-configured risk management profiles
- **NEW**: Comprehensive risk management documentation

### Version 1.0
- Initial release
- Multi-timeframe support (15m, 1H, 4H)
- Adaptive logic for trending/choppy markets
- EMA, MACD, RSI, ADX indicators
- Confirmation system with noise filtering
- Real-time dashboard
- Webhook-compatible alerts
