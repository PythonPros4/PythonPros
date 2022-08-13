print('GAME RULES')
print('Do not use CAPITAL letters while playing.')
gender = input('Male or Female? ')
username = input('Make a username ')
print('Welcome to EnviRush, ' + username)
print('Get ready for a mind-blowing journey')

print(' Narrator : Welcome to this world ' + username)
print('You are walking from work to your home.You see a truck passing by. ')
print('The truck deposited chemicals and gave off a toxic smell')
choice = input('Do you wish to investigate?  Yes/No ')
if choice == 'yes':
    print('You climb on the back of the truck without the driver knowing')

if choice == 'no':
    print('The next day you see the truck doing the same thing again.')
    print('You muster enough courage to follow the truck and climb on its back ')

print('The truck leads you to a secret factory.')
fusion = input('Trespass inside the factory. Yes/No ')

if fusion == 'yes':
    print('You find plenty of test labs,scientists and workers moving chemicals')

if fusion == 'no':
    print('You see the driver getting out with a few workers')
    print('you get inside with a suspicious feeling.')
    print('You find plenty of test labs,scientists and workers moving chemicals')

secrecy = input('Go undercover as a worker or scientist. Scientist/Worker ')

if secrecy == 'scientist':
    print('You wear a scientist disguise and go inside a test lab')
    print('A scientist comes near you')
    print('Scientist: We need more workers for a new scheme, I apologize but we have more than enough scientists.')
    print('so we need you to help out the workers but still have the same salary')
    print('You: I understand. ')
    print(username + ' is now undercover as a worker')

if secrecy == 'worker':
    print(username + ' is now undercover as a worker')

print('You go to another worker and say that you are new and need information on this association ')
print('Worker: (gives a snarl) you think I am so gullible? You might be a spy...')
rickroll = input('Threaten or bribe? ')

if rickroll == 'bribe':
    print('You give him cash, to make him speak.')
    print('Worker: Now that is more like it.')

if rickroll == 'threaten':
    print('You: I will hurt you if you do not tell me about this.')
    print('Worker: Stop it (Screaming)!')
    print('You: Fine, Stop Screaming! I will give you money and only if you give me information...')

print('Worker: This association is known as EAP (Environmental Alteration Plant). We Illegally Dump Chemicals into the')
print('oceans and on land in order to make sure that our experiments work properly. We got paid to not spread the news')
print('to the public.')

call = input('Do you want to call the Police or the National Environment Agency. Police/NEA ')

if call == 'police':
    print('You have called the police. Well Done! They have terminated the Plant and arrested the executives.')
    print('GAME OVER')

if call == 'nea':
    print('You have contacted the NEA. Well done! The National Environmental Agency will take over from here.')
    print('GAME OVER')


