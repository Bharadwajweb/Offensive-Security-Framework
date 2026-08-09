def calculate_risk_score(open_ports):

    score = 0

    for port, service, banner, risk, finding in open_ports:

        if risk == "LOW":
            score += 2

        elif risk == "MEDIUM":
            score += 5

        elif risk == "HIGH":
            score += 8

        elif risk == "CRITICAL":
            score += 10

    if score <= 5:
        level = "LOW"

    elif score <= 15:
        level = "MEDIUM"

    elif score <= 30:
        level = "HIGH"

    else:
        level = "CRITICAL"

    return score, level