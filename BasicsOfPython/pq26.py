# WAF to convert USD(dollar) to INR(rupee)...

# 1 usd = 83 inr
# 2 usd = 166 inr

def converter(usd_val):

    inr_val = usd_val * 83

    print(usd_val, "USD =", inr_val, "INR")

converter(73)