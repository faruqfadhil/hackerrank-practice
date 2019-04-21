#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    kolom_index = 0
    baris_index = 0
    pola_jam = 3
    cek_baris = True
    cek_kolom = True
    skor_sementara = 0
    hasil_penjumlahan_setiap_pola = 0
    while(cek_baris==True):
        cek_kolom = True
        kolom_index = 0
        while(cek_kolom == True):
            hasil_penjumlahan_setiap_pola = 0
            # proses pengambilan pola jam pasir
            for baris in range(0,pola_jam):
                # print(" ",end=' ')
                for kolom in range(0,pola_jam):
                    if(baris == 1):
                        if(kolom==1):
                            hasil_penjumlahan_setiap_pola += arr[baris_index+baris][kolom_index+kolom]
                        #     print(arr[baris_index+baris][kolom_index+kolom],end= '')
                        # else:
                        #     print(" ")
                    else:
                        hasil_penjumlahan_setiap_pola += arr[baris_index+baris][kolom_index+kolom]
                        # print(arr[baris_index+baris][kolom_index+kolom],end= '')
                # print("\n")
            # end
            # print("hasil penjumlahan = "+str(hasil_penjumlahan_setiap_pola))
            # print("skor = "+str(skor_sementara))
            if(hasil_penjumlahan_setiap_pola < 0 ):
                if(kolom_index == 0 and baris_index == 0):
                    # inisialisasi ulang
                    skor_sementara = hasil_penjumlahan_setiap_pola
                else:
                    # buat minus
                    convert_hasil = abs(hasil_penjumlahan_setiap_pola)
                    convert_skor = abs(skor_sementara)
                    if(skor_sementara < 0):
                        if(convert_hasil < convert_skor):
                            skor_sementara = hasil_penjumlahan_setiap_pola
                    else:
                        if(hasil_penjumlahan_setiap_pola > skor_sementara):
                            skor_sementara = hasil_penjumlahan_setiap_pola
            else:
                if(hasil_penjumlahan_setiap_pola > skor_sementara):
                    skor_sementara = hasil_penjumlahan_setiap_pola
            # elif()
            # print("skor setelah proses = "+str(skor_sementara))
            if(kolom_index+2 < len(arr)-1):
                kolom_index+=1
            else:
                cek_kolom = False
        if(baris_index+2 < len(arr)-1):
            baris_index+=1
        else:
            cek_baris = False

    return skor_sementara

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
