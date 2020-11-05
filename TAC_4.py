from Bio.Seq import Seq
from Bio import SeqIO
import re

def contando_motivos(sqnc, mtv):
    gene = str(line.id)
    mc = sqnc.count(mtv)
    if mc != 0:
        print("Identificador:",gene," Motivo:",mtv," Contagem:", mc, sep='\n')
mtv = str(input("Digite sua sequência de DNA ou AA: ")).upper()
if re.search('^[ACGT]+$', mtv):
    print("Sequência de DNA identificada")
    refArquivoEntrada1 = open("C:/Users/BECKY/Documents/TriTrypDB-47_TcruziCLBrenerEsmeraldo-like_AnnotatedCDSs.fasta", "r")
    mf = SeqIO.parse(refArquivoEntrada1, "fasta")
    for line in mf:
        sqnc = str(line.seq)
        contando_motivos(sqnc,mtv)
else:
    print("Sequência de AA identificada")
    refArquivoEntrada2 = open("C:/Users/BECKY/Documents/TriTrypDB-47_TcruziCLBrenerEsmeraldo-like_AnnotatedProteins.fasta", "r")
    mf = SeqIO.parse(refArquivoEntrada2, "fasta")
    for line in mf:
        sqnc = str(line.seq)
        contando_motivos(sqnc,mtv)
