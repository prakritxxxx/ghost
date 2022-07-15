import colorama

colorama.init()

print(colorama.Fore.GREEN + '''

              o                                  o     
             <|>                                <|>    
             / >                                < >    
   o__ __o/  \o__ __o      o__ __o       __o__   |     
  /v     |    |     v\    /v     v\     />  \    o__/_ 
 />     / \  / \     <\  />       <\    \o       |     
 \      \o/  \o/     o/  \         /     v\      |     
  o      |    |     <|    o       o       <\     o     
  <\__  < >  / \    / \   <\__ __/>  _\o__</     <\__  
         |                                             
 o__     o                                             
 <\__ __/>     
made by cipher!
enjoy it!
if you use it pls mention the creator!
''')





while True:
    var1=input(colorama.Fore.GREEN + "Enter the command: ")
    
    var2 = input(colorama.Fore.GREEN + "Enter user: ")

    if var1 == 'help':
        print(colorama.Fore.GREEN + '''
                 [+] instagram   ---> -i
                 [+] facebook    ---> -f
                 [+] twitch      ---> -t
                 [+] reddit      ---> -r
                 [+] twitter     ---> -tw
                 [+] printest    ---> -p
                 ''')
    if var1 == '-i':
        print(colorama.Fore.GREEN + f"https://www.instagram.com/{var2}/")
    else:
         print(colorama.Fore.GREEN + "[+] NO user found")

    if var1 == '-f':
        print(colorama.Fore.GREEN + f"https://www.facebook.com/{var2}")

    else:
         print(colorama.Fore.GREEN + "[+] NO user found")
    if var1 == '-t':
        print(colorama.Fore.GREEN + f"https://www.twitch.tv/{var2}")

    else:
         print(colorama.Fore.GREEN + "[+] NO user found")   
    if var1 == '-r':
        print(colorama.Fore.GREEN + f"https://www.reddit.com/user/{var2}/")
    
    else:
         print(colorama.Fore.GREEN + "[+] NO user found")

    if var1 == '-tw':
        print(colorama.Fore.GREEN + f"https://twitter.com/{var2}")
    
    else:
         print(colorama.Fore.GREEN + "[+] NO user found")

    if var1 == '-p':
        print(colorama.Fore.GREEN + f"https://in.pinterest.com/{var2}/")
    
    else:
         print(colorama.Fore.GREEN + "[+] NO user found")
