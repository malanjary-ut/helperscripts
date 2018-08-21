#!/usr/bin/python
import glob, os
import argparse

def writesummary(inpath,outname,cutoff):
    networkfiles = [x for x in glob.glob("*/*network*")]
    attrfiles = [x for x in glob.glob("*/Network_Annotations_All_*")]
    try:
        cutoffs = [float(x.strip()) for x in cutoff.split("-")[:2]]
    except ValueError:
        print "Invalid cutoff values setting to default (0-1.0)"
        cutoffs = [0.0,1.0]
    #Concatenate list of files printing headers once
    def fileconcat(files,out,cut1=None,cut2=None):
        with open(out,"w") as ofil:
            header = ""
            for fname in files:
                with open(fname,"r") as fil:
                    if not header:
                        header = fil.next()
                        ofil.write(header)
                    else:
                        header = fil.next()
                    for i,line in enumerate(fil):
                        if cut1:
                            try:
                                dist = float(line.split()[2])
                                if dist >= cut1 and dist <= cut2:
                                    ofile.write(line)
                            except ValueError:
                                print "Warning could not parse distance value, line %s file %s"%(i,fname)
                        else:
                            ofil.write(line)
    fileconcat(networkfiles,outname+".network.%s.tsv"%cutoff)
    fileconcat(attrfiles,outname+".annotations.tsv")
    print "Combined network and annotation files saved: %s.network.%s.tsv, %s.annotations.tsv"%(outname,cutoff,outname)

# Commandline Execution
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="""Collect bigscape network edges and node annotations into summary files""")
    parser.add_argument("-i","--input", help="Location of 'networks_all' folder (default=current folder)", default=".")
    parser.add_argument("-o", "--output", help="Location and prefix for summary output (default= current folder / summary)",default="summary")
    parser.add_argument("-c", "--cutoff", help="Specify cutoff range default = all (0-1.0)",default="0-1.0")
    args = parser.parse_args()
    writesummary(args.input, args.output, args.cutoff)