from PyQt5.QtCore import QObject,pyqtSignal

class QtypeSignal(QObject):
    sendmsg = pyqtSignal(object)
    def __init__(self):
        super(QtypeSignal, self).__init__()
    
    def run(self):
        self.sendmsg.emit('Hello Pyqt5')

class QtypeSlt(QObject):
    def __init__(self):
        super(QtypeSlt, self).__init__()
    
    def get(self,msg):
        print("Qslot get msg =>" + msg)

if __name__ == '__main__':
    signal = QtypeSignal()
    slot = QtypeSlt()
    print('binding signal to slot')
    signal.sendmsg.connect(slot.get)
    signal.run()

    print("disconnect the binding")
    signal.sendmsg.disconnect(slot.get)
    signal.run()  