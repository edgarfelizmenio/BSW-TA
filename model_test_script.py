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

user_db = {}
for k,v in users.items():
    user_db[k] = models.add_user(v)

for k,v in user_db.items():
    print(k, v['user_id'], v['private_key'][:20])

for k,v in user_db.items():
    user = models.get_user(v['user_id'])
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
    updated_user_db[k] = models.update_user(user_db[k]['user_id'], v)

for k,v in updated_user_db.items():
    print(k, v['user_id'], v['private_key'][:20])

for k,v in user_db.items():
    user = models.get_user(v['user_id'])
    print(user)

master_key = models.get_master_key()
print("pk", master_key['pk'])
print("mk", master_key['mk'])