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
    if not isinstance(score, (int, float)):
        raise TypeError("score must be int of float")
    return score >= 60

def average(scores):
    if not isinstance(scores, list):
        raise TypeError("scores must be a list")
    if len(scores) == 0:
        raise ValueError("length of scores can not be empty")
    if not all(isinstance(s, (int, float)) for s in scores):
        raise TypeError("invaild data types in list. All scors must be numbers")
    return round(sum(scores)/len(scores),2)
    
def curve_score(score, bonus):
    if bounus < 0:
        raise ValueError("bonus cannot be neagtive")
    return min(score+bonus, 100)

