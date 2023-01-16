import hackerforms as hf

a = hf.read_number("a")
b = hf.read_number("b")
ans = hf.read_dropdown("c")
sum = a + b
hf.display(sum)
hf.display(ans)