import random
import wx

class Dado():
    def __init__(self):
        self.numero = 0
        self.caras = 6
    def asignarValor(self):
        self.numero = random.randint(1, self.caras)

class Vaso():
    def __init__(self):
        self.dados = []
    def guardarDados(self, dado):
        self.dados.append(dado)
    def tirarDados(self):
        for i in range(0, (len(self.dados))):
            self.dados[i].asignarValor()

class Player():
    def __init__(self):
        self.puntosTurno = 0
        self.puntosTotales = 0
        self.dadosEnTurno = []
        self.nombre = str
        self.cont = 0

        self.tipo = "Player"
        self.seleccion = int


    def seleccionar(self, vaso):

        selec = int
        while (selec != 0):
            selec = int(input())
            for i in range(1, 7):
                self.opciones(selec, i, vaso)
    def seleccionar2(self, num):

        for i in range(1,7):
            self.opciones(self.seleccion, i , vaso)


    def opciones(self, selec, num,vaso):
        if(num == selec):
            self.dadosEnTurno.append(vaso.dados[num-1].numero)


class Maquina(Player):
    def __init__(self):

        self.seleccionOptima = []

    def seleccionar(self, vaso, plantar):

        selec = int
        self.analizarDados(vaso)
        l = 0
        while (selec != 0):
            selec = self.seleccionOptima[l]
            for i in range(1, 7):
                self.opciones(selec, i, vaso)
            l += 1
        plantar = "y"

    def analizarDados(self, vaso):
        for i in range(0, len(vaso.dados)):
            cont = vaso.dados.count(i+1)
            if (cont >= 3):
                self.seleccionOptima.append(i+1)
            elif (cont < 3):
                if (vaso.dados[i].numero == 1):
                    self.seleccionOptima.append(i+1)
                if (vaso.dados[i].numero == 5):
                    self.seleccionOptima.append(i+1)
        self.seleccionOptima.append(0)

class Turnos():
    def __init__(self, player, vaso, dadosList):
        self.player = player
        self.vaso = vaso
        self.dadosList = dadosList
        self.dadosEnTurno = []
        self.puntosEnTurno = 0
        self.dadosResta = 0
        self.verifica = bool
        self.puntosAux = 0
        self.plantar = str

    def empezar(self):
        self.verifica = False
        self.player.dadosEnTurno = []
        self.vaso.dados = []

        for i in range(0, (6 - self.dadosResta)):
            self.vaso.guardarDados(dadoList[i])


        self.plantar = "y"
        pass


    def setear(self):
        cont = 1

        self.puntosEnTurno = 0
        self.plantar = str


    def calcularPuntos(self, dados):

        dados.sort()


        if (dados == [1, 2 ,3 ,4, 5]):
            self.puntosEnTurno += 2500
        for i in range(1, 7):
            cont = dados.count(i)

            if (cont >= 3):
                self.puntos(i)

            elif(cont < 3):

                if (i == 1):

                    self.puntosEnTurno += 100 * cont




                if (i == 5):
                    self.puntosEnTurno += 50 * cont


    def puntos(self, num):


        if (num == 1):
            self.puntosEnTurno += 1000
        for i in range(2, 6):
            self.otrosNum(num, i)
        if (num == 6):
            self.puntosEnTurno += 600


    def plantarse(self):
        self.player.puntosTotales += self.puntosEnTurno



    def otrosNum(self, num, num2):
        if (num == num2):
            self.puntosEnTurno += 100*num2



    def verificar(self):
        for i in range(0, len(self.vaso.dados)):
            cont = self.vaso.dados.count(i)
            if (cont >= 3):
                self.verifica = True
            elif (cont < 3):
                if (self.vaso.dados[i].numero == 1):
                    self.verifica = True
                if (self.vaso.dados[i].numero == 5):
                    self.verifica = True

class Juego():
    def __init__(self, player1, player2, maquina, vaso, dados):
        self.player1 = player1
        self.player2 = player2
        self.maquina = maquina
        self.vaso = vaso
        self.dados = dados
        self.limite = 10000
        self.final = False
        self.modo = str
        self.oponente = []
        self.playerEnTurno = int
        self.turno1 = Turnos
        self.turno2 = Turnos
        self.ganador = Player

    def modoDeJuego(self):
        self.modo = int(input("Seleccionar modo de juego: \n1)Jugador Vs Jugador\n2)Jugador vs Maquina\n"))

    def maquina(self):
        self.oponente = self.maquina
    def jugar(self):

        self.oponente = self.player2



        self.turno1 = Turnos(self.player1, self.vaso, self.dados)
        self.turno2 = Turnos(self.oponente, self.vaso, self.dados)

        self.playerEnTurno = self.player1.nombre



#Creando los Dados
dado1 = Dado()
dado2 = Dado()
dado3 = Dado()
dado4 = Dado()
dado5 = Dado()
dado6 = Dado()
dadoList = [dado1, dado2, dado3, dado4, dado5, dado6]

#Creando el Vaso
vaso = Vaso()

#Creando Tipos de Jugadores
player1 = Player()
player2 = Player()
maquina = Maquina()



class VentanaMain(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent = parent)
        self.frame = parent
        sizer = wx.BoxSizer(wx.VERTICAL)
        h_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.SetSizer(h_sizer)
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.background)



        # Botones

        panel = VentanaChoose(self)

        #sizer.Add(startGame, 0, wx.ALL, 5)
        #sizer.Add(loadGame, 0, wx.ALL, 5)
        #sizer.Add(optionGame, 0, wx.ALL, 5)
        #sizer.Add(exitGame, 0, wx.ALL, 5)


        #EVENTOS



    def background (self, event):
        dc = event.GetDC()
        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRegion(rect)
        dc.Clear()
        fondo = wx.Bitmap('assets/fondo.jpg')
        dc.DrawBitmap(fondo, 0, 0)

game = Juego(player1, player2, maquina, vaso, dadoList)

class VentanaChoose(wx.Panel):
    def __init__(self, parent):

        wx.Panel.__init__(self, parent=parent)
        self.frame = parent

        sizer = wx.BoxSizer(wx.VERTICAL)
        h_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.SetSizer(h_sizer)
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.background)


        self.boolPvp = bool

        # Seleccion
        selec1 = wx.RadioButton(self, -1, "PVP", pos=(125, 380), size=(40, 20))
        selec2 = wx.RadioButton(self, -1, "PVE", pos=(350, 380), size=(40, 20))
        # Input Limite
        self.limite = wx.TextCtrl(self, -1, "", pos=(90, 500), size=(200, 20))
        aceptar = wx.Button(self, -1, "Aceptar", pos=(300, 500), size=(80, 20))

        empezar=wx.Button(self, -1, "Empezar Juego", pos=(150, 600), size=(200, 20))


        #TEXTOS
        texto = wx.StaticText(self, -1, "Seleccione el Tipo de Juego: ", pos=(90, 150))
        texto2 = wx.StaticText(self, -1, "Establezca Puntuacion Limite: ", pos=(90, 450))

        #FUENTE TEXTO
        font1=texto.GetFont()
        font1.SetPointSize(20)
        font2 = texto.GetFont()
        font2.SetPointSize(10)
        texto.SetFont(font1)
        texto.SetBackgroundColour("#612773")
        texto.SetForegroundColour("#FFFFFF")
        texto2.SetFont(font1)
        texto2.SetBackgroundColour("#612773")
        texto2.SetForegroundColour("#FFFFFF")
        self.limite.SetFont(font2)
        self.limite.SetBackgroundColour("#612773")
        self.limite.SetForegroundColour("#FFFFFF")

        #Imagenes
        jcj = wx.StaticBitmap(self, -1, wx.Bitmap('assets/pvp.jpg', wx.BITMAP_TYPE_ANY), pos=wx.Point(60, 250), size=(171, 95))
        jce = wx.StaticBitmap(self, -1, wx.Bitmap('assets/pve.jpg', wx.BITMAP_TYPE_ANY), pos=wx.Point(270, 250), size=(171, 95))

        #Eventos
        selec1.Bind(wx.EVT_RADIOBUTTON, self.pvp)
        selec2.Bind(wx.EVT_RADIOBUTTON, self.pve)
        aceptar.Bind(wx.EVT_BUTTON, self.aceptar)
        empezar.Bind(wx.EVT_BUTTON, self.empezar)


    def background (self, event):
        dc = event.GetDC()
        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRegion(rect)
        dc.Clear()
        fondo = wx.Bitmap('assets/fondo.jpg')
        dc.DrawBitmap(fondo, 0, 0)

    def pvp (self, event):
        game.modo = 1
        self.boolPvp = True

    def pve(self, event):
        game.modo = 2
        self.boolPvp = False

    def aceptar(self, event):
        game.limite = int(self.limite.GetValue())
        print("Se ha establecido como limite:", game.limite)
    def empezar(self, event):
        if(self.boolPvp == True):

            app = wx.App(self)
            nombres = Pvp()
            app.MainLoop()

        if(self.boolPvp == False):
            game.player1.nombre = "Jugador"
            app = wx.App(self)
            vsMaq = JuegoMaq()
            app.MainLoop()

        self.Close()
class Jcj(wx.Panel):
    def __init__(self, parent):

        wx.Panel.__init__(self, parent=parent)
        self.frame = parent

        sizer = wx.BoxSizer(wx.VERTICAL)
        h_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.SetSizer(h_sizer)
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.background)


        self.j1Input = wx.TextCtrl(self, -1, "", pos=(250, 460), size=(160, 20))
        self.j2Input = wx.TextCtrl(self, -1, "", pos=(250, 500), size=(160, 20))
        jugar = wx.Button(self, -1, "JUGAR!", pos=(105, 600), size=(300, 40))


        # FONDO

        self.SetBackgroundColour("#000000")


        self.Centre()

        # TEXTOS
        j1 = wx.StaticText(self, -1, "Nombre del Primer Jugador: ", pos=(40, 460))
        j2 = wx.StaticText(self, -1, "Nombre del Segundo Jugador: ", pos=(40, 500))

        #FUENTE TEXTO
        font1=j1.GetFont()
        font1.SetPointSize(10)
        j1.SetFont(font1)
        j1.SetBackgroundColour("#612773")
        j1.SetForegroundColour("#FFFFFF")
        j2.SetFont(font1)
        j2.SetBackgroundColour("#612773")
        j2.SetForegroundColour("#FFFFFF")

        #Imagenes
        jcj = wx.StaticBitmap(self, -1, wx.Bitmap('assets/pvp.jpg', wx.BITMAP_TYPE_ANY), pos=wx.Point(150, 250), size=(171, 95))


        #Eventos
        jugar.Bind(wx.EVT_BUTTON, self.jugar)

    def background (self, event):
        dc = event.GetDC()
        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRegion(rect)
        dc.Clear()
        fondo = wx.Bitmap('assets/fondo.jpg')
        dc.DrawBitmap(fondo, 0, 0)

    def jugar(self, event):

        game.player1.nombre = self.j1Input.GetValue()
        game.player2.nombre = self.j2Input.GetValue()
        self.Close()
        app = wx.App(self)
        juego = Juego()
        app.MainLoop()
class Game(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        self.frame = parent
        self.nombreEnTurno = str
        sizer = wx.BoxSizer(wx.VERTICAL)
        h_sizer = wx.BoxSizer(wx.HORIZONTAL)



        self.dadosInGame = ["prueba"]
        self.func = [self.guardarDado1, self.guardarDado2, self.guardarDado3, self.guardarDado4, self.guardarDado5, self.guardarDado6]
        self.cont = 0
        self.contTurn = 0
        self.SetSizer(h_sizer)
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.background)
        self.dados = []
        self.signo = wx.Bitmap("assets/signo.jpg", wx.BITMAP_TYPE_ANY)
        self.dadosInGame2 = []

        game.jugar()
        self.numTurno = 0

        self.cont1 = 0
        self.cont2 = 0
        self.cont3 = 0
        self.cont4 = 0
        self.cont5 = 0
        self.cont6 = 0
        self.contNum = [self.cont1, self.cont2, self.cont3, self.cont4, self.cont5, self.cont6]




        # Boton
        plantarse = wx.Button(self, label="Plantarse", pos=(120, 600), style=wx.BU_EXACTFIT, size=(100, 50))
        saveGame = wx.Button(self, label="Guardar Partida", pos=(400, 20), style=wx.BU_EXACTFIT, size=(100, 20))
        roll = wx.Button(self, label="Roll", pos=(280, 600), style=wx.BU_EXACTFIT, size=(100, 50))


        # Textos
        turno = wx.StaticText(self, -1, "Turno de :    ", pos=(75, 40))
        self.jugador = wx.StaticText(self, -1, "", pos=(280, 40))

        self.puntosEnTurno = wx.StaticText(self, -1, "Puntos:    ", pos=(175, 110))
        self.puntosEnTurno2 = wx.StaticText(self, -1, str(game.turno1.puntosEnTurno), pos=(280, 110))




        self.p1Static = wx.StaticText(self, -1, game.player1.nombre, pos=(350, 200))
        self.p2Static = wx.StaticText(self, -1, game.oponente.nombre, pos=(350, 350))
        self.puntosTotalesP1 = wx.StaticText(self, -1, "Puntos Totales:    ", pos=(300, 250))
        self.puntosTotalesP12 = wx.StaticText(self, -1, str(game.player1.puntosTotales), pos=(450, 250))
        self.puntosTotalesP2 = wx.StaticText(self, -1, "Puntos Totales:    ", pos=(300, 400))
        self.puntosTotalesP22 = wx.StaticText(self, -1, str(game.player1.puntosTotales), pos=(450, 400))



        # Fuentes
        font1 = turno.GetFont()
        font1.SetPointSize(30)
        font2 = self.puntosEnTurno.GetFont()
        font2.SetPointSize(18)
        font3 = self.p1Static.GetFont()
        font3.SetPointSize(10)


        turno.SetFont(font1)
        self.puntosEnTurno.SetFont(font2)

        self.puntosEnTurno2.SetFont(font2)

        self.p1Static.SetFont(font2)
        self.p2Static.SetFont(font2)
        self.puntosTotalesP1.SetFont(font3)
        self.puntosTotalesP12.SetFont(font3)
        self.puntosTotalesP2.SetFont(font3)
        self.puntosTotalesP22.SetFont(font3)
        self.puntosEnTurno2.SetBackgroundColour("#612773")
        self.puntosEnTurno2.SetForegroundColour("#FFFFFF")
        turno.SetBackgroundColour("#612773")
        turno.SetForegroundColour("#FFFFFF")
        self.puntosEnTurno.SetForegroundColour("#FFFFFF")
        self.puntosEnTurno.SetBackgroundColour("#612773")

        self.p1Static.SetBackgroundColour("#612773")
        self.p2Static.SetBackgroundColour("#612773")
        self.puntosTotalesP1.SetBackgroundColour("#612773")
        self.puntosTotalesP12.SetBackgroundColour("#612773")
        self.puntosTotalesP2.SetBackgroundColour("#612773")
        self.puntosTotalesP22.SetBackgroundColour("#612773")

        self.p1Static.SetForegroundColour("#FFFFFF")
        self.p2Static.SetForegroundColour("#FFFFFF")
        self.puntosTotalesP1.SetForegroundColour("#FFFFFF")
        self.puntosTotalesP12.SetForegroundColour("#FFFFFF")
        self.puntosTotalesP2.SetForegroundColour("#FFFFFF")
        self.puntosTotalesP22.SetForegroundColour("#FFFFFF")

        self.jugador.SetFont(font1)
        self.jugador.SetBackgroundColour("#612773")
        self.jugador.SetForegroundColour("#FFFFFF")

        # posiciones de dados
        self.pos1 = 170
        self.pos2 = 230
        self.pos3 = 290
        self.pos4 = 350
        self.pos5 = 410
        self.pos6 = 470
        self.posicionesDados = (170, 230, 290, 350, 410, 470)

        # Fotos

        self.carasNombres = ['assets/cara1.jpg', 'assets/cara2.jpg', 'assets/cara3.jpg', 'assets/cara4.jpg', 'assets/cara5.jpg', 'assets/cara6.jpg']

        self.cara1 = wx.BitmapButton(self, -1, wx.Bitmap('assets/signo.jpg', wx.BITMAP_TYPE_ANY), pos=wx.Point(110, 170), size=(50, 50))
        self.cara2 = wx.BitmapButton(self, -1, wx.Bitmap('assets/signo.jpg', wx.BITMAP_TYPE_ANY), pos=wx.Point(110, 230), size=(50, 50))
        self.cara3 = wx.BitmapButton(self, -1, wx.Bitmap('assets/signo.jpg', wx.BITMAP_TYPE_ANY), pos=wx.Point(110, 290), size=(50, 50))
        self.cara4 = wx.BitmapButton(self, -1, wx.Bitmap('assets/signo.jpg', wx.BITMAP_TYPE_ANY), pos=wx.Point(110, 350), size=(50, 50))
        self.cara5 = wx.BitmapButton(self, -1, wx.Bitmap('assets/signo.jpg', wx.BITMAP_TYPE_ANY), pos=wx.Point(110, 410), size=(50, 50))
        self.cara6 = wx.BitmapButton(self, -1, wx.Bitmap('assets/signo.jpg', wx.BITMAP_TYPE_ANY), pos=wx.Point(110, 470), size=(50, 50))
        self.caras = [self.cara1, self.cara2, self.cara3, self.cara4, self.cara5, self.cara6]

        # EVENTOS
        plantarse.Bind(wx.EVT_BUTTON, self.plantarse)
        self.Bind(wx.EVT_BUTTON, self.rollDados, roll)
        saveGame.Bind(wx.EVT_BUTTON, self.guardar)

        self.turnosJuego()

    def turnosJuego(self):

        self.nombreEnTurno = game.playerEnTurno
        self.jugador.SetLabel(self.nombreEnTurno)

    def plantarse(self, event):

        self.turnos[self.numTurno].calcularPuntos(self.dadosInGame)
        self.turnos[self.numTurno].plantarse()
        self.endTurn()

    def rollDados(self, event):

        for i in range(0, 6):
            self.contNum[i] = 0


        self.turnos = [game.turno1, game.turno2]
        if self.dadosInGame == []:
            self.endTurn()
        else:

            self.dadosInGame = []
            self.turnos[self.numTurno].verifica = True
            self.turnos[self.numTurno].setear()
            self.turnos[self.numTurno].empezar()
            self.turnos[self.numTurno].vaso.tirarDados()

            if (self.contTurn == 0):
                self.turnos[self.numTurno].verificar()
            else:
                self.turnos[self.numTurno].verifica = True
            self.turnos[self.numTurno].calcularPuntos(self.dadosInGame2)
            self.puntosEnTurno2.SetLabelText(str(self.turnos[self.numTurno].puntosEnTurno))

            if (self.turnos[self.numTurno].verifica == True):

                self.contTurn = 0

                for i in range(0, (6 - self.turnos[self.numTurno].dadosResta)):
                    self.crearDados(i, self.turnos[self.numTurno].vaso.dados[i].numero)
                for i in range((6 - self.turnos[self.numTurno].dadosResta), 6):
                    self.caras[i].SetBitmap(self.signo)
                self.cont += 1


            else:

                self.endTurn()

    def endTurn(self):

        if (self.numTurno == 0):
            self.puntosTotalesP12.SetLabelText(str(self.turnos[self.numTurno].player.puntosTotales))
        elif(self.numTurno == 1):
            self.puntosTotalesP22.SetLabelText(str(self.turnos[self.numTurno].player.puntosTotales))

        if game.player1.puntosTotales >= game.limite or game.oponente.puntosTotales >= game.limite:

            game.ganador = self.turnos[self.numTurno].player
            self.endGame()
        else:
            self.turnos[self.numTurno].dadosResta = 0
            for i in range(0, 6):
                self.caras[i].SetBitmap(self.signo)
            if self.numTurno == 0:
                self.numTurno = 1
            elif self.numTurno == 1:
                self.numTurno = 0
            self.contTurn = 1
            self.dadosInGame = ["prueba"]
            self.puntosEnTurno2.SetLabelText(str(self.turnos[self.numTurno].puntosEnTurno))
            # self.puntosTotales2.SetLabelText(str(game.player1.puntosTotales))
            self.dadosInGame2 = []
            self.turnos[self.numTurno].puntosEnTurno = 0

            self.jugador.SetLabel(self.turnos[self.numTurno].player.nombre)
            self.dadosResta = 0

    def crearDados(self, pos, num):
        y = self.posicionesDados[pos]

        self.caras[pos-1].SetBitmap(wx.Bitmap(self.carasNombres[num-1], wx.BITMAP_TYPE_ANY))
        self.caras[pos-1].Bind(wx.EVT_BUTTON, self.func[num-1])

    def ocultarDados(self, pos, num):
        y = self.posicionesDados[pos]
        self.caras[num - 1].SetBitmap(self.signo)

    def guardarDado1(self, event):

        self.dadosInGame.append(1)
        self.dadosInGame2.append(1)
        self.turnos[self.numTurno].dadosResta += 1
    def guardarDado2(self, event):

        self.dadosInGame.append(2)
        self.dadosInGame2.append(2)
        self.turnos[self.numTurno].dadosResta += 1
    def guardarDado3(self, event):

        self.dadosInGame.append(3)
        self.dadosInGame2.append(3)
        self.turnos[self.numTurno].dadosResta += 1
    def guardarDado4(self, event):

        self.dadosInGame.append(4)
        self.dadosInGame2.append(4)
        self.turnos[self.numTurno].dadosResta += 1
    def guardarDado5(self, event):

        self.dadosInGame.append(5)
        self.dadosInGame2.append(5)
        self.turnos[self.numTurno].dadosResta += 1
    def guardarDado6(self, event):

        self.dadosInGame.append(6)
        self.dadosInGame2.append(6)
        self.turnos[self.numTurno].dadosResta += 1

    def endGame(self):
        app = wx.App(self)
        final = FinDelJuego()
        app.MainLoop()

    def background (self, event):
        dc = event.GetDC()
        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRegion(rect)
        dc.Clear()
        fondo = wx.Bitmap('assets/fondo2.png')
        dc.DrawBitmap(fondo, 0, 0)

    def guardar(self, event):
        print("Partida Guardada!")
        saves = open("saves.txt","w")
        saves.write(str(self.numTurno))
        saves.write("\n")
        saves.write(str(game.limite))
        saves.write("\n")
        saves.write(str(game.player1.nombre))
        saves.write("\n")
        saves.write(str(game.player1.puntosTotales))
        saves.write("\n")
        saves.write(str(game.oponente.nombre))
        saves.write("\n")
        saves.write(str(game.oponente.puntosTotales))
        saves.close()
class GameMaq(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        self.frame = parent
        self.nombreEnTurno = str
        sizer = wx.BoxSizer(wx.VERTICAL)
        h_sizer = wx.BoxSizer(wx.HORIZONTAL)



        self.dadosInGame = ["prueba"]
        self.func = [self.guardarDado1, self.guardarDado2, self.guardarDado3, self.guardarDado4, self.guardarDado5, self.guardarDado6]
        self.cont = 0
        self.contTurn = 0
        self.SetSizer(h_sizer)
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.background)
        self.dados = []
        self.signo = wx.Bitmap("assets/signo.jpg", wx.BITMAP_TYPE_ANY)
        self.dadosInGame2 = []
        self.mejores=[]
        self.verifica = []

        game.jugar()
        self.numTurno = 0

        self.cont1 = 0
        self.cont2 = 0
        self.cont3 = 0
        self.cont4 = 0
        self.cont5 = 0
        self.cont6 = 0
        self.contNum = [self.cont1, self.cont2, self.cont3, self.cont4, self.cont5, self.cont6]




        # Boton
        plantarse = wx.Button(self, label="Plantarse", pos=(120, 600), style=wx.BU_EXACTFIT, size=(100, 50))
        saveGame = wx.Button(self, label="Guardar Partida", pos=(400, 20), style=wx.BU_EXACTFIT, size=(100, 20))
        roll = wx.Button(self, label="Roll", pos=(280, 600), style=wx.BU_EXACTFIT, size=(100, 50))


        # Textos
        turno = wx.StaticText(self, -1, "Turno de :    ", pos=(75, 40))
        self.jugador = wx.StaticText(self, -1, "", pos=(280, 40))

        self.puntosEnTurno = wx.StaticText(self, -1, "Puntos:    ", pos=(175, 110))
        self.puntosEnTurno2 = wx.StaticText(self, -1, str(game.turno1.puntosEnTurno), pos=(280, 110))




        self.p1Static = wx.StaticText(self, -1, game.player1.nombre, pos=(350, 200))
        self.p2Static = wx.StaticText(self, -1, "Maquina", pos=(350, 350))
        self.puntosTotalesP1 = wx.StaticText(self, -1, "Puntos Totales:    ", pos=(300, 250))
        self.puntosTotalesP12 = wx.StaticText(self, -1, str(game.player1.puntosTotales), pos=(450, 250))
        self.puntosTotalesP2 = wx.StaticText(self, -1, "Puntos Totales:    ", pos=(300, 400))
        self.puntosTotalesP22 = wx.StaticText(self, -1, str(game.player1.puntosTotales), pos=(450, 400))



        # Fuentes
        font1 = turno.GetFont()
        font1.SetPointSize(30)
        font2 = self.puntosEnTurno.GetFont()
        font2.SetPointSize(18)
        font3 = self.p1Static.GetFont()
        font3.SetPointSize(10)


        turno.SetFont(font1)
        self.puntosEnTurno.SetFont(font2)

        self.puntosEnTurno2.SetFont(font2)

        self.p1Static.SetFont(font2)
        self.p2Static.SetFont(font2)
        self.puntosTotalesP1.SetFont(font3)
        self.puntosTotalesP12.SetFont(font3)
        self.puntosTotalesP2.SetFont(font3)
        self.puntosTotalesP22.SetFont(font3)
        self.puntosEnTurno2.SetBackgroundColour("#612773")
        self.puntosEnTurno2.SetForegroundColour("#FFFFFF")
        turno.SetBackgroundColour("#612773")
        turno.SetForegroundColour("#FFFFFF")
        self.puntosEnTurno.SetForegroundColour("#FFFFFF")
        self.puntosEnTurno.SetBackgroundColour("#612773")

        self.p1Static.SetBackgroundColour("#612773")
        self.p2Static.SetBackgroundColour("#612773")
        self.puntosTotalesP1.SetBackgroundColour("#612773")
        self.puntosTotalesP12.SetBackgroundColour("#612773")
        self.puntosTotalesP2.SetBackgroundColour("#612773")
        self.puntosTotalesP22.SetBackgroundColour("#612773")

        self.p1Static.SetForegroundColour("#FFFFFF")
        self.p2Static.SetForegroundColour("#FFFFFF")
        self.puntosTotalesP1.SetForegroundColour("#FFFFFF")
        self.puntosTotalesP12.SetForegroundColour("#FFFFFF")
        self.puntosTotalesP2.SetForegroundColour("#FFFFFF")
        self.puntosTotalesP22.SetForegroundColour("#FFFFFF")

        self.jugador.SetFont(font1)
        self.jugador.SetBackgroundColour("#612773")
        self.jugador.SetForegroundColour("#FFFFFF")

        # posiciones de dados
        self.pos1 = 170
        self.pos2 = 230
        self.pos3 = 290
        self.pos4 = 350
        self.pos5 = 410
        self.pos6 = 470
        self.posicionesDados = (170, 230, 290, 350, 410, 470)

        # Fotos

        self.carasNombres = ['assets/cara1.jpg', 'assets/cara2.jpg', 'assets/cara3.jpg', 'assets/cara4.jpg', 'assets/cara5.jpg', 'assets/cara6.jpg']

        self.cara1 = wx.BitmapButton(self, -1, wx.Bitmap('assets/signo.jpg', wx.BITMAP_TYPE_ANY), pos=wx.Point(110, 170), size=(50, 50))
        self.cara2 = wx.BitmapButton(self, -1, wx.Bitmap('assets/signo.jpg', wx.BITMAP_TYPE_ANY), pos=wx.Point(110, 230), size=(50, 50))
        self.cara3 = wx.BitmapButton(self, -1, wx.Bitmap('assets/signo.jpg', wx.BITMAP_TYPE_ANY), pos=wx.Point(110, 290), size=(50, 50))
        self.cara4 = wx.BitmapButton(self, -1, wx.Bitmap('assets/signo.jpg', wx.BITMAP_TYPE_ANY), pos=wx.Point(110, 350), size=(50, 50))
        self.cara5 = wx.BitmapButton(self, -1, wx.Bitmap('assets/signo.jpg', wx.BITMAP_TYPE_ANY), pos=wx.Point(110, 410), size=(50, 50))
        self.cara6 = wx.BitmapButton(self, -1, wx.Bitmap('assets/signo.jpg', wx.BITMAP_TYPE_ANY), pos=wx.Point(110, 470), size=(50, 50))
        self.caras = [self.cara1, self.cara2, self.cara3, self.cara4, self.cara5, self.cara6]

        # EVENTOS
        plantarse.Bind(wx.EVT_BUTTON, self.plantarse)
        self.Bind(wx.EVT_BUTTON, self.rollDados, roll)
        saveGame.Bind(wx.EVT_BUTTON, self.guardar)

        self.turnosJuego()

    def turnosJuego(self):

        self.nombreEnTurno = game.playerEnTurno
        self.jugador.SetLabel(self.nombreEnTurno)

    def plantarse(self, event):

        self.turnos[self.numTurno].calcularPuntos(self.dadosInGame)
        self.turnos[self.numTurno].plantarse()
        self.endTurn()

    def rollDados(self, event):

        for i in range(0, 6):
            self.contNum[i] = 0


        self.turnos = [game.turno1, game.turno2]
        if self.dadosInGame == []:
            self.endTurn()
        else:
            if self.numTurno == 0:
                self.dadosInGame = []
                self.turnos[self.numTurno].verifica = True
                self.turnos[self.numTurno].setear()
                self.turnos[self.numTurno].empezar()
                self.turnos[self.numTurno].vaso.tirarDados()

                if (self.contTurn == 0):
                    self.turnos[self.numTurno].verificar()
                else:
                    self.turnos[self.numTurno].verifica = True
                self.turnos[self.numTurno].calcularPuntos(self.dadosInGame2)
                self.puntosEnTurno2.SetLabelText(str(self.turnos[self.numTurno].puntosEnTurno))

                if (self.turnos[self.numTurno].verifica == True):

                    self.contTurn = 0

                    for i in range(0, (6 - self.turnos[self.numTurno].dadosResta)):
                        self.crearDados(i, self.turnos[self.numTurno].vaso.dados[i].numero)
                    for i in range((6 - self.turnos[self.numTurno].dadosResta), 6):
                        self.caras[i].SetBitmap(self.signo)
                    self.cont += 1


                else:

                    self.endTurn()
            else:
                self.dadosInGame = []
                self.turnos[self.numTurno].verifica = True
                self.turnos[self.numTurno].setear()
                self.turnos[self.numTurno].empezar()
                self.turnos[self.numTurno].vaso.tirarDados()

                if (self.contTurn == 0):
                    self.turnos[self.numTurno].verificar()
                else:
                    self.turnos[self.numTurno].verifica = True
                self.turnos[self.numTurno].calcularPuntos(self.dadosInGame2)
                self.puntosEnTurno2.SetLabelText(str(self.turnos[self.numTurno].puntosEnTurno))

                if (self.turnos[self.numTurno].verifica == True):

                    self.contTurn = 0

                    for i in range(0, (6 - self.turnos[self.numTurno].dadosResta)):
                        self.crearDados(i, self.turnos[self.numTurno].vaso.dados[i].numero)

                    for i in range((6 - self.turnos[self.numTurno].dadosResta), 6):
                        self.caras[i].SetBitmap(self.signo)
                    self.cont += 1

                self.bestDados(self.turnos[self.numTurno].vaso.dados)
                print("Falto terminar sistema de guardado de dados de la Maquina\n\n")
                self.elegirDados(self.verifica)



    def bestDados(self, dados):

        for i in range(0, (6 - self.turnos[self.numTurno].dadosResta)):
            cont = dados.count(dados[i])

            if dados[i].numero == 1 or dados[i].numero==5:
                self.verifica.append(i)

            else:
                if cont > 2:
                    self.verifica.append(i)
    def elegirDados(self, indices):

        for i in range(0, (6 - self.turnos[self.numTurno].dadosResta)):
            if indices[i] == 0:
                evt1 = wx.PyCommandEvent(wx.EVT_BUTTON, self.guardarDado1())
                wx.PostEvent(self, evt1)
            elif indices[i] == 1:
                evt2 = wx.PyCommandEvent(wx.EVT_BUTTON.typeId, self.guardarDado2.GetId())
                wx.PostEvent(self, evt2)
            elif indices[i] == 2:
                evt3 = wx.PyCommandEvent(wx.EVT_BUTTON.typeId, self.guardarDado3.GetId())
                wx.PostEvent(self, evt3)
            elif indices[i] == 3:
                evt4 = wx.PyCommandEvent(wx.EVT_BUTTON.typeId, self.guardarDado4.GetId())
                wx.PostEvent(self, evt4)
            elif indices[i] == 4:
                evt5 = wx.PyCommandEvent(wx.EVT_BUTTON.typeId, self.guardarDado5.GetId())
                wx.PostEvent(self, evt5)
            elif indices[i] == 5:
                evt6 = wx.PyCommandEvent(wx.EVT_BUTTON.typeId, self.guardarDado6.GetId())
                wx.PostEvent(self, evt6)

        self.endTurn()

    def endTurn(self):

        if (self.numTurno == 0):
            self.puntosTotalesP12.SetLabelText(str(self.turnos[self.numTurno].player.puntosTotales))
        elif(self.numTurno == 1):
            self.puntosTotalesP22.SetLabelText(str(self.turnos[self.numTurno].player.puntosTotales))

        if game.player1.puntosTotales >= game.limite or game.oponente.puntosTotales >= game.limite:

            game.ganador = self.turnos[self.numTurno].player
            self.endGame()
        else:
            self.turnos[self.numTurno].dadosResta = 0
            for i in range(0, 6):
                self.caras[i].SetBitmap(self.signo)
            if self.numTurno == 0:
                self.numTurno = 1
                self.jugador.SetLabel("Maquina")
            elif self.numTurno == 1:
                self.numTurno = 0
                self.jugador.SetLabel(self.turnos[self.numTurno].player.nombre)
            self.contTurn = 1
            self.dadosInGame = ["prueba"]
            self.puntosEnTurno2.SetLabelText(str(self.turnos[self.numTurno].puntosEnTurno))
            # self.puntosTotales2.SetLabelText(str(game.player1.puntosTotales))
            self.dadosInGame2 = []
            self.turnos[self.numTurno].puntosEnTurno = 0


            self.dadosResta = 0

    def crearDados(self, pos, num):
        y = self.posicionesDados[pos]

        self.caras[pos-1].SetBitmap(wx.Bitmap(self.carasNombres[num-1], wx.BITMAP_TYPE_ANY))
        self.caras[pos-1].Bind(wx.EVT_BUTTON, self.func[num-1])

    def ocultarDados(self, pos, num):
        y = self.posicionesDados[pos]
        self.caras[num - 1].SetBitmap(self.signo)

    def guardarDado1(self, event):

        self.dadosInGame.append(1)
        self.dadosInGame2.append(1)
        self.turnos[self.numTurno].dadosResta += 1
    def guardarDado2(self, event):

        self.dadosInGame.append(2)
        self.dadosInGame2.append(2)
        self.turnos[self.numTurno].dadosResta += 1
    def guardarDado3(self, event):

        self.dadosInGame.append(3)
        self.dadosInGame2.append(3)
        self.turnos[self.numTurno].dadosResta += 1
    def guardarDado4(self, event):

        self.dadosInGame.append(4)
        self.dadosInGame2.append(4)
        self.turnos[self.numTurno].dadosResta += 1
    def guardarDado5(self, event):

        self.dadosInGame.append(5)
        self.dadosInGame2.append(5)
        self.turnos[self.numTurno].dadosResta += 1
    def guardarDado6(self, event):

        self.dadosInGame.append(6)
        self.dadosInGame2.append(6)
        self.turnos[self.numTurno].dadosResta += 1

    def endGame(self):
        app = wx.App(self)
        final = FinDelJuego()
        app.MainLoop()

    def background (self, event):
        dc = event.GetDC()
        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRegion(rect)
        dc.Clear()
        fondo = wx.Bitmap('assets/fondo2.png')
        dc.DrawBitmap(fondo, 0, 0)

    def guardar(self, event):
        print("Partida Guardada!")
        saves = open("saves.txt","w")
        saves.write(str(self.numTurno))
        saves.write("\n")
        saves.write(str(game.limite))
        saves.write("\n")
        saves.write(str(game.player1.nombre))
        saves.write("\n")
        saves.write(str(game.player1.puntosTotales))
        saves.write("\n")
        saves.write(str(game.oponente.nombre))
        saves.write("\n")
        saves.write(str(game.oponente.puntosTotales))
        saves.close()
class Final(wx.Panel):
    def __init__(self, parent):

        wx.Panel.__init__(self, parent=parent)
        self.frame = parent

        sizer = wx.BoxSizer(wx.VERTICAL)
        h_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.SetSizer(h_sizer)
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.background)

        ganador = wx.StaticText(self, -1, "El ganador fue:        ", pos=(40, 460))
        jugador = wx.StaticText(self, -1, game.ganador.nombre, pos=(350, 460))
        puntos = wx.StaticText(self, -1, "Puntuacion:        ", pos=(40, 560))
        puntuacion = wx.StaticText(self, -1, str(game.ganador.puntosTotales), pos=(200, 560))
        font1 = ganador.GetFont()
        font2 = puntos.GetFont()

        font1.SetPointSize(30)
        font2.SetPointSize(20)

        ganador.SetFont(font1)
        ganador.SetBackgroundColour("#612773")
        ganador.SetForegroundColour("#FFFFFF")
        jugador.SetFont(font1)
        jugador.SetBackgroundColour("#612773")
        jugador.SetForegroundColour("#FFFFFF")
        puntos.SetFont(font2)
        puntos.SetBackgroundColour("#612773")
        puntos.SetForegroundColour("#FFFFFF")

        puntuacion.SetFont(font2)
        puntuacion.SetBackgroundColour("#612773")
        puntuacion.SetForegroundColour("#FFFFFF")



    def background (self, event):
        dc = event.GetDC()
        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRegion(rect)
        dc.Clear()
        fondo = wx.Bitmap('assets/fin.png')
        dc.DrawBitmap(fondo, 0, 0)


class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, title='10 000', size=(533, 732), style=wx.DEFAULT_FRAME_STYLE & ~ (wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))
        self.SetIcon(wx.Icon('assets/icono.ico', wx.BITMAP_TYPE_ICO))
        panel = VentanaMain(self)
        exitGame = wx.Button(panel, label="Salir", pos=(150, 450), style=wx.BU_EXACTFIT, size=(200, 50))
        startGame = wx.Button(panel, label="Empezar Nueva Partida", pos=(150, 150), style=wx.BU_EXACTFIT, size=(200, 50))
        loadGame = wx.Button(panel, label="Cargar Partida", pos=(150, 250), style=wx.BU_EXACTFIT, size=(200, 50))
        opciones = wx.Button(panel, label="Opciones", pos=(150, 350), style=wx.BU_EXACTFIT, size=(200, 50))
        self.Center()
        self.Show()
        exitGame.Bind(wx.EVT_BUTTON, self.exit)
        startGame.Bind(wx.EVT_BUTTON, self.empezarJuego)
        loadGame.Bind(wx.EVT_BUTTON, self.cargar)

    def cargar(self, event):
        saves = open("saves.txt", "r")
        datos = saves.readlines()

        saves.close()



        game.limite = int(datos[1])
        if datos[0] == '0':
            game.player1.nombre = datos[2]
            game.player1.puntosTotales = int(datos[3])
            game.player2.nombre = datos[4]
            game.player2.puntosTotales = int(datos[5])
        else:
            game.player2.nombre = datos[2]
            game.player2.puntosTotales = int(datos[3])
            game.player1.nombre = datos[4]
            game.player1.puntosTotales = int(datos[5])
        app = wx.App(self)
        juego = Juego()
        app.MainLoop()
        self.Close()

    def exit(self, event):
        self.Close()

    def empezarJuego(self, event):
        self.Close()
        app = wx.App(self)
        elegir = Choose()

        app.MainLoop()
class Choose(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, title='10 000', size=(533, 732), style=wx.DEFAULT_FRAME_STYLE & ~ (wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))
        self.SetIcon(wx.Icon('assets/icono.ico', wx.BITMAP_TYPE_ICO))
        panel = VentanaChoose(self)
        self.Center()
        self.Show()
class Pvp(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, title='10 000', size=(533, 732), style=wx.DEFAULT_FRAME_STYLE & ~ (wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))
        self.SetIcon(wx.Icon('assets/icono.ico', wx.BITMAP_TYPE_ICO))
        panel = Jcj(self)
        self.Center()
        self.Show()
class Juego(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, title='10 000', size=(533, 732), style=wx.DEFAULT_FRAME_STYLE & ~ (wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))
        self.SetIcon(wx.Icon('assets/icono.ico', wx.BITMAP_TYPE_ICO))
        panel = Game(self)

        self.Center()
        self.Show()
class JuegoMaq(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, title='10 000', size=(533, 732), style=wx.DEFAULT_FRAME_STYLE & ~ (wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))
        self.SetIcon(wx.Icon('assets/icono.ico', wx.BITMAP_TYPE_ICO))
        panel = GameMaq(self)

        self.Center()
        self.Show()
class FinDelJuego(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, title='10 000', size=(868, 676), style=wx.DEFAULT_FRAME_STYLE & ~ (wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))
        self.SetIcon(wx.Icon('assets/icono.ico', wx.BITMAP_TYPE_ICO))
        panel = Final(self)
        self.Center()
        self.Show()

if __name__ == '__main__':
    app = wx.App(False)
    ventana = MainFrame()
    app.MainLoop()


