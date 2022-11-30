Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #tuple
>>> 
>>> t=(21,36,14,25)
>>> t[1]
36
>>> 
>>> #Sets
>>> 
>>> s={98,28,13,98}
>>> s
{98, 28, 13}
>>> 
>>> #Dictionary
>>> 
>>> d={1:'abhi',2:'dev',4:'ram'}
>>> d[4]
'ram'
>>> 
>>> 
>>> d.get(3)
>>> d.get(3,'NA')
'NA'
>>> 
>>> k=['blg','chen','mum']
>>> v=['kar','TN','MH']
>>> d=dict(zip(k,v))
>>> d= dict(zip(k,v))
>>> dict(zip(k,v))
{'blg': 'kar', 'chen': 'TN', 'mum': 'MH'}
>>> d['hyd']='tel'
>>> d['chen']='tel'
>>> dict(zip(k,v))
{'blg': 'kar', 'chen': 'TN', 'mum': 'MH'}
>>> del d['mum']
>>> dict(zip(k,v))
{'blg': 'kar', 'chen': 'TN', 'mum': 'MH'}
>>> d
{'blg': 'kar', 'chen': 'tel', 'hyd': 'tel'}
