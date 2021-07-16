# class Point:
#     def __init__(self,x=0,y=0):
#         self.__x=x
#         self.__y=y
#     def __str__(self):
#         return f"({self.__x},{self.__y})"
# class Prop:
#     def __init__(self,sp:Point,ep:Point,color:str="red",width:int=1):
#         self._sp=sp
#         self._ep=ep
#         self._color=color
#         self.__width=width
#     def getWidth(self):
#         return self.__width
# class Line(Prop):
#     def __init__(self,*args):
#         print("Переопределенный метод")
#         super().__init__(*args)
#     def drawLine(self):
#         print(f"Print line: {self._sp},{self._ep},{self._color},{self.getWidth()}")
#
# l=Line(Point(1,2),Point(10))
# l.drawLine()


class PC:
    def __init__(self,sizeData=0,disk="SSD",model="ASUS",cpu=4):
        self.s=sizeData
        self.d=disk
        self.m=model
        self.c=cpu
    def __str__(self):
        return f"({self.s},{self.d},{self.m},{self.c})"
class PersonalComputer(PC):
    def __init__(self,montor=None,mouse=None,weidth=8,lengh=0,*args):
        super().__init__(*args)
        self._monitor=montor
        self._mouse=mouse
        self._weidth=weidth
        self._lengh=lengh



    def drawLine(self):
         print(f"Параметры компа:\n"
               f"Размер диска: {self.s} \n"
               f"Тип диска: {self.d} \n"
               f"Модель: {self.m}\n"
               f"СPU: {self.c} \n"
               f"Монитор: {self._monitor}\n"
               f"Мышь: {self._mouse} \n"
               f"Ширина: {self._weidth}\n"
               f"Длина: {self._lengh}\n")
class Notebook(PC):
    def __init__(self,gabarite,diagonal,*args):
        super().__init__(*args)
        self.gabarite=gabarite
        self.deiagonal=diagonal
    def drawLine(self):
         print(f"Параметры компа:\n"
               f"Размер диска: {self.s} \n"
               f"Тип диска: {self.d} \n"
               f"Модель: {self.m}\n"
               f"СPU: {self.c} \n"
               f"Габариты: {self.gabarite}\n"
               f"Диагональ: {self.deiagonal} \n")



l=PersonalComputer("LG","Mouse",45,43)
l.drawLine()

n=Notebook(800,1500)
n.drawLine()




# class Pc:
#     def __init__(self, memory=1024, disc=None, model='Helwett Packard', cpu=4):
#         self.memory = memory
#         self.disc = disc
#         self.model = model
#         self.cpu = cpu
#
#     def __str__(self):
#         return '{}, {}, {}, {}'.format(self.memory, self.disc, self.model, self.cpu)
#
#
# class PersonPc(Pc):
#     def __init__(self, *args, monitor=None, klav=None, mouse=None, width=0, length=0):
#
#         super().__init__(*args)
#         self.monitor = monitor
#         self.klav = klav
#         self.mouse = mouse
#         self.width = width
#         self.length = length
#     def infoPc(self):
#         print( 'Настольный пк:'
#                'Монитор: {},'
#                'Клавиатура: {},'
#                'Мышь: {},'
#                'Ширина: {},'
#                'Длина: {},'
#                'Память: {},'
#                'Дсковод: {},'
#                'Модель: {},'
#                'CPU: {}'.format(
#         self.monitor,
#         self.klav,
#         self.mouse,
#         self.width,
#         self.length,
#         self.memory,
#         self.disc,
#         self.model,
#         self.cpu))
#
#
# class NoteBook(Pc):
#     def __init__(self,width=0, length=0,  *args ):
#         super().__init__(*args)
#         self.width = width
#         self.length = length
#
#     def infoPC(self):
#         print('Ширина: {},'
#               'Длина: {},'
#               'Память: {},'
#               'Дсковод: {},'
#               'Модель: {},'
#               'CPU: {}'.format(self.width,
#         self.length,
#         self.memory,
#         self.disc,
#         self.model,
#         self.cpu))
# p = PersonPc(monitor='LG', klav='ATECH', mouse='ATECH', width=1000, length=2000)
# p.infoPc()
# n = NoteBook(800, 1500)
# n.infoPC()
