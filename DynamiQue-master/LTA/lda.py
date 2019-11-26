
# doc2, doc3, doc4, doc5]

from nltk.corpus import stopwords 
from nltk.stem.wordnet import WordNetLemmatizer
import string



def f_lda(doc_complete):
    stop = set(stopwords.words('english'))
    exclude = set(string.punctuation) 
    lemma = WordNetLemmatizer()
    def clean(doc):
        stop_free = " ".join([i for i in doc.lower().split() if i not in stop])
        punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
        normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
        return normalized

    doc_clean = [clean(doc).split() for doc in doc_complete]
    # Importing Gensim
    import warnings
    warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
    import gensim
    from gensim import corpora
    # Creating the term dictionary of our courpus, where every unique term is assigned an index. 
    dictionary = corpora.Dictionary(doc_clean)
    # Converting list of documents (corpus) into Document Term Matrix using dictionary prepared above.
    doc_term_matrix = [dictionary.doc2bow(doc) for doc in doc_clean]
    # Creating the object for LDA model using gensim library
    Lda = gensim.models.ldamodel.LdaModel
    # Running and Trainign LDA model on the document term matrix.
    ldamodel = Lda(doc_term_matrix, num_topics=2, id2word = dictionary, passes=50)
    
    new_str = ldamodel.print_topics(num_topics = 2, num_words=30)
    print(new_str)

    # print("NUMBER OF TOPICS : ")
    # print(ldamodel.num_topics)0
    # for t in range(ldamodel.num_topics):
    #     topk = ldamodel.show_topic(t,29)
    #     print("list of topics -----------------")
    #     print(topk)


    var_word = ""

    for t in range(ldamodel.num_topics):
        topk = ldamodel.show_topic(t,2)
        print("topic:")
        print(topk)
        t_word = [w for w,_ in topk]
        print("t_word:")
        print(t_word)
        
    return t_word
        