cifra = int(input("Introdu cifra factoriala: "))
factorialul = 1

while cifra > 0:
    factorialul *= cifra
    cifra -= 1

print(f"Factorialul este: {factorialul}")