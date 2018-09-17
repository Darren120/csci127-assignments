#12: Darren Zou & Darren Liang
a = ["a","e","i","o","u"]

def pigLatin (word):
    for vowels in a:
        if word[0].lower() == vowels:
            return word + "ay"
        else:
            return word[1:] + word[0] + "ay"
            
        
    
print(pigLatin("apwple"))
print(pigLatin("cake"))
