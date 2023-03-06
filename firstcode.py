import numpy as np
import json
THERESHOLD = 5 #TODO ask value
WINDOW = 3 #TODO ask value
def main():
    bedfile = (row for row in open("/home/user/D/BAMdata/proje/bedfilem.bed" ,"r")) #TODO I will use sampy 
    preseq = bedfile.readline()
    length = preseq[2] - preseq[1] # as I recognize seq lengths are same every where
    sonuc = open("sonuc.txt","w")
    ittirate = 0
    data_dic = {}#TODO will change to array
    chr, start, end = 0, 0, 0
    while True:
        
        seq = next(bedfile).split()
        chr1, start1, end1 = seq[0], int(seq[1]), int(seq[1])+length
        print(seq)
        for nucleotid in range(start1, end1+1):
            try:
                data_dic[nucleotid] += 1
            except KeyError:
                data_dic[nucleotid] = 1
        
        cleaning(start, start1, data_dic)
        peak_start, signal = peak_start(start1, data_dic)


        ittirate += 1

        if ittirate == 1000000000000:
            break
    
    for key, value in data_dic.items():
        sonuc.write(f"{key}:{value}\n")

def cleaning (start:int, start1:int, data_dic:dict): # clean passed  nucleotids 
    if start1 > start:
        for key in range(start, start1):
            if key in data_dic:
                del data_dic[key]
            else:
                continue
    else:
        pass

def peak_start(start1:int, data_dic:dict): #TODO will combine peak_start and end functions
    signal = None
    peak_start = None
    if data_dic[start1]  == THERESHOLD:
        for i in range(start1, start1+WINDOW-1):
            if data_dic[i] != data_dic[start1]:
                signal = False
            else:
                peak_start = start1
                signal = True
    return peak_start, signal

def peak_end(start1:int, data_dic:dict):
    signal = None
    nucleotid_pos = data_dic[start1]
    nucleotid = start1
    while nucleotid_pos >= THERESHOLD:
        nucleotid_pos = data_dic[nucleotid]
    else:
        signal = False



main()
      
