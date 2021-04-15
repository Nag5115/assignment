f=open('word-char-count-descend.txt','w')
l1=map(lambda x:x+'\n', sorted(open('logfile-content.log', 'r').read().split(), key=len,reverse=True))
f.writelines(l1)
f.close()