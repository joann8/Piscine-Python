from ft_filter import ft_filter
from ft_map import ft_map
from ft_reduce import ft_reduce

x = [1, 2, 3, 4, 5]
ft_map(lambda dum: dum + 1, x)
# Output:
#<generator object ft_map at 0x7f708faab7b0> # The adress will be different

mylist = (list(ft_map(lambda t: t + 1, x)))
print(mylist)
# Output:[2, 3, 4, 5, 6]

# Example 2:
ft_filter(lambda dum: not (dum % 2), x)
# Output:
#<generator object ft_filter at 0x7f709c777d00> # The adress will be different

mylist2 = list(ft_filter(lambda dum: not (dum % 2), x))
print(mylist2)

# Output:[2, 4]

# Example 3:
lst = ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
mystr = ft_reduce(lambda u, v: u + v, lst)
print(mystr)
# Output:
#"Hello world"