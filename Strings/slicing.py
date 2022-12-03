my_name = 'Aditya Kumar Tripathi'
fi_name = my_name[0:6]
mi_name = my_name[7:12]
la_name = my_name[13:]
print(fi_name,mi_name,la_name)

revname = my_name[::-1]
print(revname)

even_name = my_name[::2]
print(even_name)
odd_name = my_name[1::2]
print(odd_name)

message = '''A data scientist’s duties can include developing strategies for analyzing data, preparing data for analysis, exploring, analyzing, and visualizing data, building models with data using programming languages, such as Python and R, and deploying models into applications.

The data scientist doesn’t work solo. In fact, the most effective data science is done in teams. In addition to a data scientist, this team might include a business analyst who defines the problem, a data engineer who prepares the data and how it is accessed, an IT architect who oversees the underlying processes and infrastructure, and an application developer who deploys the models or outputs of the analysis into applications and products.'''

print("Length of message is ," ,len(message))
# First 100 character
print(message[:100])
# last 200 character
print(message[-200:])
# every 10th character
print(message[::10])
# all data expect first 100 and last 100 character
print(message[100:-100])