doc1 = "A function is a group of statements that together perform a task. Every C program has at least one function, which is main(), and all the most trivial programs can define additional functions."
#doc2 = "My father spends a lot of time driving my sister around to dance practice."
#doc3 = "On the basis of hLDA and the PAM, several hierarchical topic models were proposed later."
#doc4 = "M name is vartika agrahari."
#doc5 = "Health experts say that Sugar is not good for your lifestyle."
# compile documents
doc_complete = [doc1]

import lda        #Importing calculation module
print(lda.f_lda(doc_complete))   #Calling function defined in add module.