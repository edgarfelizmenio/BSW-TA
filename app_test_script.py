import requests
import models

models.clear_tables()

users = {
    'Akande': {
        'first_name': 'Akande',
        'last_name': 'Ogundimu',
        'attributes': ['CANNON', 'SLAM', 'UPPERCUT', 'PUNCH', 'METEOR']
    },
    'Genji': {
        'first_name': 'Genji',
        'last_name': 'Shimada',
        'attributes': ['SHURIKEN', 'DEFLECT', 'SWIFT', 'STRIKE', 'DRAGONBLADE']
    },
    'Jesse': {
        'first_name': 'Jesse',
        'last_name': 'McCree',
        'attributes': ['PEACEKEEPER', 'COMBAT', 'ROLL', 'FLASHBANG', 'DEADEYE']
    },
    'Fareeha': {
        'first_name': 'Fareeha',
        'last_name': 'Amari',
        'attributes': ['ROCKET', 'JUMP', 'CONCUSSIVE', 'BLAST', 'BARRAGE']
    },
    'Gabriel': {
        'first_name': 'Gabriel',
        'last_name': 'Reyes',
        'attributes': ['HELLFIRE', 'SHOTGUNS', 'WRAITH', 'SHADOW', 'DEATH']
    },
}

headers = {'Content-Type': 'application/json'}
host = 'http://127.0.0.1:4000'

user_db = {}
for k,v in users.items():
    user_db[k] = requests.post('{}/user'.format(host),
                               json=v,
                               headers=headers).json()

for k,v in user_db.items():
    print(k, v['user_id'], v['private_key'][:20])

for k,v in user_db.items():
    user = requests.get('{}/user/{}'.format(host, v['user_id'])).json()
    print(user)

updates = {}
updates['Akande'] = {
    'first_name': 'doomfist',
    'attributes': 'METEOR STRIKE INCOMING'.split()
}
updates['Genji'] = {
    'first_name': 'dragon',
    'attributes': 'RYUJIN NO KEN WO KURAE'.split()
}
updates['Jesse'] = {
    'first_name': 'highnoon',
    'attributes': 'LIKE SHOOTING FISH IN A BARRELL'.split()
}
updates['Fareeha'] = {
    'first_name': 'pharah',
    'attributes': 'JUSTICE RAINS FROM ABOVE'.split()
}
updates['Gabriel'] = {
    'first_name': 'reaper',
    'attributes': 'CLEARING THE AREA'.split()
}

updated_user_db = {}
for k, v in updates.items():
    updated_user_db[k] = requests.put('{}/user/{}'.format(host, user_db[k]['user_id']),
                                      json=v,
                                      headers=headers).json()

for k,v in updated_user_db.items():
    print(k, v['user_id'], v['private_key'][:20])

for k,v in user_db.items():
    user = requests.get('{}/user/{}'.format(host, v['user_id'])).json()
    print(user)

master_key = requests.get('{}/masterkey'.format(host))
print("pk", master_key.json()['pk'])
print("mk", master_key.json()['mk'])
