import random
class darts:
    q=0 
    k=0
    playfield=[]

    def __init__(self, q, k, field):
        self.q = q
        self.k = k
        self.plfield = field

    def getdarts(self):
        return self.q, self.k, self.plfield

    def setdarts(self, newq, newk, newfield):
        self.q = newq
        self.k = newk
        self.plfield = newfield

    def FindMaxScoreDark(self):
        max_sum=0
        if self.k >= 0 and self.k<=self.q-1:  
            snd_half = self.plfield[:self.k]
            fst_half = self.plfield[self.k+1:]
            self.plfield = fst_half + snd_half
            for i in range(0, len(self.plfield), 1):
                for j in range(0, -(len(self.plfield)), -1):
                    if j == 0:
                        iter_sum = sum(self.plfield[i:])
                    else:
                        iter_sum = sum(self.plfield[i:j])
                    if max_sum<iter_sum:
                        max_sum = iter_sum
        if max_sum != 0:
            return(max_sum)
        else:
            return('Черный сектор не установлен')

    def FindMaxScore(self):
        max_sum=0
        for k in range(0, len(self.plfield), 1):
            for i in range(0, len(self.plfield), 1):
                for j in range(0, -(len(self.plfield)), -1):
                    if j == 0:
                        iter_sum = sum(self.plfield[i:])
                    else:
                        iter_sum = sum(self.plfield[i:j])
                    if max_sum<iter_sum:
                        max_sum = iter_sum
            self.plfield=self.plfield[1:]+self.plfield[:1]
        return(max_sum)

    def BeHeading(self):
        print('Вы ведущий!')
        self.q=(int(input('Введите число секторов ')))
        self.k=(int(input('Введите число черного сектора ')))
        field=(str(input('Ввести поле самому [Y/N]?')))
        if field == 'Y':
            self.plfield=list(map(int, input('Введите список баллов секторов через пробел: ').split( )[:self.q]))
        elif field == 'N':
            self.plfield = [random.randint(-30, 30) for i in range(self.q)]
        else:
            print('Введено неверное значение!')
        
darkdarts = darts(8, 2, [2, 3, 4, 5, -30, 6, -1, 2])             
justdarts = darts(6, -1, [1, -3, 2, -2, 3, 4])
print('Тест #1: ', darkdarts.FindMaxScoreDark())
print('Тест #2: ', justdarts.FindMaxScore())

somedarts = darts(0, 0, [])         
somedarts.BeHeading()
print('Баллы: ', somedarts.playfield)
if somedarts.k >=0 and somedarts.k<=somedarts.n-1:
    print('Максимально возможный результат: ', somedarts.FindMaxScoreDark())
else:
    print('Максимально возможный результат: ', somedarts.FindMaxScore())