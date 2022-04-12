from time import sleep


class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']

    def switch(self):
        i = 0
        while i < 3:
            print(f'\rГорит {TrafficLight.__color[i]} сигнал', end='')
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(3)
            elif i == 2:
                sleep(5)
            i += 1



TrafficLight = TrafficLight()
TrafficLight.switch()
