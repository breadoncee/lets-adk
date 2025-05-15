
def calculate_tip(bill_amount: float, tip_percentage: float = 15.0) -> dict:
  """Calculate tip amount based on the bill and percentage."""
  tip_amount = bill_amount * (tip_percentage / 100)
  total = bill_amount + tip_amount
  return {
    "bill_amount": bill_amount,
    "tip_percentage": tip_percentage,
    "tip_amount": round(tip_amount, 2),
    "total": round(total, 2)
  }