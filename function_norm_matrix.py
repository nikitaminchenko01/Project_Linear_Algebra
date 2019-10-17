def norm_matrix(elements):
    norm = 0
    sum_row = []
    try:
        for row in elements:
            sum = 0
            for element in row:
                float(element)
                sum += element
            sum_row.append(sum)
        norm = max(sum_row)
    except:
        raise ValueError('Incorrect elements')
    else:
        return norm

