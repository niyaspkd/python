import re
adress=re.compile('[/w/d.+-]+@([/w/d.]+\.)+(com|org|edu)',
                    re.UNICODE)
candidates=[u'first.last@exaple.com',u'first.last+category@gmail.com',
            u'abc@foo',]
for candidate in candidates:
    match=adress.search(candidate)
    
    print '%-50s %s' % (candidate, 'Matches' if match else 'No match')

    
