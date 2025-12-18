# Risk Management Guide - Adaptive Momentum Strategy v2.0

## Overview
This comprehensive guide covers all risk management features available in the Adaptive Multi-Timeframe Momentum Strategy version 2.0. These features are designed to protect your capital, optimize position sizing, and maximize risk-adjusted returns.

## Table of Contents
1. [Trade Direction Control](#trade-direction-control)
2. [Position Sizing & Pyramiding](#position-sizing--pyramiding)
3. [Stop Loss System](#stop-loss-system)
4. [Take Profit System](#take-profit-system)
5. [Trailing Stops](#trailing-stops)
6. [Alert System](#alert-system)
7. [Dashboard Metrics](#dashboard-metrics)
8. [Best Practices](#best-practices)
9. [Configuration Examples](#configuration-examples)

---

## Trade Direction Control

### Overview
Control which types of trades the strategy generates based on market outlook or personal preference.

### Options
- **Both** (Default): Generate both long and short signals
- **Long Only**: Only generate buy signals (good for stock markets or bull markets)
- **Short Only**: Only generate sell signals (good for bear markets)

### When to Use Each Setting

#### Both Directions
- **Best for**: Forex, crypto, futures markets
- **Market conditions**: Any market environment
- **Advantages**: Maximum opportunity capture
- **Considerations**: Requires skill in both directions

#### Long Only
- **Best for**: Stock markets, retirement accounts, bullish trends
- **Market conditions**: Bull markets, strong uptrends
- **Advantages**: Aligns with natural market bias, simpler psychology
- **Considerations**: Misses downside opportunities

#### Short Only
- **Best for**: Bear markets, hedging strategies
- **Market conditions**: Bear markets, strong downtrends
- **Advantages**: Profit from declines
- **Considerations**: Higher risk, against long-term market bias

### Configuration
```pinescript
tradeDirection = "Both"  // Change to "Long Only" or "Short Only"
```

---

## Position Sizing & Pyramiding

### Overview
Pyramiding allows you to add to winning positions as the trend strengthens, scaling into trades incrementally rather than going all-in at once.

### Key Parameters

#### Enable Pyramiding
- **Default**: false (disabled for backward compatibility)
- **Purpose**: Allows multiple entries into the same position
- **When enabled**: Strategy can add to positions up to maxScaleIns times

#### Initial Position Size
- **Default**: 50% of account equity
- **Range**: 1% to 100%
- **Purpose**: First entry position size
- **Conservative**: 25-33%
- **Moderate**: 50%
- **Aggressive**: 60-75%

#### Scale-In Size
- **Default**: 25% of account equity
- **Range**: 1% to 100%
- **Purpose**: Additional position size for each scale-in
- **Best practice**: Typically half of initial size or less

#### Maximum Scale-In Count
- **Default**: 2 (allowing 3 total positions)
- **Range**: 0 to 5
- **Purpose**: Maximum number of additional entries
- **Conservative**: 1 (2 total entries)
- **Aggressive**: 3-5 (4-6 total entries)

### Scale-In Triggers

The strategy automatically adds to positions when ANY of these conditions are met:

#### 1. Confirmation Increase
- Triggers when signal confirmations increase to 4 or 5 out of 5
- Indicates strengthening trend
- Example: Entry at 3/5, scale-in when reaches 4/5

#### 2. Trend Strengthening
- Triggers when ADX increases by 5+ points
- Shows momentum acceleration
- Example: Entry at ADX 30, scale-in at ADX 35+

#### 3. Favorable Price Movement
- Triggers when price moves 0.5 ATR in profitable direction
- Confirms position is working
- Example: Long at $100, scale-in at $100 + (0.5 × ATR)

### Position Sizing Example

**Account**: $10,000
**Initial Position**: 50% = $5,000
**Scale-In Size**: 25% = $2,500
**Max Scale-Ins**: 2

- **Entry 1**: $5,000 position at $100
- **Scale-In 1**: Add $2,500 at $102 (trend strengthens)
- **Scale-In 2**: Add $2,500 at $105 (confirmations increase)
- **Total Exposure**: $10,000 (100% of account)
- **Average Entry**: $101.67

### Advantages of Pyramiding
1. Start with smaller risk, increase if working
2. Average entry improves as trend develops
3. Maximize profits in strong trends
4. Reduce impact of false breakouts
5. Better risk-adjusted returns

### Risks of Pyramiding
1. Can overleverage account quickly
2. All entries correlated (same trade)
3. Reversal affects entire position
4. Requires strong trends to be effective
5. More complex position management

### Best Practices
- Never exceed 100% account exposure
- Use tighter stops when pyramiding
- Scale smaller than initial position
- Only pyramid in strong, clear trends
- Have clear exit plan for full position

---

## Stop Loss System

### Overview
The stop loss system protects your capital by automatically closing losing positions. Choose from three different stop loss calculation methods.

### Stop Loss Types

#### 1. ATR Based (Recommended)
- **How it works**: Stop loss based on Average True Range
- **Formula**: 
  - Long: `Entry Price - (ATR × Multiplier)`
  - Short: `Entry Price + (ATR × Multiplier)`
- **Default Multiplier**: 2.0
- **Advantages**: Adapts to volatility
- **Best for**: All market conditions

**Configuration**:
```pinescript
stopLossType = "ATR Based"
stopLossAtrMult = 2.0  // Adjust 1.5-3.0 based on risk tolerance
```

**Example**:
- Entry: $100
- ATR: $2
- Multiplier: 2.0
- Stop Loss: $100 - ($2 × 2.0) = $96

#### 2. Fixed Percentage
- **How it works**: Stop loss as fixed percentage from entry
- **Formula**: 
  - Long: `Entry Price × (1 - Percentage/100)`
  - Short: `Entry Price × (1 + Percentage/100)`
- **Default**: 2%
- **Advantages**: Simple, predictable risk
- **Best for**: When ATR is not reliable

**Configuration**:
```pinescript
stopLossType = "Fixed Percentage"
stopLossPct = 2.0  // 2% stop loss
```

**Example**:
- Entry: $100
- Percentage: 2%
- Stop Loss: $100 × (1 - 0.02) = $98

#### 3. Previous Swing
- **How it works**: Stop below recent swing low (long) or above swing high (short)
- **Lookback**: 20 bars
- **Advantages**: Respects market structure
- **Best for**: Trending markets with clear swings

**Configuration**:
```pinescript
stopLossType = "Previous Swing"
```

**Example**:
- Long entry: $105
- Recent swing low: $98
- Stop Loss: $98 (below swing low)

### Stop Loss Multiplier Guidelines

| Risk Tolerance | ATR Multiplier | Fixed % |
|---------------|----------------|---------|
| Very Conservative | 2.5 - 3.0 | 2.5% - 3.0% |
| Conservative | 2.0 - 2.5 | 2.0% - 2.5% |
| Moderate | 1.5 - 2.0 | 1.5% - 2.0% |
| Aggressive | 1.0 - 1.5 | 1.0% - 1.5% |

### Stop Loss Best Practices
1. Always use stop losses - never trade without protection
2. Set stops before entering trade
3. Don't move stops against you (further from entry)
4. Give stops enough room to breathe (respect volatility)
5. Accept losses when stops are hit - don't second guess

---

## Take Profit System

### Overview
The take profit system helps you lock in gains by automatically closing portions of your position at predetermined levels.

### Take Profit Methods

#### 1. ATR Based
- **How it works**: Target levels based on ATR multiples
- **Formula**: 
  - Long: `Entry + (ATR × Multiplier)`
  - Short: `Entry - (ATR × Multiplier)`
- **Advantages**: Adapts to volatility
- **Best for**: Volatile markets, crypto

**Configuration**:
```pinescript
tpMethod = "ATR Based"
tp1Mult = 1.5  // 1.5 × ATR
tp2Mult = 2.5  // 2.5 × ATR
tp3Mult = 4.0  // 4.0 × ATR
```

**Example**:
- Entry: $100
- ATR: $2
- TP1: $100 + ($2 × 1.5) = $103
- TP2: $100 + ($2 × 2.5) = $105
- TP3: $100 + ($2 × 4.0) = $108

#### 2. Risk-Reward Ratio
- **How it works**: Target based on stop loss distance
- **Formula**: `Entry + (Stop Distance × RR Ratio)`
- **Advantages**: Built-in risk management
- **Best for**: Professional trading approach

**Configuration**:
```pinescript
tpMethod = "Risk-Reward Ratio"
tp1Mult = 1.5  // 1.5:1 RR
tp2Mult = 2.5  // 2.5:1 RR
tp3Mult = 4.0  // 4.0:1 RR
```

**Example**:
- Entry: $100
- Stop Loss: $96
- Risk: $4
- TP1: $100 + ($4 × 1.5) = $106 (1.5:1)
- TP2: $100 + ($4 × 2.5) = $110 (2.5:1)
- TP3: $100 + ($4 × 4.0) = $116 (4.0:1)

#### 3. Fixed Percentage
- **How it works**: Fixed percentage gains from entry
- **Formula**: `Entry × (1 + Percentage/100)`
- **Advantages**: Simple, predictable
- **Best for**: Stable markets, stocks

**Configuration**:
```pinescript
tpMethod = "Fixed Percentage"
tp1Mult = 1.5  // 1.5% gain
tp2Mult = 2.5  // 2.5% gain
tp3Mult = 4.0  // 4.0% gain
```

### Take Profit Levels

#### TP1 (First Target)
- **Default**: 1.5× (ATR/RR/%)
- **Close Amount**: 50% of position
- **Purpose**: Lock in some profit, reduce risk
- **Typical timing**: Reached most often

#### TP2 (Second Target)
- **Default**: 2.5× (ATR/RR/%)
- **Close Amount**: 30% of remaining (15% total)
- **Purpose**: Capture trend extension
- **Typical timing**: Reached in good trends

#### TP3 (Final Target)
- **Default**: 4.0× (ATR/RR/%)
- **Close Amount**: Remaining 35% of position
- **Purpose**: Capture major moves
- **Typical timing**: Reached in strong trends only

### Partial Position Closing Example

**Initial Position**: 100 shares at $100

1. **TP1 Hit** ($103):
   - Close 50% = 50 shares
   - Remaining: 50 shares
   - Profit: $150

2. **TP2 Hit** ($105):
   - Close 30% of remaining = 15 shares
   - Remaining: 35 shares
   - Additional profit: $75

3. **TP3 Hit** ($108):
   - Close remaining 35 shares
   - Final profit: $280
   - **Total Profit**: $505

### Take Profit Best Practices
1. Always take partial profits - never hold for "perfect" exit
2. Let winners run after taking TP1
3. Adjust targets based on market conditions
4. Higher volatility = wider targets
5. Scale out more aggressively in choppy markets

---

## Trailing Stops

### Overview
Trailing stops automatically move your stop loss up (for longs) or down (for shorts) as the price moves in your favor, locking in profits while allowing room for continued gains.

### Activation Triggers

Trailing stops activate when EITHER condition is met:

#### 1. TP1 Hit
- Automatically activates after first take profit
- Ensures breakeven or better on remaining position
- Most common activation method

#### 2. Price Moves +2 ATR
- Activates when price moves 2× ATR in your favor
- Useful when TP1 not reached but good profit exists
- Protects unrealized gains

### Trailing Distance
- **Default**: 1.5 × ATR
- **How it works**: Stop trails price by fixed ATR distance
- **Updates**: Every bar as price moves favorably
- **Never moves backward**: Only moves in profitable direction

### Example: Long Trade

**Setup**:
- Entry: $100
- Initial Stop: $96 (2 ATR)
- TP1: $103 (1.5 ATR)
- Trailing Distance: $3 (1.5 ATR)

**Progression**:
1. Enter at $100, stop at $96
2. Price reaches $103, TP1 hit, trailing activated
3. Price at $106, trailing stop moves to $103 ($106 - $3)
4. Price at $110, trailing stop moves to $107 ($110 - $3)
5. Price drops to $107.50, position closed at trailing stop
6. **Result**: $7.50 profit instead of risking full $10 gain

### Breakeven Stop Movement

After TP1 is hit:
- Stop moves to entry price + commission
- Ensures no loss on remaining position
- Psychological safety net
- Allows stress-free trade management

### Configuration
```pinescript
enableTrailingStop = true
trailingStopAtrMult = 1.5  // Distance in ATR multiples
```

### Trailing Stop Guidelines

| Market Type | ATR Multiplier | Rationale |
|------------|----------------|-----------|
| High Volatility (Crypto) | 2.0 - 2.5 | Needs room to breathe |
| Moderate (Forex) | 1.5 - 2.0 | Balanced approach |
| Low Volatility (Stocks) | 1.0 - 1.5 | Tighter trailing |
| Trending | 2.0+ | Let trends run |
| Choppy | 1.0 - 1.5 | Protect gains quickly |

### Best Practices
1. Give trailing stops adequate room (1.5-2.0 ATR minimum)
2. Too tight = premature exits
3. Let big winners run with trailing stops
4. Accept that you'll never sell at the top
5. Trailing stops are for profit protection, not entry signals

---

## Alert System

### Overview
The enhanced alert system provides comprehensive JSON-formatted alerts for every action, suitable for webhook integration and automated trading.

### Alert Types

#### 1. Entry Alert
Triggered on initial position entry (long or short).

**Format**:
```json
{
  "action": "BUY",
  "signal_type": "ENTRY",
  "direction": "LONG",
  "symbol": "BTCUSD",
  "price": 45000.00,
  "regime": "trending",
  "confirmations": 4,
  "position_size": "50%",
  "stop_loss": 43600.00,
  "take_profit_1": 46400.00,
  "take_profit_2": 47800.00,
  "take_profit_3": 50200.00,
  "risk_reward_ratio": 2.33,
  "atr": 700.00,
  "timestamp": "2024-01-15 10:30:00"
}
```

**Use**: Execute initial entry with full risk management parameters

#### 2. Scale-In Alert
Triggered when adding to existing position.

**Format**:
```json
{
  "action": "ADD",
  "signal_type": "SCALE_IN",
  "direction": "LONG",
  "symbol": "BTCUSD",
  "price": 46000.00,
  "position_number": 2,
  "scale_in_size": "25%",
  "total_position": "75%",
  "updated_avg_price": 45333.33,
  "updated_stop_loss": 43900.00,
  "reason": "Confirmations increased to 5/5"
}
```

**Use**: Add to position with updated average entry and stop loss

#### 3. Take Profit Alert
Triggered when each TP level is reached.

**Format**:
```json
{
  "action": "CLOSE_PARTIAL",
  "signal_type": "TAKE_PROFIT",
  "direction": "LONG",
  "symbol": "BTCUSD",
  "price": 46400.00,
  "tp_level": "TP1",
  "close_amount": "50%",
  "profit": "+3.11%",
  "remaining_position": "50%",
  "instruction": "CLOSE 50% OF LONG POSITION",
  "move_stop_to_breakeven": true
}
```

**Use**: Close specified percentage and update risk management

#### 4. Stop Loss Alert
Triggered when stop loss is hit.

**Format**:
```json
{
  "action": "CLOSE",
  "signal_type": "STOP_LOSS",
  "direction": "LONG",
  "symbol": "BTCUSD",
  "price": 43600.00,
  "loss": "-3.11%",
  "stop_type": "FIXED_ATR",
  "instruction": "CLOSE LONG POSITION - STOP LOSS HIT"
}
```

**Use**: Close entire position, accept loss

#### 5. Exit Signal Alert
Triggered by strategy exit conditions (not stop loss).

**Format**:
```json
{
  "action": "CLOSE",
  "signal_type": "EXIT_SIGNAL",
  "direction": "LONG",
  "symbol": "BTCUSD",
  "price": 47000.00,
  "profit": "+4.44%",
  "reason": "EMA crossunder + MACD bearish",
  "instruction": "CLOSE LONG POSITION"
}
```

**Use**: Close position based on signal reversal

### Webhook Integration

All alerts are JSON formatted for easy webhook integration:

1. **TradingView Setup**:
   - Create alert for each condition
   - Set webhook URL to your server
   - Alerts sent automatically

2. **Server Processing**:
   - Parse JSON alert
   - Validate fields
   - Execute trade via broker API
   - Log transaction

3. **Example Flask Handler**:
```python
@app.route('/webhook', methods=['POST'])
def webhook():
    alert = request.json
    if alert['action'] == 'BUY':
        execute_buy(alert['symbol'], alert['price'])
    return 'OK', 200
```

---

## Dashboard Metrics

### Overview
The enhanced dashboard displays 13 key metrics including position and risk management information.

### Dashboard Sections

#### 1. Market Information
- **Market Regime**: Trending/Choppy/Strong Trend
- **ADX**: Current strength value
- **RSI**: Momentum indicator
- **MACD**: Bullish/Bearish status
- **EMA Trend**: Current direction
- **MTF Status**: Multi-timeframe alignment
- **Long Confirms**: Current confirmations (X/5)

#### 2. Position Information (NEW in v2.0)

**Position**
- Shows: LONG, SHORT, or None
- Color: Green (long), Red (short), Gray (none)
- Purpose: Immediate position awareness

**Entry & P&L**
- Shows: Entry price and current profit/loss %
- Format: "45000.00 (+3.5%)"
- Color: Green (profit), Red (loss)
- Updates: Real-time

**Stop Loss**
- Shows: Current stop loss level
- Format: "43600.00" or "43600.00 (Trail)"
- Indicates: If trailing stop is active
- Color: Red warning

**Next TP**
- Shows: Next take profit target
- Format: "46400.00" (TP1/TP2/TP3)
- Updates: After each TP is hit
- Color: Green target

**Scale Count**
- Shows: Position count vs maximum
- Format: "2/3" (2 positions out of 3 max)
- Purpose: Track pyramiding status

### Reading the Dashboard

**Example - Active Long Position**:
```
Market Regime: Trending
ADX: 32.5
RSI: 58
MACD: Bullish
EMA Trend: Bullish
MTF Status: Mostly Up
Long Confirms: 4/5
---
Position: LONG
Entry & P&L: 45000 (+3.5%)
Stop Loss: 43600 (Trail)
Next TP: 46400
Scale Count: 2/3
```

**Interpretation**:
- In a trending market (good for long)
- Position up 3.5% from $45,000 entry
- Trailing stop active at $43,600
- Next target at $46,400
- 2 positions entered (can add 1 more)
- Strong confirmation (4/5)

---

## Best Practices

### 1. Position Sizing
- Never risk more than 1-2% per trade
- Calculate position size: `Account × Risk% / Stop Distance`
- Account for total exposure when pyramiding
- Reduce size in choppy markets
- Increase size in strong trends (with caution)

### 2. Stop Loss Management
- Always set stops before entry
- Use ATR-based stops in volatile markets
- Give stops adequate room (2-2.5 ATR minimum)
- Never move stops against your position
- Accept losses when stops are hit

### 3. Take Profit Strategy
- Always take partial profits at TP1 (50%)
- Let remaining position run with trailing stop
- Adjust TP levels based on market volatility
- Be more aggressive in choppy markets
- Let winners run in trending markets

### 4. Pyramiding Guidelines
- Only pyramid in strong, clear trends
- Scale in smaller than initial position
- Update stops after each scale-in
- Maximum 2-3 scale-ins recommended
- Never exceed 100% account exposure

### 5. Risk-Reward Requirements
- Minimum 1.5:1 reward-to-risk ratio
- Target 2:1 or better for best results
- Higher RR = lower required win rate
- Calculate RR before every trade
- Skip trades with poor RR

### 6. Market Regime Adaptation
- **Trending Markets**:
  - Wider stops (2.5-3.0 ATR)
  - Wider TP targets
  - Enable pyramiding
  - Let winners run longer

- **Choppy Markets**:
  - Tighter stops (1.5-2.0 ATR)
  - Closer TP targets
  - Disable pyramiding
  - Take profits quickly

### 7. Trade Direction Selection
- **Bull Market**: Long Only
- **Bear Market**: Short Only or Both
- **Ranging**: Both directions
- **High uncertainty**: Long Only (lower risk)

---

## Configuration Examples

### Example 1: Conservative Swing Trader
```pinescript
// Trade Direction
tradeDirection = "Both"

// Position Sizing
enablePyramiding = false
initialPositionPct = 33
scaleInPct = 17
maxScaleIns = 1

// Stop Loss
stopLossType = "ATR Based"
stopLossAtrMult = 2.5
enableTrailingStop = true
trailingStopAtrMult = 2.0

// Take Profit
enableTakeProfit = true
tpMethod = "Risk-Reward Ratio"
tp1Mult = 2.0    // 2:1 RR
tp2Mult = 3.0    // 3:1 RR
tp3Mult = 5.0    // 5:1 RR
tp1ClosePct = 50
tp2ClosePct = 30
tp3ClosePct = 100
```

**Profile**: Low risk, high quality trades
**Win rate target**: 50-60%
**Avg RR**: 2.5:1
**Max exposure**: 50% (with pyramiding)

### Example 2: Moderate Day Trader
```pinescript
// Trade Direction
tradeDirection = "Both"

// Position Sizing
enablePyramiding = true
initialPositionPct = 50
scaleInPct = 25
maxScaleIns = 2

// Stop Loss
stopLossType = "ATR Based"
stopLossAtrMult = 2.0
enableTrailingStop = true
trailingStopAtrMult = 1.5

// Take Profit
enableTakeProfit = true
tpMethod = "ATR Based"
tp1Mult = 1.5    // 1.5 ATR
tp2Mult = 2.5    // 2.5 ATR
tp3Mult = 4.0    // 4.0 ATR
tp1ClosePct = 50
tp2ClosePct = 30
tp3ClosePct = 100
```

**Profile**: Balanced approach
**Win rate target**: 45-55%
**Avg RR**: 2:1
**Max exposure**: 100% (with pyramiding)

### Example 3: Aggressive Scalper
```pinescript
// Trade Direction
tradeDirection = "Both"

// Position Sizing
enablePyramiding = true
initialPositionPct = 60
scaleInPct = 30
maxScaleIns = 3

// Stop Loss
stopLossType = "ATR Based"
stopLossAtrMult = 1.5
enableTrailingStop = true
trailingStopAtrMult = 1.0

// Take Profit
enableTakeProfit = true
tpMethod = "ATR Based"
tp1Mult = 1.0    // 1 ATR
tp2Mult = 1.5    // 1.5 ATR
tp3Mult = 2.5    // 2.5 ATR
tp1ClosePct = 50
tp2ClosePct = 30
tp3ClosePct = 100
```

**Profile**: High frequency, active management
**Win rate target**: 40-50%
**Avg RR**: 1.5:1
**Max exposure**: 150% (with pyramiding)

### Example 4: Stock Market (Long Only)
```pinescript
// Trade Direction
tradeDirection = "Long Only"

// Position Sizing
enablePyramiding = true
initialPositionPct = 50
scaleInPct = 25
maxScaleIns = 2

// Stop Loss
stopLossType = "ATR Based"
stopLossAtrMult = 2.0
enableTrailingStop = true
trailingStopAtrMult = 1.5

// Take Profit
enableTakeProfit = true
tpMethod = "Risk-Reward Ratio"
tp1Mult = 2.0    // 2:1 RR
tp2Mult = 3.0    // 3:1 RR
tp3Mult = 5.0    // 5:1 RR
tp1ClosePct = 50
tp2ClosePct = 30
tp3ClosePct = 100
```

**Profile**: Stock swing trader
**Win rate target**: 50-60%
**Avg RR**: 2.5:1
**Max exposure**: 100%

---

## Risk Calculator

### Calculate Position Size
```
Position Size = (Account Balance × Risk %) / Stop Loss Distance

Example:
- Account: $10,000
- Risk per trade: 2% = $200
- Entry: $100
- Stop: $96
- Stop distance: $4

Position Size = $200 / $4 = 50 shares
Position Value = 50 × $100 = $5,000 (50% of account)
```

### Calculate Risk-Reward Ratio
```
RR Ratio = Profit Target Distance / Stop Loss Distance

Example:
- Entry: $100
- Stop: $96 (Risk: $4)
- TP1: $106 (Reward: $6)

RR Ratio = $6 / $4 = 1.5:1
```

### Calculate Required Win Rate
```
Required Win Rate = 100% / (1 + RR Ratio)

Examples:
- 1:1 RR → 50% win rate needed
- 1.5:1 RR → 40% win rate needed
- 2:1 RR → 33% win rate needed
- 3:1 RR → 25% win rate needed
```

---

## Troubleshooting

### Issue: Stops Too Tight
**Symptoms**: Stopped out frequently, then price moves in your direction
**Solution**: 
- Increase ATR multiplier (2.0 → 2.5)
- Use "Previous Swing" stop type
- Give more room in volatile markets

### Issue: Not Reaching TP Levels
**Symptoms**: Price doesn't reach take profit targets
**Solution**:
- Reduce TP multipliers (4.0 → 3.0)
- Use "ATR Based" method instead of RR
- Check if targets are realistic for timeframe

### Issue: Too Much Exposure from Pyramiding
**Symptoms**: Account overleveraged, high stress
**Solution**:
- Reduce maxScaleIns (3 → 1)
- Reduce scaleInPct (30% → 20%)
- Disable pyramiding in choppy markets

### Issue: Trailing Stop Hit Too Early
**Symptoms**: Exited before major move continues
**Solution**:
- Increase trailing distance (1.5 → 2.0 ATR)
- Only use trailing in strong trends
- Accept some give-back for bigger gains

### Issue: Alerts Not Generating
**Symptoms**: Expected alert didn't fire
**Solution**:
- Check alert is created in TradingView
- Verify webhook URL is correct
- Check alert condition matches your filters
- Ensure strategy is active on chart

---

## Summary Checklist

Before going live, ensure:
- [ ] Trade direction configured for your strategy
- [ ] Position sizes appropriate for account (1-2% risk)
- [ ] Stop loss type selected and tested
- [ ] Stop loss gives adequate room (2+ ATR)
- [ ] Take profit levels realistic for timeframe
- [ ] Pyramiding disabled or conservatively configured
- [ ] Trailing stops enabled with proper distance
- [ ] All alerts created and tested
- [ ] Dashboard metrics understood
- [ ] Risk calculator used for position sizing
- [ ] Backtested configuration on historical data
- [ ] Paper traded for at least 2 weeks
- [ ] Trade journal ready for tracking

---

## Conclusion

The risk management features in v2.0 provide professional-grade tools for capital protection and profit optimization. Start conservatively, test thoroughly, and adjust based on your results. Always prioritize capital preservation over profit maximization.

Remember: **The goal is not to make money on every trade, but to manage risk so well that winners far exceed losers over time.**

Good luck and trade safe! 📈
