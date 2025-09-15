def marichka_method(quantity_field):
   if not quantity_field or len(quantity_field) == 0:
       return []
   rows = len(quantity_field)
   cols = len(quantity_field[0])
   result = []
   for i in range(0, rows):
       for j in range(0, cols):
           if i % 2 == 0:
               result.append(quantity_field[i][j])
           else:
               result.append(quantity_field[i][cols - j - 1])
   return result