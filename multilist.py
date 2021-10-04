#===================================================================
#    Purpose:   Demonstrate Python programming multidimensional list
#===================================================================


# Initialize a multidimensional list
donors = list(); 'columns represent name, address, contact'
donors.append(list())
donors.append(list())
donors.append(list())


# Aquire first donor from user
donors[0].append(input('Name:'))
donors[0].append(input('Address:'))
donors[0].append(input('Contact:'))

# Aquire first donor from user
donors[1].append(input('Name:'))
donors[1].append(input('Address:'))
donors[1].append(input('Contact:'))

# Aquire first donor from user
donors[2].append(input('Name:'))
donors[2].append(input('Address:'))
donors[2].append(input('Contact:'))

# Loop through all donors and display
for i in range(3):
   for j in range(3):
      print(donors[i][j])
