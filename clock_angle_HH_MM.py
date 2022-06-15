# WAP to find angle between hr and min hand


def find_angle(t):
    hr = int(t.split(":")[0])
    min = int(t.split(":")[1])
    angle_min_hand = 6*min
    angle_hr_hand = 30*hr
    angle_hr_hand += min/2
    diff = angle_hr_hand-angle_min_hand
    if (abs(diff) >180):
        # print(360-abs(diff))
        return (360-abs(diff))
      
      
t = "07:20"
print(find_angle(t))
