#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 12:53:17 2017

@author: ohm
"""
from datetime import datetime
import argparse
from tempfile import mkstemp
from shutil import move
from os import fdopen, remove
#import os
#import subprocess


def main(args):
    datestring = datetime.strftime(datetime.now(), '%d-%m-%Y')
    entryfname = 'entry_' + datestring + '.tex'

    print 'texmaker days/'+entryfname+'&'
#    print args

    content = r"""\subsection{"""+datestring+r"""}
    \begin{bullets}
    \item Dear diary..
    \end{bullets}
    """
    with open('days/'+entryfname,'w') as f:
        f.write(content%args.__dict__)
        
    replace('diary.tex','%lastentryline%',entryfname)
    print 'pdflatex diary.tex'
    return 0



def replace(file_path, pattern, subst):
    #Create temp file
    fh, abs_path = mkstemp()
    with fdopen(fh,'w') as new_file:
        with open(file_path) as old_file:
            for line in old_file:
                new_file.write(line.replace(pattern, '\include{days/'+subst[:-4]+'}'+'\n'+pattern))
    #Remove original file
    remove(file_path)
    #Move new file
    move(abs_path, file_path)

#cmd = ['pdflatex', '-interaction', 'nonstopmode', 'cover.tex']
#proc = subprocess.Popen(cmd)
#proc.communicate()

#retcode = proc.returncode
#if not retcode == 0:
#    os.unlink('cover.pdf')
#    raise ValueError('Error {} executing command: {}'.format(retcode, ' '.join(cmd)))

#os.unlink(entryfname)
#os.unlink('cover.log')

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--month')
    parser.add_argument('-t', '--title')
    parser.add_argument('-n', '--name',)
    parser.add_argument('-s', '--school', default='My U')

    args = parser.parse_args()
    main(args)
