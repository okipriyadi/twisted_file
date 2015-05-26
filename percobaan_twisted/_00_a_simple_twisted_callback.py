"""
#perhatikan bahwa fungsi hello() dipanggil setelah reactor.run(). 
Artinya fungsi ini dipanggil dari dalam reactor itu sendiri
caranya dengan memanggil reactor method yang bernama callWhenrunning yang mereferensikan
ke fungsi yang kita mau, dan tentu kita harus melakukannya sebelum reactor.run() dijalankan
kita menyebutnya dengan istilah CALLBACK untuk menjelaskan referensi ke fungsi hello()
sebaiknya kita menghindari penggunaan blocking I?O seperti os.system atau juga yg bisa terblock seperti penggunaan pipe
"""

def hello(): 
    print "hello from the reactor loop"
    print "Lately I fell like I'm stuck "
    
from twisted.internet import reactor

reactor.callWhenRunning(hello)#ini yang disebut callback

print "start the reactor"
reactor.run()

"""
you still have to kill the program yourself, 
since it gets stuck again after printing those line
"""