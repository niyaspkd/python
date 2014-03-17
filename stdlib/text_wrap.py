import textwrap
sample_text =''' 
The textwrap module can be used to format text for output in
situations where pretty-printing is desired. It offers'''
print textwrap.filll(sample_text,width=50)
