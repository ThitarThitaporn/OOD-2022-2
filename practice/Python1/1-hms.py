print('*** Converting hh.mm.ss to seconds ***')
hh,mm,ss = list(map(int,input('Enter hh mm ss : ').split()))
if mm > 59 :
    print(f'mm({mm}) is invalid!')
elif mm < 0:
    print(f'mm({mm}) is invalid!')
else:
    if hh < 10:
        print(f'0{hh}',end=':')
    else:
        print(hh,end=':')
    
    if mm < 10:
        print(f'0{mm}',end=':')
    else:
        print(mm,end=':')
    
    if ss < 10:
        print(f'0{ss}',end=' = ')
    else:
        print(ss,end=' = ')
    total = hh*3600+mm*60+ss
    print(f'{total:,d} seconds')
    #print('{:,d} seconds'.format(total))
    
