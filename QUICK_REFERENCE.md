# Quick Reference Card - Adaptive Momentum Strategy v2.0

## 🚀 Quick Start (5 Minutes)

### Step 1: Add Strategy to TradingView
1. Open Pine Editor in TradingView
2. Copy `adaptive_momentum_strategy.pine`
3. Click "Add to Chart"

### Step 2: Choose Your Profile
Pick from `strategy_configs.json`:
- **Conservative**: Low risk, high quality (33% position, 2.5 ATR stops)
- **Moderate**: Balanced (50% position, 2.0 ATR stops) ⭐ Recommended
- **Aggressive**: High frequency (60% position, 1.5 ATR stops)
- **Crypto**: For volatile crypto markets (40% position, 3.0 ATR stops)
- **Forex**: For stable forex pairs (50% position, RR-based)
- **Stocks**: Long-only for stocks (50% position, RR-based)

### Step 3: Set Risk Parameters
Configure in Settings:
```
Trade Direction: Both
Initial Position: 50%
Stop Loss Type: ATR Based
Stop Loss Multiplier: 2.0
Enable Take Profit: Yes
Enable Trailing Stop: Yes
```

---

## 📊 Dashboard Quick View

| Indicator | Meaning | Good Value |
|-----------|---------|------------|
| Market Regime | Trending/Choppy | Trending = Better |
| ADX | Trend Strength | >25 = Trending |
| Long Confirms | Signal Quality | 3+/5 = Good |
| Position | Current Direction | LONG/SHORT/None |
| Entry & P&L | Profit/Loss | Green = Profit |
| Stop Loss | Protection Level | Shows if trailing |
| Next TP | Next Target | Upcoming goal |
| Scale Count | Pyramid Status | X/3 positions |

---

## 💡 Risk Management Cheat Sheet

### Position Sizing Formula
```
Position Size = (Account × Risk %) / Stop Distance
Example: ($10,000 × 2%) / $4 = 50 shares
```

### Risk-Reward Ratios
| RR Ratio | Win Rate Needed | Recommended |
|----------|-----------------|-------------|
| 1:1 | 50% | ❌ Too low |
| 1.5:1 | 40% | ✅ Good |
| 2:1 | 33% | ✅✅ Better |
| 3:1 | 25% | ✅✅✅ Best |

### Stop Loss Guidelines
| Market Type | ATR Multiplier | Fixed % |
|-------------|----------------|---------|
| Crypto (High Vol) | 2.5-3.0 | 3.0% |
| Forex (Medium) | 2.0-2.5 | 2.0% |
| Stocks (Lower) | 1.5-2.0 | 1.5% |

### Take Profit Levels
Default setup (Moderate profile):
- **TP1**: 1.5× ATR → Close 50%
- **TP2**: 2.5× ATR → Close 15% more
- **TP3**: 4.0× ATR → Close remaining 35%

---

## 🎯 Signal Quality Checklist

### Before Taking a Trade
- [ ] Confirmations: 3+ out of 5
- [ ] Market Regime: Trending (ADX >25)
- [ ] MTF Alignment: At least 2/3 timeframes
- [ ] Risk-Reward: Minimum 1.5:1
- [ ] Position Size: 1-2% account risk
- [ ] No major news events pending

### Ideal Entry Conditions
| Condition | Trending | Choppy |
|-----------|----------|--------|
| Confirmations | 3-4/5 | 4-5/5 |
| ADX | >30 | N/A |
| MTF | 2-3 aligned | Any |
| Risk Level | Moderate | Higher |

---

## 🔔 Alert Types Reference

### 1. Entry Alert
Sent when: New position opened
Contains: Symbol, price, size, stops, targets, RR ratio
Action: Open position with displayed parameters

### 2. Scale-In Alert
Sent when: Adding to winning position
Contains: Position #, size, new average, reason
Action: Add specified amount to existing position

### 3. Take Profit Alert
Sent when: TP1, TP2, or TP3 hit
Contains: TP level, close amount, profit %, remaining
Action: Close specified percentage

### 4. Stop Loss Alert
Sent when: Stop hit (fixed or trailing)
Contains: Loss/profit %, stop type
Action: Close entire position

### 5. Exit Signal Alert
Sent when: Strategy exit signal
Contains: Reason, profit/loss %
Action: Close entire position

---

## ⚙️ Common Settings Adjustments

### Too Many Signals?
```
Increase: Min Confirmations (2 → 3)
Enable: Require Trend Alignment
Increase: ADX Threshold (25 → 30)
```

### Too Few Signals?
```
Decrease: Min Confirmations (2 → 1)
Disable: Require Trend Alignment
Decrease: ADX Threshold (25 → 20)
```

### Getting Stopped Out Too Often?
```
Increase: Stop Loss Multiplier (2.0 → 2.5)
Change: Stop Loss Type to "Previous Swing"
```

### Not Reaching Take Profits?
```
Decrease: TP Multipliers (1.5 → 1.0)
Change: TP Method to "ATR Based"
```

---

## 📈 Pyramiding Quick Guide

### When to Use
- ✅ Strong, clear trends
- ✅ ADX increasing
- ✅ High confirmations (4-5/5)
- ❌ Choppy markets
- ❌ Weak trends

### Scale-In Triggers
1. **Confirmations increase** to 4-5/5
2. **ADX increases** by 5+ points
3. **Price moves** +0.5 ATR favorably

### Example
```
Entry 1: 50% at $100 (Initial)
Entry 2: 25% at $102 (Trend strengthens)
Entry 3: 25% at $105 (Confirmations up)
Average: $101.67
Total: 100% position
```

---

## 🛡️ Trailing Stop Behavior

### Activation
Trailing stop activates when:
- TP1 is hit, OR
- Price moves +2 ATR in your favor

### Movement
- **Distance**: 1.5 ATR from price (configurable)
- **Direction**: Only moves in profit direction
- **Never**: Moves against you

### Breakeven
After TP1 hits:
- Stop moves to entry price
- Ensures no loss on remaining position

---

## 💰 Expected Performance

### Conservative Profile
- Win Rate: 50-60%
- Avg RR: 2.5:1
- Max Drawdown: <15%
- Trade Frequency: Low

### Moderate Profile
- Win Rate: 45-55%
- Avg RR: 2.0:1
- Max Drawdown: <20%
- Trade Frequency: Medium

### Aggressive Profile
- Win Rate: 40-50%
- Avg RR: 1.5:1
- Max Drawdown: <25%
- Trade Frequency: High

---

## 🔍 Troubleshooting

| Problem | Quick Fix |
|---------|-----------|
| No signals appearing | Check ADX, lower confirmations |
| Too many signals | Increase confirmations to 3 |
| Stops too tight | Increase ATR multiplier |
| Not reaching TPs | Lower TP multipliers |
| Strategy not loading | Refresh page, check Pine version |
| Alerts not firing | Create alert in TradingView UI |
| Dashboard not showing | Check strategy is active on chart |
| Position size wrong | Verify % in settings |

---

## 📱 Risk Management Daily Checklist

### Before Market Open
- [ ] Check economic calendar
- [ ] Review open positions
- [ ] Verify risk per trade (1-2%)
- [ ] Confirm total exposure (<100%)
- [ ] Check stop losses in place

### During Trading
- [ ] Follow signals (don't override)
- [ ] Let stops work (don't move)
- [ ] Take profits at levels (don't hold)
- [ ] Monitor dashboard P&L
- [ ] Track position count

### After Market Close
- [ ] Journal all trades
- [ ] Calculate win rate
- [ ] Review what worked
- [ ] Update settings if needed
- [ ] Plan tomorrow

---

## 🎓 Best Practices

### Position Sizing
- ✅ Never risk >2% per trade
- ✅ Calculate before entry
- ✅ Account for pyramiding
- ❌ Don't overtrade

### Stop Losses
- ✅ Set before entry
- ✅ Use ATR-based in volatile markets
- ✅ Give 2+ ATR room
- ❌ Never remove stops
- ❌ Never move against position

### Take Profits
- ✅ Always take 50% at TP1
- ✅ Let rest run with trailing
- ✅ Adjust for conditions
- ❌ Don't hold for "perfect" exit

### Pyramiding
- ✅ Only in strong trends
- ✅ Scale smaller than initial
- ✅ Update stops each time
- ❌ Don't exceed 100% exposure

---

## 📞 Quick Support

- **Full Guide**: RISK_MANAGEMENT_GUIDE.md
- **Setup Help**: QUICK_START.md
- **Strategy Details**: STRATEGY_GUIDE.md
- **Testing**: VALIDATION_CHECKLIST.md
- **Configs**: strategy_configs.json

---

## 🎯 Remember

1. **Risk First**: Protect capital before seeking profit
2. **Follow Signals**: Trust the strategy
3. **Be Patient**: Quality over quantity
4. **Stay Disciplined**: Follow risk management rules
5. **Keep Learning**: Track and improve

**Trade Safe! 📈**
