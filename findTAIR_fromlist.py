#!/usr/bin/env python2.7

import sys
from subprocess import *

mylist=sys.argv[1]
#mylist='/ebio/abt6_projects9/ath_1001G_image_pheno/experiment_218_droughtgwa/multivargwa/_dLDtopserial/m1d_polqua_LDtop_1_100_gwahits.txt'
#mylist='/ebio/abt6_projects9/ath_1001G_image_pheno/experiment_218_droughtgwa/multivargwa/_dLDtopserial/m1d_polqua_LDtop_1_100_gwahits.txttmplist'
#mylist='/home/moisesexpositoalonso/ebio_remote/abt6_projects9/ath_1001G_image_pheno/experiment_218_droughtgwa/multivargwa/_dLDtopserial/m1d_polqua_LDtop_1_100_gwahits.txt'


print "=========================================================================================="
print "REQUIREMENTS OF THIS SCRIPT"
print "(1) This script requires the module subprocess from python 2.7 "
print "(2) This expects an imput file (e.g. input.txt) with chromosome and position tab separated like:"
print "1   22241373"
print "1   12025127"
print "3   7227395"
print "(3) It also expects to have the TAIR annotations file one folder up"
print "                  "
print "HOW TO RUN:"
print "python findTAIR_fromlist.py input.txt"
print "                  "
print "OUTPUT:"
print "The output is one file named as the input plus a termination:"
print "_genelistTAIR this contains the gene name in which each SNP falls exactly."
print "==========================================================================================="

 

genelist="".join([mylist,"_genelistTAIR"])
genelistobject=open(genelist,"w")


tmplist=open(mylist,'r')
tmplist_use=[i.replace("\n",'').split('\t') for i in tmplist]
#print tmplist_use


newexcel=[]
for i in tmplist_use:
	if "SNP" in i:
		pass
	else:
		cmd="awk \'{ if ($1 == \"Chr%s\" && $3 ~ \"gene\"  && $4 < %d && $5 > %d && $9 !~ \"ID=Chr\")  print ($1,$3,$4,$5,$9) }\' TAIR10_GFF3_genes.gff.txt " %(str(i[0]),int(i[1]),int(i[1]))
		print(cmd)
		process = Popen(cmd, stdout=PIPE, stderr=PIPE ,shell=True)
		stdout = process.communicate()[0]
		newexcel.append([i[0],i[1], stdout.split(" ")[-1].split("Name=")[-1].replace("\n","").replace(";Index=1","")])


print newexcel

for i in newexcel:
	genelistobject.write(str("\t".join(i)+"\n"))
genelistobject.close()

print('end script parsed ATgenes')
