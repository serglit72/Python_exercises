def disemvowel(string):
    vowels = ['a','e','i','o','u']
    
    for each in string:
        if each.lower() in vowels:
            string = string.replace(each,'')
            
    return string

if __name__ == "__main__":
    string = "This website is for losers LOL!"
    
    
    print(disemvowel(string))