s = set()

l= [1, "a", "ali", 123]
s= set(l)

t = (2, "ayse", "b", 321)
s= set(t)


ali = "ata_bakma"
s= set(ali)
s 

l= ["geleceği", "yazanlar"]
s = set(l)
s 

s.add("ile")
s 

s.remove("ile") #eğer listede zaten yoksa hata verir
s 

s.discard("ile") #eğer listede zaten yoksa hata vermez

# =============================================================================
# diffirence() ile iki kümenin farkı
# intersection() iki kümenin kesişimi
# union() iki kümenin birleşimi
# symmetric.diffirence() ikisinde de olmayan
# =============================================================================

set1 = set([1,3,5])
set2 = set([1,2,3])

set1.difference(set2) #1de olup 2de olmayan
set1-set2

set2.difference(set1) #2de olup 1de olmayan
set2-set1

set1.symmetric_difference(set2) #ikisinde olmayan

set1.intersection(set2) #ikisinin kesişimi
set1 & set2

set1.union(set2) #birleşim

set1.intersection_update(set2) #set1 artık set1 ve set 2'nin birleşimi
set1 

set3 = set([7,8,9])
set4 = set([5,6,7,8,9,10])

set3.isdisjoint(set4) #iki kümenin kesişimi boş mu?
set3.issubset(set4) #set4 set3'ün alt kümesi mi?
set4.issuperset(set3) #set4 set3'ün ana kümesi mi?

