seats = [3,1,5] 
students = [2,7,4]

seats.sort()
students.sort()
print(sum(abs(seat - student) for seat, student in zip(seats, students)))

