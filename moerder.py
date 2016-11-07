import os
import subprocess
from random import shuffle
mystring='test'
mylist=[]
recover='n'

recover=input('gespeicherte Liste fortsetzen? (y/n)\n')
if recover=='y' or recover=='yes' or recover=='ja':
    try:
        with open('tmp','r') as tmp:
            for line in tmp:
                mylist.append(line.rstrip())
            
    except IOError:
        print('file couldn\'t be opened, perhaps you need to create it')
    

while mystring:
    mystring=input('Naechsten Namen eingeben. Zum zwischenspeichern "s" eingeben. (leer = fertig)\n')
    mylist.append(mystring)
    if mystring == 's':
        mylist.pop()
        with open('tmp','w') as tmp:
            for string in mylist:
                tmp.write(string+'\n')

#g=open('testnamen','r')
#for line in g:
#    mylist.append(line)
mylist.pop()
print('Liste der Mitspieler (zum ueberpruefen!): ',mylist)

with open('morderpy.tex','w') as f:
    f.write('\documentclass{article}\n')
    f.write('\parindent0mm\n')
    f.write('\\usepackage{color}\n')
    f.write('\pagestyle{empty}\n')
    f.write('\\begin{document}\n')
    f.write('\\flushright\n')
    f.write('\Huge\n')
    f.write('\\bf\n')
    
    mylist=mylist
    shuffle(mylist)
    mynewlist=mylist[1:]+mylist[:1]
    mycouple=list(zip(mylist,mynewlist))
    shuffle(mycouple)
    #print(mycouple)
        
    i=0
    vorne=''
    hinten=''
    for s in mycouple:
        if i%6==0 and not i==0:
            vorne=vorne[:-10]
            hinten=hinten[:-10]
            vorne+='\\newpage\n'
            hinten+='\\newpage\n'
            vorne+=hinten
            hinten=''
    
        vorne+='\\textcolor{green}{'+s[0]+'}'+'\\\[2.4cm]\n'
        hinten+=s[1]+'\\\[2.4cm]\n'
        i+=1
    
    hinten=hinten[:-10]
    vorne=vorne[:-10]
    vorne+='\\newpage\n'
    vorne+=hinten
    
    f.write(vorne)
    
        #if i == 1:
        #    print('Der ',i,'ste Moerder ',s[0],' hat ',s[1],' als Opfer.')
        #else:
        #    print('Der ',i,'te Moerder ',s[0],' hat ',s[1],' als Opfer.')
        #i+=1
        
    f.write('\end{document}')

FNULL = open(os.devnull,'w')
pdf=subprocess.call(['pdflatex','-interaction=batchmode','morderpy.tex'],stdout=FNULL,stderr=FNULL)
if pdf:
    print('pdf konnte nicht erstellt werden! Fehler beim TeXen')
else:
    print('Bleibt nurnoch die "moerderpy.pdf" doppelseitig zu drucken und in der Mitte zu falten!')
