def distance(strand_a, strand_b):
    count = 0
    if len(strand_a) != len(strand_b):
        raise ValueError('Strands must be of equal length.')
    for i in range(len(strand_a)) : 
        if strand_a[i] != strand_b[i]:
            count += 1 
            print(strand_a[i], "+ ", strand_b[i])
    return count

print(distance('GAGCCTACTAACGGGAT', 'CATCGTAATGACGGCCT'))