#!/usr/bin/env python
def get_letter_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'

print get_letter_grade(100)
print get_letter_grade(90)
print get_letter_grade(80)
print get_letter_grade(70)
print get_letter_grade(60)
