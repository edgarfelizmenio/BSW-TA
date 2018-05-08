from charm.core.engine.util import objectToBytes,bytesToObject

from charm.toolbox.pairinggroup import PairingGroup
from charm.schemes.abenc.abenc_bsw07 import CPabe_BSW07
from charm.adapters.abenc_adapt_hybrid import HybridABEnc 

import json
import os

group_object = PairingGroup('SS512')
cpabe = CPabe_BSW07(group_object)
hybrid_abe = HybridABEnc(cpabe, group_object)

master_key_file_name = "master_key.json"

if not os.path.exists(master_key_file_name):
    (pk, mk) = hybrid_abe.setup()
    pk_string = str(objectToBytes(pk, group_object), 'utf-8')
    mk_string = str(objectToBytes(mk, group_object), 'utf-8')
    with open(master_key_file_name, "w") as master_key_file:
        json.dump({
            'pk': pk_string,
            'mk': mk_string        
        }, master_key_file)
else:
    with open(master_key_file_name) as master_key_file:
        master_key = json.load(master_key_file)
        pk_string = master_key['pk']
        mk_string = master_key['mk']

