from Bio.Seq import Seq

#Q1
DNA = Seq(str(input('TYPE DNA SEQUENCE:')))
mRNA = DNA.transcribe()
PTN = mRNA.translate()
print('mRNA - ', mRNA, 'PROTEIN - ', PTN, sep='\n')

#Q2
from Bio.Seq import Seq
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
refArquivoEntrada1 = open("C:/Users/BECKY/Documents/sequencias.fasta", "r")
mf = SeqIO.parse (refArquivoEntrada1, "fasta")
s = 0
for line in mf:
    s = s + 1
    rec = SeqRecord(line.seq, line.id)
    SeqIO.write(rec, 'C:/Users/BECKY/Documents/Sequences/Sequence-%d.fasta' %s, "fasta")

#Q3
import pandas
import pandas as pd
from Bio.Seq import Seq
from Bio import SeqIO
from Bio.Blast.Applications import NcbiblastpCommandline


sequence = "C:/Users/BECKY/Documents/sequenciaDesconhecida.fasta"
database = "C:/Users/BECKY/Documents/TriTrypDB-47_TcruziCLBrenerEsmeraldo-like_AnnotatedProteins.fasta"
myoutput = "C:/Users/BECKY/Documents/Out_blastp.txt"
blast_path = "C:/Users/BECKY/Prog II/blast-2.2.18+/bin/blastp"
blastp_commandline = NcbiblastpCommandline(cmd = blast_path, query = sequence, subject = database, evalue = 0.05, outfmt = 6, out = myoutput )
stdout, stderr = blastp_commandline()
blast_result = open(myoutput, "r")
results = pd.read_csv("C:/Users/BECKY/Documents/Out_blastp.txt", sep='\t', names=["qseqid","sseqid","pident","length","mismatch","gapopen","qstart","qend","sstart","send","evalue","bitscore"])
max_score = results.sort_values(["bitscore"])
print(max_score.iloc[[-1]])