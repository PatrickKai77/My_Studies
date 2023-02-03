n = input("Qual número deseja saber ser multiplo de 10: ")
n=int(n)
r=n % 10
if r == 0:
    print("este número é multiplo")
else:
    print("Este não")