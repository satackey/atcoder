from math import cos, radians, sqrt

a_hour_cm, b_min_cm, h_time_hour, m_time_min = map(int, input().split())

min_hand_angle = m_time_min * 6
hour_hand_angle = h_time_hour * 30 + m_time_min / 2

sandwiched_angle = abs(hour_hand_angle - min_hand_angle)

result = sqrt(a_hour_cm ** 2 + b_min_cm ** 2 - 2 * a_hour_cm * b_min_cm * cos(radians(sandwiched_angle)))
print(result)
