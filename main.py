# Define the BLOSUM62 matrix
BLOSUM62 = {
    'A': {'A': 4,  'B': -2, 'C': 0,  'D': -2, 'E': -1, 'F': -2, 'G': 0,  'H': -2, 'I': -1, 'K': -1, 'L': -1, 'M': -1, 'N': -2, 'P': -1, 'Q': -1, 'R': -1, 'S': 1,  'T': 0,  'V': 0,  'W': -3, 'X': -1, 'Y': -2, 'Z': -1},
    'B': {'A': -2, 'B': 6,  'C': -3, 'D': 6,  'E': 2,  'F': -3, 'G': -1, 'H': -1, 'I': -3, 'K': -1, 'L': -4, 'M': -3, 'N': 1,  'P': -1, 'Q': 0,  'R': -2, 'S': 0,  'T': -1, 'V': -3, 'W': -4, 'X': -1, 'Y': -3, 'Z': 2},
    'C': {'A': 0,  'B': -3, 'C': 9,  'D': -3, 'E': -4, 'F': -2, 'G': -3, 'H': -3, 'I': -1, 'K': -3, 'L': -1, 'M': -1, 'N': -3, 'P': -3, 'Q': -3, 'R': -3, 'S': -1, 'T': -1, 'V': -1, 'W': -2, 'X': -1, 'Y': -2, 'Z': -4},
    'D': {'A': -2, 'B': 6,  'C': -3, 'D': 6,  'E': 2,  'F': -3, 'G': -1, 'H': -1, 'I': -3, 'K': -1, 'L': -4, 'M': -3, 'N': 1,  'P': -1, 'Q': 0,  'R': -2, 'S': 0,  'T': -1, 'V': -3, 'W': -4, 'X': -1, 'Y': -3, 'Z': 2},
    'E': {'A': -1, 'B': 2,  'C': -4, 'D': 2,  'E': 5,  'F': -3, 'G': -2, 'H': 0,  'I': -3, 'K': 1,  'L': -3, 'M': -2, 'N': 0,  'P': -1, 'Q': 2,  'R': 0,  'S': 0,  'T': -1, 'V': -2, 'W': -3, 'X': -1, 'Y': -2, 'Z': 5},
    'F': {'A': -2, 'B': -3, 'C': -2, 'D': -3, 'E': -3, 'F': 6,  'G': -3, 'H': -1, 'I': 0,  'K': -3, 'L': 0,  'M': 0,  'N': -3, 'P': -4, 'Q': -3, 'R': -3, 'S': -2, 'T': -2, 'V': -1, 'W': 1,  'X': -1, 'Y': 3,  'Z': -3},
    'G': {'A': 0,  'B': -1, 'C': -3, 'D': -1, 'E': -2, 'F': -3, 'G': 6,  'H': -2, 'I': -4, 'K': -2, 'L': -4, 'M': -3, 'N': 0,  'P': -2, 'Q': -2, 'R': -2, 'S': 0,  'T': -2, 'V': -3, 'W': -2, 'X': -1, 'Y': -3, 'Z': -2},
    'H': {'A': -2, 'B': -1, 'C': -3, 'D': -1, 'E': 0,  'F': -1, 'G': -2, 'H': 8,  'I': -3, 'K': -1, 'L': -3, 'M': -2, 'N': 1,  'P': -2, 'Q': 0,  'R': 0,  'S': -1, 'T': -2, 'V': -3, 'W': -2, 'X': -1, 'Y': 2,  'Z': 0},
    'I': {'A': -1, 'B': -3, 'C': -1, 'D': -3, 'E': -3, 'F': 0,  'G': -4, 'H': -3, 'I': 4,  'K': -3, 'L': 2,  'M': 1,  'N': -3, 'P': -3, 'Q': -3, 'R': -3, 'S': -2, 'T': -1, 'V': 3,  'W': -3, 'X': -1, 'Y': -1, 'Z': -3},
    'K': {'A': -1, 'B': -1, 'C': -3, 'D': -1, 'E': 1,  'F': -3, 'G': -2, 'H': -1, 'I': -3, 'K': 5,  'L': -2, 'M': -1, 'N': 0,  'P': -1, 'Q': 1,  'R': 2,  'S': 0,  'T': -1, 'V': -2, 'W': -3, 'X': -1, 'Y': -2, 'Z': 1},
    'L': {'A': -1, 'B': -4, 'C': -1, 'D': -4, 'E': -3, 'F': 0,  'G': -4, 'H': -3, 'I': 2,  'K': -2, 'L': 4,  'M': 2,  'N': -3, 'P': -3, 'Q': -2, 'R': -2, 'S': -2, 'T': -1, 'V': 1,  'W': -2, 'X': -1, 'Y': -1, 'Z': -3},
    'M': {'A': -1, 'B': -3, 'C': -1, 'D': -3, 'E': -2, 'F': 0,  'G': -3, 'H': -2, 'I': 1,  'K': -1, 'L': 2,  'M': 5,  'N': -2, 'P': -2, 'Q': 0,  'R': -1, 'S': -1, 'T': -1, 'V': 1,  'W': -1, 'X': -1, 'Y': -1, 'Z': -2},
    'N': {'A': -2, 'B': 1,  'C': -3, 'D': 1,  'E': 0,  'F': -3, 'G': 0,  'H': 1,  'I': -3, 'K': 0,  'L': -3, 'M': -2, 'N': 6,  'P': -2, 'Q': 0,  'R': 0,  'S': 1,  'T': 0,  'V': -3, 'W': -4, 'X': -1, 'Y': -2, 'Z': 0},
    'P': {'A': -1, 'B': -1, 'C': -3, 'D': -1, 'E': -1, 'F': -4, 'G': -2, 'H': -2, 'I': -3, 'K': -1, 'L': -3, 'M': -2, 'N': -2, 'P': 7,  'Q': -1, 'R': -2, 'S': -1, 'T': -1, 'V': -2, 'W': -4, 'X': -1, 'Y': -3, 'Z': -1},
    'Q': {'A': -1, 'B': 0,  'C': -3, 'D': 0,  'E': 2,  'F': -3, 'G': -2, 'H': 0,  'I': -3, 'K': 1,  'L': -2, 'M': 0,  'N': 0,  'P': -1, 'Q': 5,  'R': 1,  'S': 0,  'T': -1, 'V': -2, 'W': -2, 'X': -1, 'Y': -1, 'Z': 2},
    'R': {'A': -1, 'B': -2, 'C': -3, 'D': -2, 'E': 0,  'F': -3, 'G': -2, 'H': 0,  'I': -3, 'K': 2,  'L': -2, 'M': -1, 'N': 0,  'P': -2, 'Q': 1,  'R': 5,  'S': -1, 'T': -1, 'V': -3, 'W': -3, 'X': -1, 'Y': -2, 'Z': 0},
    'S': {'A': 1,  'B': 0,  'C': -1, 'D': 0,  'E': 0,  'F': -2, 'G': 0,  'H': -1, 'I': -2, 'K': 0,  'L': -2, 'M': -1, 'N': 1,  'P': -1, 'Q': 0,  'R': -1, 'S': 4,  'T': 1,  'V': -2, 'W': -3, 'X': -1, 'Y': -2, 'Z': 0},
    'T': {'A': 0,  'B': -1, 'C': -1, 'D': -1, 'E': -1, 'F': -2, 'G': -2, 'H': -2, 'I': -1, 'K': -1, 'L': -1, 'M': -1, 'N': 0,  'P': -1, 'Q': -1, 'R': -1, 'S': 1,  'T': 5,  'V': 0,  'W': -2, 'X': -1, 'Y': -2, 'Z': -1},
    'V': {'A': 0,  'B': -3, 'C': -1, 'D': -3, 'E': -2, 'F': -1, 'G': -3, 'H': -3, 'I': 3,  'K': -2, 'L': 1,  'M': 1,  'N': -3, 'P': -2, 'Q': -2, 'R': -3, 'S': -2, 'T': 0,  'V': 4,  'W': -3, 'X': -1, 'Y': -1, 'Z': -2},
    'W': {'A': -3, 'B': -4, 'C': -2, 'D': -4, 'E': -3, 'F': 1,  'G': -2, 'H': -2, 'I': -3, 'K': -3, 'L': -2, 'M': -1, 'N': -4, 'P': -4, 'Q': -2, 'R': -3, 'S': -3, 'T': -2, 'V': -3, 'W': 11, 'X': -1, 'Y': 2,  'Z': -3},
    'X': {'A': -1, 'B': -1, 'C': -1, 'D': -1, 'E': -1, 'F': -1, 'G': -1, 'H': -1, 'I': -1, 'K': -1, 'L': -1, 'M': -1, 'N': -1, 'P': -1, 'Q': -1, 'R': -1, 'S': -1, 'T': -1, 'V': -1, 'W': -1, 'X': -1, 'Y': -1, 'Z': -1},
    'Y': {'A': -2, 'B': -3, 'C': -2, 'D': -3, 'E': -2, 'F': 3,  'G': -3, 'H': 2,  'I': -1, 'K': -2, 'L': -1, 'M': -1, 'N': -2, 'P': -3, 'Q': -1, 'R': -2, 'S': -2, 'T': -2, 'V': -1, 'W': 2,  'X': -1, 'Y': 7,  'Z': -2},
    'Z': {'A': -1, 'B': 2,  'C': -4, 'D': 2,  'E': 5,  'F': -3, 'G': -2, 'H': 0,  'I': -3, 'K': 1,  'L': -3, 'M': -2, 'N': 0,  'P': -1, 'Q': 2,  'R': 0,  'S': 0,  'T': -1, 'V': -2, 'W': -3, 'X': -1, 'Y': -2, 'Z': 5}
}
#BLOSUM matrix defined here to make it more runnable on every type of device and the program logic is also implemented on this


def print_alignment(a1, a2):
    match_line = ''.join('|' for _ in range(len(a1)))
    print(a1)
    print(match_line)  # showing the alignments and matches in a human readable way
    print(a2)
    print()

def traceback(i, j, aligned1, aligned2, alignments, score_matrix, traceback_matrix, seq1, seq2):
    if score_matrix[i][j] == 0:
        alignments.append((aligned1[::-1], aligned2[::-1]))    #tracing back to form the alignment recursively
        return
    for (pi, pj) in traceback_matrix[i][j]:
        if pi == i - 1 and pj == j - 1:
            traceback(pi, pj, aligned1 + seq1[i - 1], aligned2 + seq2[j - 1],
                      alignments, score_matrix, traceback_matrix, seq1, seq2)
        elif pi == i - 1 and pj == j:
            traceback(pi, pj, aligned1 + seq1[i - 1], aligned2 + '-',
                      alignments, score_matrix, traceback_matrix, seq1, seq2)
        elif pi == i and pj == j - 1:
            traceback(pi, pj, aligned1 + '-', aligned2 + seq2[j - 1],
                      alignments, score_matrix, traceback_matrix, seq1, seq2)



# Get score from matrix (with fallback for unknown characters)
def get_blosum_score(a, b):
    try:
        return BLOSUM62[a][b]          #this function will be used in blosum version of the application it takes the correct score from the blosum matrix.
    except KeyError:                   #in the cases that user chooses blosum option but includes a letter that does not belong to BLOSUM matrix we will assume a penalty of -4.
        return -4  # default penalty for unknown residues


def smith_waterman(seq1, seq2, match_score, mismatch_penalty, gap_penalty):
    seq1=seq1.upper().strip()                          #taking the sequences and adjusting them to correctly align later
    seq2=seq2.upper().strip()
    m, n = len(seq1), len(seq2)
    score_matrix = [[0]*(n+1) for _ in range(m+1)]                            #filling the matrix with zeros
    traceback_matrix = [[[] for _ in range(n+1)] for _ in range(m+1)]
    max_score = 0
    max_positions = []


    for i in range(1, m+1):
        for j in range(1, n+1):
            match = score_matrix[i-1][j-1] + (match_score if seq1[i-1] == seq2[j-1] else mismatch_penalty)
            delete = score_matrix[i-1][j] + gap_penalty
            insert = score_matrix[i][j-1] + gap_penalty              #using the algorithms logic we are setting values on score matrix
            score = max(0, match, delete, insert)
            score_matrix[i][j] = score

            if score == 0:
                continue
            if score == match:
                traceback_matrix[i][j].append((i-1, j-1))
            if score == delete:
                traceback_matrix[i][j].append((i-1, j))             #to traceback and store the alignment we have traceback matrix and here we are populating it
            if score == insert:
                traceback_matrix[i][j].append((i, j-1))
            if score > max_score:
                max_score = score
                max_positions = [(i, j)]
            elif score == max_score:
                max_positions.append((i, j))

    alignments = []
    for i, j in max_positions:
        traceback(i, j, '', '', alignments, score_matrix, traceback_matrix, seq1, seq2)

    for a1, a2 in alignments:
        print_alignment(a1, a2)


def smith_waterman_blosum62(seq1, seq2, gap_penalty):
    seq1 = seq1.upper().strip()
    seq2 = seq2.upper().strip()
    m, n = len(seq1), len(seq2)

    # Score matrix and traceback
    score_matrix = [[0] * (n + 1) for _ in range(m + 1)]
    traceback_matrix = [[[] for _ in range(n + 1)] for _ in range(m + 1)]

    max_score = 0
    max_positions = []

    # Fill matrices
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            match = score_matrix[i - 1][j - 1] + get_blosum_score(seq1[i - 1], seq2[j - 1])   #Main difference is this line from the first choice taking values from BLOSUM matrix
            delete = score_matrix[i - 1][j] + gap_penalty
            insert = score_matrix[i][j - 1] + gap_penalty
            score = max(0, match, delete, insert)
            score_matrix[i][j] = score

            # Store traceback
            if score == 0:
                continue
            if score == match:
                traceback_matrix[i][j].append((i - 1, j - 1))
            if score == delete:
                traceback_matrix[i][j].append((i - 1, j))
            if score == insert:
                traceback_matrix[i][j].append((i, j - 1))

            if score > max_score:
                max_score = score
                max_positions = [(i, j)]
            elif score == max_score:
                max_positions.append((i, j))


    alignments = []
    for i, j in max_positions:
        traceback(i, j, '', '', alignments, score_matrix, traceback_matrix, seq1, seq2)

    for a1, a2 in alignments:
        print_alignment(a1, a2)




print("Smith-Waterman Alignment Tool")
print("1 - Use simple scoring (match/mismatch/gap)")
print("2 - Use BLOSUM62 matrix ")

choice = input("Enter your choice (1 or 2): ")
seq1 = input("Enter first sequence: ")
seq2 = input("Enter second sequence: ")

if not (seq1.isalpha() and seq2.isalpha()):
    print("Invalid sequence! Sequences must contain only letters.")

else:
    if choice == "1":
        match_score = int(input("Enter match score: "))
        mismatch_penalty = int(input("Enter mismatch penalty: "))
        gap_penalty = int(input("Enter gap penalty: "))
        smith_waterman(seq1, seq2, match_score, mismatch_penalty, gap_penalty)
    elif choice == "2":
        gap_penalty = int(input("Enter gap penalty: "))
        smith_waterman_blosum62(seq1, seq2,gap_penalty)
    else:
        print("Invalid choice!")









