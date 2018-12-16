#!/usr/bin/env python2.7

import sys
from subprocess import *
import re

mylist=sys.argv[1]

# Examples
#mylist='/ebio/abt6_projects9/ath_1001G_image_pheno/experiment_218_droughtgwa/multivargwa/_dLDtopserial/m1d_polqua_LDtop_1_100_gwahits.txttmplist'
#mylist='/ebio/abt6_projects9/ath_1001G_image_pheno/experiment_218_droughtgwa/multivargwa/_dLDtopserial/m1d_polqua_LDtop_1_100_gwahits.txt'
# mylist='/home/moisesexpositoalonso/ebio_remote/abt6_projects9/ath_1001G_image_pheno/experiment_218_droughtgwa/multivargwa/_dLDtopserial/m1d_polqua_LDtop_1_100_gwahits.txt'



print "=========================================================================================="
print "REQUIREMENTS OF THIS SCRIPT"
print "(1) This script requires the modules subprocess and re from python 2.7 "
print "(2) This expects an imput file (e.g. input.txt) with chromosome and position tab separated like:"
print "1   22241373"
print "1   12025127"
print "3   7227395"
print "(3) It also expects to have the snpeff file from the 1001 genomes one folder up"
print "                  "
print "HOW TO RUN:"
print "python findSNPeff_fromlist.py input.txt"
print "                  "
print "OUTPUTS:"
print "The output are three files named as the input plus a termination:"
print "_genearound file is the raw row from SNPeff"
print "_around_protein_name tries to find wheter there is a common protein name in the SNPeff row"
print "_around_atname tries to find the official ATname identifier. Then you can search more in www.arabidopsis.org/tools/bulk/genes/index.jsp"
print "==========================================================================================="



print "finding hit genes from annotated genome matrix ... "
out="".join([mylist,"_genearound"])
cmd="awk 'NR==FNR{a[$1$2];next}($1$2) in a {print $1,$2,$8}' %s /ebio/abt6_projects9/ath_1001g_foreverybody/1001genomes_snp-short-indel_only_ACGTN_v3.1.vcf.snpeff > %s" %(mylist,out) 
call(cmd,shell=True)
print cmd
genelistparse=open(out,'r')


print "parsing the annotation information and print output ..."
genelist_parsed="_".join([out,"_around_protein_name"])
parsedname=open(genelist_parsed,"w")

genelist_parsed="_".join([out,"_around_atname"])
atname=open(genelist_parsed,"w")


for i in genelistparse:
# 	# print i
	splitted=i.split()
	# print splitted
	chrpos="_".join(splitted[0:2])

	toparse=splitted[2].split("|")
	print toparse
	if "protein_coding"  in toparse:
            ind=toparse.index("protein_coding")
	    	# print i[ind-1]
            # parsedgenenames.append("\t".join([chrpos,toparse[ind-1])]) 
            parsedname.write(str("\t".join([chrpos,toparse[ind-1]])+"\n"  ))
            print toparse
        for z in toparse:
        	if z[0:2] =="AT":
	        	atname.write(str("\t".join([chrpos,z])+"\n" ))

genelistparse.close()
parsedname.close()
atname.close()

print "...end script" 





