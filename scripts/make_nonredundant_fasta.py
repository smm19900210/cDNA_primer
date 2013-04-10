import os, sys
from Bio import SeqIO

def main(fasta_filename):
    seen_id = set()
    seen_seq = set()
    f = open(fasta_filename + '.nonredundant.fasta', 'w')
    for r in SeqIO.parse(open(fasta_filename), 'fasta'):
        s = str(r.seq)
        id = r.id
        if id in seen_id:
            print >> sys.stderr, "id: {0} already seen. skipping this one".format(id)
        elif s in seen_seq:
            print >> sys.stderr, "seq of {0} already seen. skipping this one".format(id)
        else:
            seen_id.add(id)
            seen_seq.add(s)
            f.write(">{0}\n{1}\n".format(id, s))
    f.close()
    print >> sys.stderr, "Nonredundant output written to", f.name

if __name__ == "__main__":
    main(sys.argv[1])

