#!/usr/bin/python
import time
import sys
# YOUR FUNCTIONS GO HERE -------------------------------------
# 1. Populate the scoring matrix and the backtracking matrix

# ------------------------------------------------------------

def calculateMatrices(seq1, seq2):
    s = [[0]*(len(seq1) + 1) for _ in range(len(seq2) + 1)]
    b = [['-']*(len(seq1) + 1) for _ in range(len(seq2) + 1)]
    for i in range(0, len(s)):
        newI = -2 * i
        seq2Acc = i - 1
        for j in range(0, len(s[i])):
            if i == j == 0:
                continue
            elif j == 0:
                s[i][j] = newI
                b[i][j] = 'U'
            elif i == 0:
                s[i][j] = -2 * j
                b[i][j] = 'L'
            else:
                c = -3
                seq1Acc = j - 1
                if seq1[seq1Acc] == seq2[seq2Acc]:
                    if seq1[seq1Acc] == 'A':
                        c = 4
                    elif seq1[seq1Acc] == 'C':
                        c = 3
                    elif seq1[seq1Acc] == 'G':
                        c = 2
                    elif seq1[seq1Acc] == 'T':
                        c = 1
                largest = c + s[seq2Acc][seq1Acc]
                b[i][j] = 'D'
                nextR = s[seq2Acc][j] - 2
                if nextR > largest:
                    largest = nextR
                    b[i][j] = 'U'
                nextR = s[i][seq1Acc] - 2
                if nextR > largest:
                    largest = nextR
                    b[i][j] = 'L'
                s[i][j] = largest
    i = len(seq2)
    j = len(seq1)
    bestScore = s[i][j]
    alSeq1 = ''
    alSeq2 = ''
    while(not(i == j == 0)):
        v = b[i][j]
        if v == 'L':
            alSeq1 = seq1[j - 1] + alSeq1
            alSeq2 = '-' + alSeq2
            j -= 1
        elif v == 'U':
            alSeq2 = seq2[i - 1] + alSeq2
            alSeq1 = '-' + alSeq1
            i -= 1
        elif v == 'D':
            alSeq1 = seq1[j - 1] + alSeq1
            alSeq2 = seq2[i - 1] + alSeq2
            i -= 1
            j -= 1
    response = {'alignment':[alSeq1, alSeq2], 'bestScore':bestScore}
    return response


# DO NOT EDIT ------------------------------------------------
# Given an alignment, which is two strings, display it

def displayAlignment(alignment):
    string1 = alignment[0]
    string2 = alignment[1]
    string3 = ''
    for i in range(min(len(string1),len(string2))):
        if string1[i]==string2[i]:
            string3=string3+"|"
        else:
            string3=string3+" "
    print('Alignment ')
    print('String1: '+string1)
    print('         '+string3)
    print('String2: '+string2+'\n\n')

# ------------------------------------------------------------


# DO NOT EDIT ------------------------------------------------
# This opens the files, loads the sequences and starts the timer
file1 = open(sys.argv[1], 'r')
seq1=file1.read()
file1.close()
file2 = open(sys.argv[2], 'r')
seq2=file2.read()
file2.close()
start = time.time()
#-------------------------------------------------------------
# YOUR CODE GOES HERE ----------------------------------------
# The sequences are contained in the variables seq1 and seq2 from the code above.
# Intialise the scoring matrix and backtracking matrix and call the function to populate them
# Use the backtracking matrix to find the optimal alignment 
# To work with the printing functions below the best alignment should be called best_alignment and its score should be called best_score.
result = calculateMatrices(seq1, seq2)
best_alignment = result.get('alignment')
best_score = result.get('bestScore')
#-------------------------------------------------------------
# DO NOT EDIT (unless you want to turn off displaying alignments for large sequences)------------------
# This calculates the time taken and will print out useful information 
stop = time.time()
time_taken=stop-start

# Print out the best
print('Time taken: '+str(time_taken))
print('Best (score '+str(best_score)+'):')
displayAlignment(best_alignment)
#-------------------------------------------------------------
