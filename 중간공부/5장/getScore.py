# 점수를 입력 받아 학점을 구하는 로직

while(True):
    score = int(input("당신의 점수를 입력 : "))

    if score >= 90:
        if score >= 95:
            result = "A+"
        else :
            result = "A"
    elif score >= 80:
        if score >= 85:
            result = "B+"
        else :
            result = "B"
    elif score >= 70:
        if score >= 75:
            result = "C+"
        else :
            result = "C"
    elif score >= 60:
        if score >= 65:
            result = "D+"
        else :
            result = "D"
    else:
        result = "F"

    print(f"당신의 학점은 '{result}'입니다.")

    choice = str(input("종료 여부를 선택 (yes/no) :"))
    if choice == "yes":
        break