# indexing = accessing elements of a sequencce using [] (indexing operator)
#   This is the indexing operator:         [start : end : step] the end is exclusive doesn't contain the 4th

credit_number = "1234-5678-9012-3456"

#print(credit_number[3])

#Now if we want to access the first 4 places of the string then:
#print(credit_number[0:4])

#from index 5 to 8 as 9 is exclusive
#print(credit_number[5:9])

#index 5 dekhi last ko sabbai print garcha
# Similarly, [:5] cha vane python le automatically bujcha ki 0 dekhi 5 samma vanera
#print(credit_number[5:])

# negative index: last character of a string=-1, ani 2nd last = -2 and so on
#print(credit_number[-1])

#step: prints every 2nd character of the string
print(credit_number[::2])