"""This code is comparing the characters of two strings, string1 and string2, one by one, and counting the number of mismatches."""



string1= "GAGTCGACATGGAGGTCCCACCAGCAATTTGGTGAGATTCCTAATACAATTGGGCGTGGCATATACGGATCCCAATCGTAACGACCAGACTCTCCTGCTGATTACCTGAGTTCATGCTGTTAATGCGAGATCTGGAGAGACCTCCCGTTTTTCCACATTAGACTGATCCAGAGCATCTAATTATGCTTGCGGCTGCATGCCTGGCATGTCATGCCGGGGACGCCCAAGTGGCCGATACACGTAGTTGACAAAGTGGCCTTTCAGAACTTGGATTTGTTAAAGTCTGTTGAGGAAACTGCCAGGCCGCAGGGTTTTCGGTGAAGTTCCTACTCACGGCAGTCTTGTCCCTTCCGGCACGGGACCATACCGTAGTTGATCGACTCTTCACCCTAATTCCTAATGTATATTAAAGGGATGGGATAACGATACCAGCCACAGCCCGGGTCCAGAACCACCCCGCCGATTCATTCCAGTACTCACTCGGCAGGTTTTCCCCCTATCGAGTAAGGGACGGGCCCTATCTCAATCTACCGCAGGAGATGGATTAGGAAAAGTACTGGCTGAGGATATCATAATGGACCGAGCCCGATTCGCGAAGATCGCTCAGAGCGGAGGTCAACAGACTGGTCTGGCACAGATATCCGGTGCGGCTGATATTAGCTCTACCAAAACATGTGCTTTATTATGCGGAAAGCCGTGTGCCGAGACGGGGACAGGTCGGATGGAGATTGGCGGTGGCCTGCAACCTCTGACAAAGAACCTTTGCTCCGCATATGAAGTGCGTTATCAGGTTGCCTTGCGTGTTGGGCTATGGGAAGAGTGCAAGTGCAAAGGACGCACTCCACGGCATGGTCAATTGTTGCGCAAGGGCACTAATGCGCCTGGCTAGTCAGAAACGTGAACGGCCTTTGTGC"
string2= "GAGTAAACCTCAACGACTCACTTGCGATTTAGAAACAACTCTAAACCACCCCGGAGTGTAAGACTCGGATCCAGTTGAGTCCCACGAGATACTGTTACAGATTATGTTAGTTCCATTAGTGCAGATGCGATCTGACGACGCCTGGCGGGGTTCAGCCTTGGCCAGGTCCATGTGACATTAACATGAGTGCGGCTGCACGGCTGCGTCCTCAAACCGGCGTTGTCCAAGGGTACGCTCAACCCAATAGGGAATATAGCCTTATTAATAATGGTGTTGATAAAGTCGGAAGAGACAAGTCCATTGACAGCGAGATTTTCTTCAAGCCCACAGTTACGAAGGTACTCCATCCTACTCCTAGGCAGACTATCTTAGTGCCTAGACCCTTCTCGTAAGTTCCCAATTTGTCTTCGGTGTATGGGCTCAAGATCTCCGGTAAAGGCCCAGACGGAGTCACGATCGCTGCTGCATCCAACTAAACACGCAGTTTGGGAACACAAGTATAAATAGCGGGCGGGGACGACATCCCTCTGCCGAGGGAGAAGAATGCCAATACGGATCTGGTTAGTTTATGTTGACGGAGCGACTACAGCTCAGGAAGTTTGTACGTAGCGGACCTAATCGTCCTATTCTTGCGAGAAACTGTCCTAAGAGAGATACATCCGTGGCCAAAAACTGCCCGTTGTCATACTGGAAGCTGACTCGCGAACCCGGGAATGGTGCTATCGAAAAATACGGCGCCAGCCGACCTCTCACAAAATCCCCTTGAAGCCTCTCTAATTTGTATTACGAGGATGCTAAGGGACTTTACCTTAGGAACCAGACCAAGTGCAAAGTTCGCGGTCTTACGGCAGAGCAGAAGTCTAGCAATCACCCCGAGACTGTTATCTCTTCTTTACCATAGACATTTTTTGTGT"

mismatches= 0
# iterate over each index of the strings
for i in range(len(string1)):
    # compare the characters at the current index
    if string1[i] != string2[i]:
        mismatches += 1

# print the number of mismatches
print(f"There are {mismatches} mismatches between the strings.")