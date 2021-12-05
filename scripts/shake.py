from client import db
import math
from scipy.stats import norm

won = len(list(db.find({"poktan": {"$gt": 0}, "won": {"$gt": 0}})))
lost = len(list(db.find({"poktan": {"$gt": 0}, "won": {"$lt": 0}})))
size = won + lost

prop = won/(won + lost)

statistic = (prop - 1/3)/math.sqrt((1/3) * (2/3) / size)
pvalue = 1 - norm.cdf(statistic)

print("Alternative Hypothesis: p > 1/3")
print(f"Won: {won} times, Lost: {lost} times, statistic: {statistic}")
print(f"p-value: {pvalue}, {'Rejected' if pvalue < 0.05 else 'Failed to Reject'}")