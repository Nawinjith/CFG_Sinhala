
import nltk
import codecs

load_grammar = nltk.data.load('file:grammar.cfg')
file_input = codecs.open('input.txt', 'r', 'utf-8-sig')
print("************A Context free grammar for Sinhala Language***********")

for sent in file_input:
        print("\nSentence: "+sent)
        sent_split = sent.split()
        rd_parser = nltk.RecursiveDescentParser(load_grammar)
        if(list(rd_parser.parse(sent_split))==[]):
                print("Error !! Could not generate parse tree:  The Sentence is Grammatically Incorrect")
        else:
                print("Parse tree: ")
                for tree_struc in rd_parser.parse(sent_split):
                        s = str(tree_struc)
                        print (s)
                        
        print("******************************************************************")


