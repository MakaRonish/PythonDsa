def add(n1,n2,n3)-> int:
    total=n1+n2+n3
    return total


def even_odd(num)->None:
    if num%2==0:
        print("even")
    else:
        print("odd")

x=add(9,29,99)
print(x)
even_odd(x)


def sentence_correction(Sentence:str,word_to_replace:str,word:str)->str:
    new_sentence=Sentence.replace(word_to_replace,word)
    return new_sentence

x=sentence_correction("i am ronish maakaju","ronish","Priya")
print(sentence_correction("i am ronish maakaju","ronish","Priya"))


