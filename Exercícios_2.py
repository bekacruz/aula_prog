#Q1
seq = str(input('sequência de nucleotídeos:'))
c = 0
for x in seq:
    if str(x).upper() == "G" or str(x).upper() == "C" :
        c = c+1
print ('total= ', len(seq), 'GC=', c, ((c/len(seq))*100))

#Q2
seq = str(input('sequencia de AA:')).upper()
t = len(seq)
AA_cont = { 'A' : 0, 'C' : 0, 'D' : 0, 'E' : 0, 'F' : 0, 'G' : 0, 'H' : 0, 'I' : 0, 'K' : 0, 'L' : 0, 'M' : 0,
            'N' : 0, 'P' : 0, 'Q' : 0, 'R' : 0, 'S' : 0, 'T' : 0, 'V' : 0, 'W' : 0, 'Y' : 0}
for x in seq:
    AA_cont[x] += 1
for key, value in AA_cont.items():
    if value != 0:
        pcnt = float((value/t)*100)
        print (key, pcnt)

#Q3
seq_a = str(input('Sequência 1:'))
seq_b = str(input('Sequência 2:'))

seq = seq_a + seq_b
rev_seq = seq[::-1]
comp_rev = ''
for x in rev_seq:
    if x.upper() == 'A':
        comp_rev += 'T'
    if x.upper() == 'T':
        comp_rev += 'A'
    if x.upper() == 'G':
        comp_rev += 'C'
    if x.upper() == 'C':
        comp_rev += 'G'
print(comp_rev)

#Q4
RNA = str(input('sequência de RNA:'))
coord_1 = str(input('coordenada 1:'))
coord_2 = str(input('coordenada 2:'))
exon_1 = RNA[int(coord_1[0])-1:int(coord_1[-1])-1]
exon_2 = RNA[int(coord_2[0])-1:int(coord_2[-1])-1]
mRNA = exon_1 + exon_2
print(mRNA)
