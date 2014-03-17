import difflib
d=difflib.SequenceMatcher(None,'abcd','dcb')
print d.ratio()

