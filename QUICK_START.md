# Quick Start Guide - Adaptive Multi-Timeframe Strategy

## 5-Minute Setup

### Step 1: Setup TradingView Strategy (2 minutes)

1. **Open TradingView**
   - Go to [TradingView.com](https://www.tradingview.com)
   - Open any chart (e.g., BTC/USD, EUR/USD)

2. **Add the Strategy**
   - Click "Pine Editor" at the bottom of the screen
   - Click "New" → "New Blank Script"
   - Copy ALL content from `adaptive_momentum_strategy.pine`
   - Paste into the editor
   - Click "Save" and give it a name
   - Click "Add to Chart"

3. **You're Done!**
   - The strategy should now appear on your chart with:
     - Moving averages (green/red lines)
     - Entry signals (triangles)
     - Dashboard (top right corner)
     - Colored backgrounds showing market regime

### Step 2: Configure Settings (2 minutes)

1. **Click the strategy name** on the chart (it will say "Adaptive Multi-Timeframe...")
2. **Click the gear icon** (Settings)
3. **Choose a preset** from `strategy_configs.json`:
   - **Conservative**: For swing trading (fewer but higher quality signals)
   - **Moderate**: For balanced day/swing trading (recommended for beginners)
   - **Aggressive**: For scalping (more signals, higher risk)
   - **Crypto Volatile**: Optimized for cryptocurrency markets
   - **Forex Stable**: Optimized for forex pairs
   - **Stocks Daily**: Long-only for stock markets

**For your first time, use MODERATE settings:**

**Signal Settings:**
```
Minimum Confirmations: 2
Use Multi-Timeframe: ✓ (enabled)
Require Trend Alignment: □ (disabled)
ADX Trend Threshold: 25
```

**Risk Management (NEW in v2.0):**
```
Trade Direction: "Both"
Enable Pyramiding: ✓ (enabled)
Initial Position Size: 50%
Scale-In Size: 25%
Max Scale-Ins: 2
Stop Loss Type: "ATR Based"
Stop Loss ATR Multiplier: 2.0
Enable Trailing Stop: ✓ (enabled)
Trailing Stop ATR Multiplier: 1.5
Enable Take Profit: ✓ (enabled)
TP Method: "ATR Based"
TP1 Multiplier: 1.5
TP1 Close Amount: 50%
TP2 Multiplier: 2.5
TP2 Close Amount: 30%
TP3 Multiplier: 4.0
TP3 Close Amount: 100%
```

**Note**: All risk management features are enabled by default for v2.0. You can disable pyramiding or take profits if you prefer simpler trading.

### Step 3: Setup Webhook Alerts (2 minutes)

1. **Start the Flask Server**
   ```bash
   cd /home/runner/work/Algotrading-Projects/Algotrading-Projects
   python First_program.py
   ```
   - Server will run on `http://localhost:5000`
   - Open browser to see dashboard

2. **Create Alert in TradingView**
   - Right-click anywhere on the chart
   - Select "Add Alert"
   - Condition: Select "Adaptive Multi-Timeframe..." → "Long Entry Alert"
   - Alert name: "Strategy Buy Signal"
   - Webhook URL: `http://your-server-ip:5000/webhook`
   - Click "Create"

3. **Repeat for Other Signals**
   - Create alerts for:
     - Short Entry Alert (Sell signals)
     - Exit Long Alert
     - Exit Short Alert

## What You Should See

### On the Chart:
- **Green/Red Lines**: Fast and Slow EMAs showing trend
- **Blue Line**: 50 EMA trend filter
- **Background Colors**:
  - Light Green = Trending market
  - Light Blue = Strong trend
  - Light Orange = Choppy market
- **Triangles**:
  - Green ▲ = Buy signal
  - Red ▼ = Sell signal

### On the Dashboard (Top Right):

**Market Indicators:**
- **Market Regime**: Shows current market state
- **ADX**: Trend strength (higher = stronger trend)
- **RSI**: Momentum indicator
- **MACD**: Bullish or Bearish
- **EMA Trend**: Current trend direction
- **MTF Status**: Multi-timeframe alignment
- **Long Confirms**: How many conditions are met

**Position & Risk Info (NEW in v2.0):**
- **Position**: Current direction (LONG/SHORT/None)
- **Entry & P&L**: Entry price and profit/loss percentage
- **Stop Loss**: Active stop level (shows "(Trail)" if trailing)
- **Next TP**: Next take profit target to be hit
- **Scale Count**: Number of positions entered vs maximum allowed

**Example Active Position:**
```
Position: LONG
Entry & P&L: 45000 (+3.5%)
Stop Loss: 43600 (Trail)
Next TP: 46400
Scale Count: 2/3
```
This means: You're long from $45,000, up 3.5%, trailing stop at $43,600, next target $46,400, and you've entered 2 of 3 allowed positions.

## Understanding Your First Signals

### In a Trending Market (Green Background):
**Long Signal Appears When:**
- Fast EMA crosses above Slow EMA
- Price is above 50 EMA
- MACD is bullish
- ADX shows trend (>25)
- At least 2 confirmations met

**What to Do:**
- Check the dashboard confirmations (should be 2+)
- Verify multi-timeframe status
- Enter trade with proper stop loss

### In a Choppy Market (Orange Background):
**Long Signal Appears When:**
- RSI crosses above 30 (oversold)
- RSI is below 40
- Price is above fast EMA
- At least 3 confirmations met

**What to Do:**
- Be more cautious (choppy = higher risk)
- Use tighter stops
- Consider smaller position size

## Testing Before Live Trading

### Backtest the Strategy:
1. Click "Strategy" tab at the bottom (shows performance)
2. Look at key metrics:
   - **Net Profit**: Should be positive
   - **Win Rate**: Aim for >45%
   - **Profit Factor**: Should be >1.2
   - **Max Drawdown**: Check if acceptable for your risk
3. Adjust settings if needed

### Paper Trade First:
1. Use TradingView's paper trading feature
2. Follow signals for at least 1-2 weeks
3. Track your results
4. Only go live after consistent results

## Common Questions

### Q: Too many signals?
**A:** Increase "Minimum Confirmations" to 3, enable "Require Trend Alignment"

### Q: Too few signals?
**A:** Decrease "Minimum Confirmations" to 1, disable "Require Trend Alignment"

### Q: Signals not appearing?
**A:** Check that:
- Strategy is loaded on chart
- You're on correct timeframe (15m, 1H, or 4H recommended)
- Symbol has enough volatility
- Market is open (for stocks)

### Q: How do I know if it's working?
**A:** Check the dashboard:
- Market regime should update in real-time
- Confirmations count should change with price
- Alert should trigger when triangle appears

### Q: What's a good win rate?
**A:** 
- Trending markets: 50-60% win rate is good
- Choppy markets: 40-50% win rate is acceptable
- Overall: Aim for profit factor >1.5

### Q: How do stop losses and take profits work?
**A:** The strategy automatically:
- Sets stop loss when you enter (e.g., 2 ATR below entry for long)
- Closes 50% at TP1 (first target)
- Closes 15% at TP2 (second target)
- Closes remaining 35% at TP3 (final target)
- Activates trailing stop after TP1 to protect profits

### Q: What is pyramiding/scale-in?
**A:** Pyramiding adds to winning positions:
- Start with 50% position
- Add 25% when trend strengthens (up to 2 more times)
- Results in better average entry price
- Only happens in strong, confirmed trends

### Q: Should I enable pyramiding as a beginner?
**A:** 
- **Beginners**: Keep it disabled or max 1 scale-in
- **Intermediate**: Enable with 2 scale-ins (default)
- **Advanced**: Can use 3-5 scale-ins in very strong trends

## Understanding Risk Management (v2.0)

### Position Sizing Example
**Account**: $10,000
**Risk per trade**: 2% = $200

**Trade Setup**:
- Entry: $100
- Stop Loss: $96 (2 ATR = $4 away)
- Position Size: $200 ÷ $4 = 50 shares
- Position Value: 50 × $100 = $5,000 (50% of account)

**With Pyramiding**:
- Initial Entry: 50 shares at $100 = $5,000
- Scale-In 1: 25 shares at $102 = $2,500
- Scale-In 2: 25 shares at $105 = $2,500
- Total: 100 shares, Average: $101.67, Exposure: $10,167

### Take Profit Example
**Initial**: 100 shares at $100
**ATR**: $2

1. **TP1 at $103** (1.5 ATR):
   - Close 50 shares
   - Profit: 50 × $3 = $150
   - Remaining: 50 shares

2. **TP2 at $105** (2.5 ATR):
   - Close 15 shares (30% of remaining)
   - Profit: 15 × $5 = $75
   - Remaining: 35 shares

3. **TP3 at $108** (4.0 ATR):
   - Close 35 shares (all remaining)
   - Profit: 35 × $8 = $280
   - **Total Profit**: $505 on $10,000 = 5.05%

### Stop Loss Protection
The strategy protects you automatically:
- **Initial Stop**: Prevents large losses (e.g., -2%)
- **Trailing Stop**: Locks in profits after TP1
- **Breakeven Stop**: Moves to entry after TP1 hits
- **Never moves backward**: Only in profitable direction

### Quick Risk Settings Guide

**Conservative (Lower Risk)**:
```
Initial Position: 33%
Max Scale-Ins: 1
Stop Loss ATR: 2.5
TP1 Multiplier: 2.0
Enable Trailing: Yes
```

**Moderate (Balanced)**:
```
Initial Position: 50%
Max Scale-Ins: 2
Stop Loss ATR: 2.0
TP1 Multiplier: 1.5
Enable Trailing: Yes
```

**Aggressive (Higher Risk)**:
```
Initial Position: 60%
Max Scale-Ins: 3
Stop Loss ATR: 1.5
TP1 Multiplier: 1.0
Enable Trailing: Yes
```

## Next Steps

### Week 1: Learn the System
- Watch how the strategy behaves in different market conditions
- Observe trending vs choppy market signals
- Note which signals are most profitable

### Week 2: Optimize Settings
- Adjust parameters based on your observations
- Try different confirmation levels
- Test on different timeframes

### Week 3: Paper Trade
- Follow every signal
- Keep a trading journal
- Calculate your actual win rate

### Week 4+: Go Live (If Ready)
- Start with small position sizes
- Follow your risk management rules
- Review and adjust regularly

## Risk Management Checklist (v2.0)

### Before First Trade
- [ ] Risk management settings configured
- [ ] Position size appropriate for account (1-2% risk)
- [ ] Stop loss type selected (ATR Based recommended)
- [ ] Take profit levels enabled
- [ ] Trailing stops enabled
- [ ] Pyramiding configured (or disabled if beginner)
- [ ] Trade direction set (Both/Long Only/Short Only)
- [ ] Dashboard understood (can read P&L, stops, targets)

### Before Each Trade
- [ ] Position size calculated (1-2% of account risk)
- [ ] Stop loss level verified (strategy sets automatically)
- [ ] Take profit targets confirmed (TP1, TP2, TP3)
- [ ] Risk-reward ratio acceptable (minimum 1.5:1)
- [ ] Market regime checked (trending vs choppy)
- [ ] Confirmations count sufficient (2+ for trending, 3+ for choppy)
- [ ] Multi-timeframe alignment (if enabled)
- [ ] No major news events expected
- [ ] Total account exposure acceptable (including existing positions)
- [ ] Dashboard shows "ready" state (no conflicting positions)

### During Trade (Strategy Manages Automatically)
- [ ] Monitor dashboard for P&L updates
- [ ] Watch for TP1 hit (50% closes automatically)
- [ ] Check trailing stop activation (after TP1)
- [ ] Look for scale-in opportunities (if enabled)
- [ ] Verify stop moved to breakeven after TP1

### After Trade
- [ ] Record trade in journal
- [ ] Note win/loss and percentage
- [ ] Check which TP levels were hit
- [ ] Review if pyramiding was used
- [ ] Calculate actual RR ratio achieved
- [ ] Note market regime during trade

## Troubleshooting

### Strategy Not Loading
- Check you copied the complete Pine script
- Verify TradingView subscription allows indicators
- Try refreshing the page

### Webhook Not Receiving Alerts
- Verify Flask server is running (`python First_program.py`)
- Check webhook URL is correct
- Ensure firewall allows connections on port 5000
- Test with: `curl -X POST http://localhost:5000/webhook -H "Content-Type: application/json" -d '{"message":"test"}'`

### Unexpected Signals
- Review strategy settings
- Check timeframe (some signals only on specific timeframes)
- Verify market conditions (trending vs choppy)
- Look at confirmations count

## Support Resources

- **Quick Start**: This file - 5-minute setup
- **Risk Management Guide**: `RISK_MANAGEMENT_GUIDE.md` - Comprehensive risk management
- **Strategy Guide**: `STRATEGY_GUIDE.md` - Complete technical documentation
- **Configuration Presets**: `strategy_configs.json` - 6 pre-configured profiles
- **Validation Checklist**: `VALIDATION_CHECKLIST.md` - Testing procedures
- **Flask Webhook**: `First_program.py` - Alert receiver

## Pro Tips

1. **Best Timeframes**:
   - Scalping: 5m chart with 15m/1H/4H higher timeframes
   - Day Trading: 15m chart with 1H/4H/1D higher timeframes
   - Swing Trading: 1H or 4H chart with 4H/1D/1W higher timeframes

2. **Best Markets**:
   - Trending strongly: Use trending logic (will auto-detect)
   - Ranging: Strategy adapts automatically to choppy mode
   - High volatility: Increase ADX threshold to 30

3. **Combining with Other Tools**:
   - Use support/resistance levels for entries
   - Check volume for confirmation
   - Consider broader market context
   - Watch for divergences

4. **Performance Tracking**:
   - Keep a trading journal
   - Track win rate by market regime
   - Note which timeframes work best
   - Record optimal confirmation counts

## Remember

- **Start Small**: Use small position sizes initially
- **Be Patient**: Wait for high-quality signals (3+ confirmations)
- **Stay Disciplined**: Follow your risk management rules
- **Keep Learning**: Market conditions change, adapt accordingly
- **Never Risk More Than You Can Afford to Lose**

## Success Metrics

After 20 trades, you should have:
- Win rate >45%
- Average win > average loss
- Profit factor >1.2
- Consistent with risk management rules

If not, adjust settings or timeframes before continuing.

---

**Ready to start? Open TradingView and add the strategy to your chart!**

Good luck and trade safe! 📈
