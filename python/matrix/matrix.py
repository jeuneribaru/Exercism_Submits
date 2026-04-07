class Matrix:
    def __init__(self, matrix_string):
        mat = [[]]
        index = 0
        select = 0
        for i in range(len(matrix_string)) :
            if matrix_string[i] == "\n":
                mat[index].append(matrix_string[select:i])
                select = i + 1
                mat.append([])
                index += 1            
            elif matrix_string[i] == " ":
                mat[index].append(matrix_string[select:i])
                select = i+1

        if select < len(matrix_string): #est ce qu'il reste un nombre à extraire ?
            mat[index].append(matrix_string[select:])
        self.mat = mat  

    def row(self, index):
        list = []
#        stri = ""
#        for num in self.mat[index-1] :
#            stri += str(num)
#           stri += ", "
#       return stri
#       return ", ".join(str(num) for num in self.mat[index-1]) #Dans le cas ou on veut return une str
        for num in self.mat[index-1] :
            list.append(int(num))
#        list.append(str(num) for num in self.mat[index-1])
        return list 

    def column(self, index):
        list = []
#       stri = ""
#       for ligne in self.mat :
#           stri += str(ligne[index-1])
#           stri += ", "
#        return ", ".join(str(ligne[index]) for ligne in self.mat) #Dans le cas ou on veut return une str
        for ligne in self.mat :
            list.append(int(ligne[index-1]))        
#        list.append(str(ligne[index]) for ligne in self.mat)
        return list 

Mat_Julien = Matrix(
    "1 2 3\n4 5 6\n7 8 9"
)
print(Mat_Julien.mat)
print(Mat_Julien.column(3))