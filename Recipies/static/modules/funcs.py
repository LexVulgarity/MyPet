import time



#Таймер для обновления рецепта дня
def timer():
    first = 0
    sec = 0
    if first == 0:
        return True
    else:
        while sec < 60:
            time.sleep(1)
            sec += 30
            first = 1
        return True