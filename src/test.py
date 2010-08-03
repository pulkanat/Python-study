import timeit
x=0
taken = timeit.repeat(stmt = 'x=5')
print taken
taken2 = timeit.repeat(stmt = '5')
print taken2
statement2 = "x=2;x=5;z=8"
taken4 = timeit.repeat(stmt = statement2)
print taken4
#iki ya da daha fazla degisken=sayi dedigimde sure 0.1'e cikiyor
statement = "x=4;y=x;z=y"
taken3 = timeit.repeat(stmt = statement)
print taken3
#en fazla bir kez sayi kullaninca ise 0.6 civarinda kaliyor

#taken = timeit.timeit(stmt = """x+=5""")
#print taken
#taken = timeit.timeit(stmt = """x+5""")
#print taken
