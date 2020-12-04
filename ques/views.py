from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.

questionsList = [
    {
<<<<<<< HEAD
        'index': 0,
=======
        'index':0,
>>>>>>> e3406deb98bfead647438876f2fbc86acf2046aa
        'question': 'Q1. Where would you go on vacation?',
        'choice': ['a)Beach', 'b)Mountain', 'c)City', 'd)Theme Park', 'e)Forest'],

    },
<<<<<<< HEAD
    {'index': 1,
     'question': 'Q2. where would you like to live?',
     'choice': ['a)Mansion', 'b)Apartment', 'c)Penthouse', 'd)Cabin', 'e)Beach House']

     },
    {'index': 2,
     'question': 'Q3. What is your favorite colour',
     'choice': ['a)Gold', 'b)Black', 'c)Green', 'd)Fiery Red', 'e)Electric Blue']

     },
    {'index': 3,
     'question': 'Q4)Favorite genre of games?',
     'choice': ['a)Strategy', 'b)Stealth Action', 'c)Action', 'd)Action-Adventure', 'e)Horror']

     },
    {'index': 4,
     'question': 'Q5)Which civilisation would you be a part of?',
     'choice': ['a)Greek', 'b)Egypt', 'c)Romans', 'd)Viking', 'e)Japanese']

     },
    {'index': 5,
     'question': 'Q6)What would you do during your free time?',
     'choice': ['a)Work on your plan to rule the world', 'b)Play a prank', 'c)Read', 'd)Start a fight',
                'e)Play a sport']

     },
    {'index': 6,
     'question': 'Q7)What is your favourite series?',
     'choice': ['a)The Crown', 'b)The Americans', 'c)Brooklyn 99', 'd)Stranger Things', 'e)Chernobyl']
=======
    {   'index':1,
        'question': 'Q2. where would you like to live?',
        'choice': ['a)Mansion', 'b)Apartment', 'c)Penthouse', 'd)Cabin', 'e)Beach House']

    },
    {   'index':2,
        'question': 'Q3. What is your favorite colour',
        'choice': ['a)Gold', 'b)Black', 'c)Green', 'd)Fiery Red', 'e)Electric Blue']

    },
    {   'index':3,
        'question': 'Q4)Favorite genre of games?',
        'choice': ['a)Strategy', 'b)Stealth Action', 'c)Action', 'd)Action-Adventure', 'e)Horror']

    },
    {   'index':4,
        'question': 'Q5)Which civilisation would you be a part of?',
        'choice': ['a)Greek', 'b)Egypt', 'c)Romans', 'd)Viking', 'e)Japanese']

    },
   {'index':5,
        'question': 'Q6)What would you do during your free time?',
        'choice': ['a)Work on your plan to rule the world', 'b)Play a prank', 'c)Read', 'd)Start a fight', 'e)Play a sport']

    },
    {'index':6,
        'question': 'Q7)What is your favourite series?',
        'choice': ['a)The Crown', 'b)The Americans', 'c)Brooklyn 99', 'd)Stranger Things', 'e)Chernobyl']
>>>>>>> e3406deb98bfead647438876f2fbc86acf2046aa

     }

]

count = [0] * 5
ship = [
    {
<<<<<<< HEAD
        'name': 'INS Vikramaditya:',
        'desc': 'Greetings your highness, just like INS Vikramaditya is the peerless crown jewel of the Indio-Pacific, so are you in your life. You are the centre of attention and all people seem to revolve around you. You are seemingly unstoppable and ability too single-handedly change the balance of power.',
        'img': 'https://economictimes.indiatimes.com/thumb/msid-55372917,width-1200,height-900,resizemode-4,imgsize-50822/news/defence/ins-vikramaditya-ready-to-go-back-to-sea-after-refit-works.jpg?from=mdr',
    }, {
        'name': 'INS Arihant:',
        'desc': 'You are secret, suave and strong. You are a silent and hidden predator. People often underestimate your full capability and pay dearly for their ignorance. You are not the centre of the attention but that doesn’t matter, does it? Your presence looms like the sword of Damocles over your enemies.',
        'img': 'https://www.thehindu.com/news/national/article19862548.ece/ALTERNATES/FREE_660/TH15ARIHANT',
    }, {
        'name': 'INS Satpura:',
        'desc': 'The jack of all trades but the master of none is the perfect description for you. You have an endlessly diverse skillset, ensuring your usefulness in any scenario. Your versatility means that you have a varied range of experiences allowing you to have an ironclad grasp of any situation making you the MVP of your team ',
        'img': 'https://upload.wikimedia.org/wikipedia/commons/9/94/Indian_Navy_frigate_Satpura_%28F_48%29_arrives_at_Joint_Base_Pearl_Harbor-Hickam_for_Rim_of_the_Pacific_2016.jpg',
    }, {
        'name': 'INSV Tarini:',
        'desc': 'Adventure seeks you. A breathtaking experience of others is a quiet Tuesday afternoon for you. People describe you as either incredibly brave but you are too busy enjoying life to pay attention to them, after all, they seem too boring and slow to you. You do things without much rhyme or reason except that you can. ',
        'img': 'https://upload.wikimedia.org/wikipedia/commons/8/88/Navika_Sagar_Parikrama_sets_sail%2C_2017.jpg',
    }, {
        'name': 'INS Kolkata:',
        'desc': 'You are an unstoppable juggernaut, you slow down for no one and constantly conquer all obstacles within your path. Your plan of attack is often one word, attack. Aggression is your first, second and only nature. You run into the fray, and like to get up and close to your problems. You don’t solve problems, problems seem to cease their existence once you’re done with them.',
        'img': 'https://miro.medium.com/max/752/1*en0yGb9vCFIeMFgjLmxdcQ.jpeg',
=======
        'name' : 'INS Vikramaditya:',
        'desc' : 'Greetings your highness, just like INS Vikramaditya is the peerless crown jewel of the Indio-Pacific, so are you in your life. You are the centre of attention and all people seem to revolve around you. You are seemingly unstoppable and ability too single-handedly change the balance of power.',
        'img'  : 'https://economictimes.indiatimes.com/thumb/msid-55372917,width-1200,height-900,resizemode-4,imgsize-50822/news/defence/ins-vikramaditya-ready-to-go-back-to-sea-after-refit-works.jpg?from=mdr',
    },{
        'name' : 'INS Arihant:',
        'desc' : 'You are secret, suave and strong. You are a silent and hidden predator. People often underestimate your full capability and pay dearly for their ignorance. You are not the centre of the attention but that doesn’t matter, does it? Your presence looms like the sword of Damocles over your enemies.',
        'img'  : 'https://www.thehindu.com/news/national/article19862548.ece/ALTERNATES/FREE_660/TH15ARIHANT',
    },{
        'name' : 'INS Satpura:',
        'desc' : 'The jack of all trades but the master of none is the perfect description for you. You have an endlessly diverse skillset, ensuring your usefulness in any scenario. Your versatility means that you have a varied range of experiences allowing you to have an ironclad grasp of any situation making you the MVP of your team ',
        'img'  : 'https://upload.wikimedia.org/wikipedia/commons/9/94/Indian_Navy_frigate_Satpura_%28F_48%29_arrives_at_Joint_Base_Pearl_Harbor-Hickam_for_Rim_of_the_Pacific_2016.jpg',
    },{
        'name' : 'INSV Tarini:',
        'desc' : 'Adventure seeks you. A breathtaking experience of others is a quiet Tuesday afternoon for you. People describe you as either incredibly brave but you are too busy enjoying life to pay attention to them, after all, they seem too boring and slow to you. You do things without much rhyme or reason except that you can. ',
        'img'  : 'https://upload.wikimedia.org/wikipedia/commons/8/88/Navika_Sagar_Parikrama_sets_sail%2C_2017.jpg',
    },{
        'name' : 'INS Kolkata:',
        'desc' : 'You are an unstoppable juggernaut, you slow down for no one and constantly conquer all obstacles within your path. Your plan of attack is often one word, attack. Aggression is your first, second and only nature. You run into the fray, and like to get up and close to your problems. You don’t solve problems, problems seem to cease their existence once you’re done with them.',
        'img'  : 'https://miro.medium.com/max/752/1*en0yGb9vCFIeMFgjLmxdcQ.jpeg',
>>>>>>> e3406deb98bfead647438876f2fbc86acf2046aa
    },
]


def home(request):
    global count
    count = [0 for x in count]
    data = {
        'questions': questionsList
    }
    if request.method == "POST":
<<<<<<< HEAD

        try:

            for i in range(7):
                ans = request.POST[str(i)]
                count[int(ans) - 1] += 1
                return redirect('ans-url')
        except:
            messages.info(request, 'Please answer all the question')



=======
        
        try:
            
            for i in range(7):
                ans = request.POST[str(i)]
                count[int(ans)-1] += 1
        except:
            messages.info(request, 'Please answer all the question')


            return redirect('ans-url')

>>>>>>> e3406deb98bfead647438876f2fbc86acf2046aa
    return render(request, template_name="ques/home.html", context=data)


def ans(request):
    output = count.index(max(count))
    data = {
        'ship': ship[output]
    }
<<<<<<< HEAD
    return render(request, template_name='ques/ans.html', context=data)
=======
    return render(request, template_name='ques/ans.html',context=data)
>>>>>>> e3406deb98bfead647438876f2fbc86acf2046aa
