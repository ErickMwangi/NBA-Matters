from random import choice as rc
import random
from faker import Faker
from app import app
from models import db, Team, Player, Team_player

fake = Faker()

with app.app_context():
    Team_player.query.delete()
    Team.query.delete()
    Player.query.delete()
    players = [
        Player(
            name='Kareem Abdul-Jabbar',
            team='Los Angeles Lakers',
            image='https://i.pinimg.com/564x/e8/d4/ef/e8d4efb9e81a347d5e9ef125df0c70f4.jpg'
        ),
        Player(
            name='Wilt Chamberlain',
            team='Los Angeles Lakers',
            image='https://i.pinimg.com/564x/7b/9f/fb/7b9ffb70f907ab9927b159165d1be03f.jpg'
            ),
        Player(
            name='Bill Russell',
            team='Boston Celtics',
            image='https://i.pinimg.com/564x/98/ea/5b/98ea5b3e08928d0f6bc25dd4da4adb1e.jpg'
        ),
        Player(
            name='Larry Bird',
            team='Boston Celtics',
            image='https://i.pinimg.com/564x/9f/54/c2/9f54c28a7e0b7feb7815eb8d4afccf99.jpg'
            ),
        Player(
            name='Magic Johnson',
            team='Los Angeles Lakers',
            image='https://i.pinimg.com/564x/d5/d6/a0/d5d6a09f400f1a91379f30bf07ad1c51.jpg'
        ),
        Player(
            name='Michael Jordan',
            team='Chicago Bulls',
            image='https://i.pinimg.com/564x/cb/62/a3/cb62a3628740a7e9ce8c94cf2ae1e5d4.jpg'
            ),
        Player(
            name='Lebron James',
            team='Los Angeles Lakers',
            image='https://i.pinimg.com/564x/90/83/72/90837220b539484626e98b098e7aacc7.jpg'
        ),
        Player(
            name='Nicola Jokic',
            team='Denver Nuggets',
            image='https://i.pinimg.com/564x/6d/cd/b6/6dcdb6716e5ab0db8f3f8a856403184c.jpg'
            ),
        Player(
            name='Kobe Bryant',
            team='Los Angeles Lakers',
            image='https://i.pinimg.com/564x/c9/c5/d3/c9c5d3b3609bd2b2c66a9399cd58f99c.jpg'
        ),
        Player(
            name='Karl Malone',
            team='Utah Jazz',
            image='https://i.pinimg.com/564x/2b/a9/91/2ba991400fd8dcad40db250714482e5c.jpg'
            ),
        Player(
            name='Ja Morant',
            team='Memphis Grizzles',
            image='https://i.pinimg.com/564x/d3/bd/f9/d3bdf97adc304f7676fe74150877f429.jpg'
        ),
        Player(
            name='Stephen Curry',
            team='Golden State Warriors',
            image='https://i.pinimg.com/564x/40/98/33/4098333f762b134b0b96d2a3cfa70ff6.jpg'
            ),
        Player(
            name='Kevin Durant',
            team='Phoenix Suns',
            image='https://i.pinimg.com/564x/20/6b/ab/206bab0bc43c5ba154752fdabfd81411.jpg'
        ),
        Player(
            name='Dwayne wade',
            team='Miami Heat',
            image='https://i.pinimg.com/564x/04/7a/55/047a55a7f43040e46aadf20c74155b40.jpg'
            ),
        Player(
            name='Lamello Ball',
            team='Charlotte Hornets',
            image='https://i.pinimg.com/564x/a0/61/f1/a061f14beef913271355a4484de84e75.jpg'
        ),
        Player(
            name='Giannis Antetokounmpo',
            team='Milwaukee Bucks',
            image='https://i.pinimg.com/564x/58/20/e5/5820e5f903493ccd3746259b9ddda30f.jpg'
            ),
        Player(
            name='Damian Lillard',
            team='Portland Trail Blazers',
            image='https://i.pinimg.com/564x/b8/e8/af/b8e8afd8d0923f35bffd0a69246f8e59.jpg'
        ),
        Player(
            name='Jimmy Butler',
            team='Miami Heat',
            image='https://i.pinimg.com/564x/d8/a1/f8/d8a1f859db09b18a736eefde99807585.jpg'
            ),
        Player(
            name='Paul George',
            team='LA Clippers',
            image='https://i.pinimg.com/564x/04/cc/ca/04cccaee718e5a9afe93b0d6e543eda0.jpg'
        ),
        Player(
            name=' Anthony Davis ',
            team='Lakers',
            image='https://i.pinimg.com/564x/96/fd/9e/96fd9ec0f0d57dc8c893cac9f35fa7a2.jpg'
            ),
    ]
        
    db.session.add_all(players)
    teams = []
    ranking = ['high', 'low']
    mvp = ['Kobe Bryant', 'Stephen Curry', 'Lebron James']

    for _ in range(20):
        t = Team(
            name=fake.name(),
            # ranking=rc(ranking),
            # mvp=rc(mvp),
        )
        teams.append(t)

    db.session.add_all(players + teams)
    db.session.commit()

    # Create team-player relationships
    team_player = []
    player_ids = [player.id for player in players]
    team_ids = [team.id for team in teams]
    
    for _ in range(20):
        tp = Team_player(
            team_id=random.choice(team_ids),
            player_id=random.choice(player_ids)
        )
        team_player.append(tp)
    
    db.session.add_all(team_player)
    db.session.commit()

    