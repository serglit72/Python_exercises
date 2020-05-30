# end_other('Hiabc', 'abc') → True
# end_other('AbC', 'HiaBc') → True
# end_other('abc', 'abXabc') → True

def end_other(a, b):
    len_a = len(a)
    len_b = len(b)
  
    if len_a >= len_b:
        return(b.lower() == a[-len_b:].lower())           
    return(a.lower() == b[-len_a:].lower())
        


print(end_other('ti','alsjtykhdflfty'))