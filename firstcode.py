import numpy as np
import json
THERESHOLD = 5 #TODO ask value
WINDOW = 3 #TODO ask value
def main():
    preopen = open("/home/user/D/BAMdata/proje/bedfilem.bed" ,"r") # This is just for count length to runout from unwanted calculates in program
    preseq = preopen.readline().split()
    preopen.close()
    length = int(preseq[2]) - int(preseq[1]) # as I recognize seq lengths are same every where
    bedfile = (row for row in open("/home/user/D/BAMdata/proje/bedfilem.bed" ,"r")) #TODO I will use sampy 
    output = open("output.txt","w")
    ittirate = 0
    data_dic = {}#TODO will change to array
    chr, start, end = 0, 0, 0
    signal = False
    peak_start_pos, peak_end_pos = 0, 0
    while True:        
        seq = next(bedfile).split()# TODO it will be a function
        chr1, start1, end1 = seq[0], int(seq[1]), int(seq[1])+length
        print(seq)
        for nucleotid in range(start1, end1+1):
            try:
                data_dic[nucleotid] += 1
            except KeyError:
                data_dic[nucleotid] = 1
        
        
        
        if signal == False:
            peak_start_pos, signal = peak_start(start1, data_dic)
        else:
            signal, peak_end_pos = peak_end(start,start1, data_dic)
            if signal == False:
                peak_bed = f"{chr}\t{peak_start_pos}\t{peak_end_pos}\n"
                output.write(peak_bed)
        start, end = start1, end1
        if ittirate != 0:
            cleaning(start, start1, data_dic)


        ittirate += 1

        if ittirate == 1000:
            break
    


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
    signal = False
    peak_start = None
    if data_dic[start1]  == THERESHOLD:
        for i in range(start1, start1+WINDOW-1):# if just one of pos is 5 it would not be peak
            if data_dic[i] != data_dic[start1]:
                signal = False
            else:
                peak_start = start1
                signal = True
    return peak_start, signal

def peak_end(pre_start:int,start1:int, data_dic:dict):
    signal = True
    nucleotid = data_dic[start1]
    nucleotid_pos = start1
    end = None

    if nucleotid >= THERESHOLD:
        signal = True
    else:
        signal = False
        for nucleotid in range(pre_start,start1):
            if data_dic[nucleotid] < THERESHOLD:
                end = data_dic[nucleotid]

    return signal, end
main()
      
