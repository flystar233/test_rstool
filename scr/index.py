#!/usr/bin/env python
# coding=utf-8
import os
import click
from pathlib import Path

@click.command("index", help="create the index  of reference genome")
@click.option(
    "-r", "--reference", type=click.Path(exists=True), help="the file of reference genome"
    )
@click.option(
    "-o", "--outfile", default="work_index.sh", type=str, help="Output file ", show_default=True)
def index(reference,outfile):
	reference = os.path.abspath(reference)
	try:
		if not os.path.exists("02.Index"):
			os.mkdir('02.Index')
			os.chdir('02.Index')
		else: 
			print("the Folder of index already exists")
			os._exit()
		with open(outfile,'w') as IN:		
			#ref_stem = Path(reference).stem
			ref_name = Path(reference).name
			ref_softlink = 'ln -s {} ./{}'.format(reference,ref_name)
			if Path(bwa_path).name =='bwa-mem2':
				index = '{} index {} -p {}'.format(bwa_path,ref_name,ref_name)
			else:
				index = '{} index -a  bwtsw {} -p {}'.format(bwa_path,ref_name,ref_name)
			samtools_index = '{}  faidx {}'.format(samtools_path,ref_name)
			split = '{} Fatools split -InFa {}'.format(iTools_path,ref_name)
			#split_directory = '{}_cut'.format(ref_stem)

			scr= ref_softlink+"\n"+index+"\n"+samtools_index+"\n"+split
			IN.write(scr)

	except TypeError:
			print("File not found,please input existing file or use option --help")
	except FileNotFoundError :
			print("File not found,please input existing file or use option --help")
	else:
		print("successfully! The script has been saved in 02.Index/{}.".format(outfile))