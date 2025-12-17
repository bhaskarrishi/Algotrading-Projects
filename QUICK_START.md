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

### Step 2: Configure Settings (1 minute)

1. **Click the strategy name** on the chart (it will say "Adaptive Multi-Timeframe...")
2. **Click the gear icon** (Settings)
3. **Choose a preset** from `strategy_configs.json`:
   - **Conservative**: For swing trading (fewer but higher quality signals)
   - **Moderate**: For balanced day/swing trading (recommended for beginners)
   - **Aggressive**: For scalping (more signals, higher risk)

**For your first time, use MODERATE settings:**
```
Minimum Confirmations: 2
Use Multi-Timeframe: ✓ (enabled)
Require Trend Alignment: □ (disabled)
ADX Trend Threshold: 25
```

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
- **Market Regime**: Shows current market state
- **ADX**: Trend strength (higher = stronger trend)
- **RSI**: Momentum indicator
- **MACD**: Bullish or Bearish
- **EMA Trend**: Current trend direction
- **MTF Status**: Multi-timeframe alignment
- **Long Confirms**: How many conditions are met

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

## Risk Management Checklist

Before each trade, confirm:
- [ ] Position size calculated (1-2% of account risk)
- [ ] Stop loss level set (based on ATR or support/resistance)
- [ ] Take profit target identified (2:1 or 3:1 reward:risk)
- [ ] Market regime checked (dashboard)
- [ ] Confirmations count is sufficient (2+ for trending, 3+ for choppy)
- [ ] Multi-timeframe alignment (if enabled)
- [ ] No major news events expected
- [ ] Account has no other correlated positions

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

- **Full Documentation**: See `STRATEGY_GUIDE.md`
- **Configuration Presets**: See `strategy_configs.json`
- **Flask Webhook**: Already in `First_program.py`

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
