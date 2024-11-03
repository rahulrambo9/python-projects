from prettytable import PrettyTable

my_table = PrettyTable()

my_table.add_column("Pokemon Names", ["Pikachu", "Charmender", "Meowto"])
my_table.add_column("Type", ["Electric", "Fire", "Spacex"])
my_table.align = "l"
print(my_table)