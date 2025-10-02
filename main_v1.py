def calculate_cost(W, R):
    if W < 1 or W > 1000:
        raise ValueError("Invalid")

    if R.lower() == "nội thành":
        if W < 100:
            return int(W * 5000)
        else:
            return int(W * 10000)
    elif R.lower() == "ngoại thành":
        if W < 100:
            return int(W * 8000)
        else:
            return int(W * 20000)
    else:
        raise ValueError("Invalid")
