def letter_grade(score):
    if not isinstance(score, (int, float)):
        raise TypeError("score must be int of float")
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    else:
        return "F"

def is_passing(score):
    return True

def average(scores):
    pass
    
def curve_score(score, bonus):
    pass